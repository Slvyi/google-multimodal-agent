import os
import json
import argparse
import time
from datetime import datetime
from google import genai
from google.genai import types

# --- Configuration & Paths ---
SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_FILE = os.path.join(SKILL_DIR, "config.json")
DEFAULT_OUTPUT_DIR = os.path.expanduser("~/workspace/outputs")

# --- Model Aliases (Synced with Google Cloud Docs, May 2026) ---
MODEL_ALIASES = {
    # --- Gemini (Multimodal LLMs & Image Recognition) ---
    "Gemini 3.5 Pro": "gemini-3.5-pro",
    "Gemini 3.1 Pro": "gemini-3.1-pro",
    "Gemini 3.5 Flash": "gemini-3.5-flash",
    "Gemini 3.1 Flash": "gemini-3.1-flash-preview",
    "Gemini 3.1 Flash-Lite": "gemini-3.1-flash-lite",
    "Gemini 3 Deep Think": "gemini-3-deep-think",
    
    # --- Image Generation (Gemini Image Series) ---
    "Gemini 3.1 Flash Image": "gemini-3.1-flash-image",  # Nano Banana 2, GA
    "Gemini 3 Pro Image": "gemini-3-pro-image",  # Nano Banana Pro, GA
    "Imagen 4 Ultra": "imagen-4.0-ultra-generate-001",
    "Imagen 4": "imagen-4.0-generate-001",
    "Gemini 2.5 Flash Image": "gemini-2.5-flash-image",
    
    # --- Video Generation (Veo 3.1 Series) ---
    "Veo 3.1": "veo-3.1-generate-001",  # GA
    "Veo 3.1 Fast": "veo-3.1-fast-generate-001",  # GA
    "Veo 3.1 Lite": "veo-3.1-lite-generate-001",  # Preview with sound
}
# Inverse mapping for display
ID_TO_ALIAS = {v: k for k, v in MODEL_ALIASES.items()}

def get_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {}

def save_config(config):
    os.makedirs(SKILL_DIR, exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)

def get_client():
    project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
    location = os.environ.get("GOOGLE_CLOUD_REGION", "us-central1")
    return genai.Client(enterprise=True, project=project_id, location=location)

def save_output(content, ext, prefix, output_dir=None):
    target_dir = output_dir or DEFAULT_OUTPUT_DIR
    os.makedirs(target_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = os.path.join(target_dir, f"{prefix}_{timestamp}.{ext}")
    with open(filepath, "wb") as f:
        f.write(content)
    return filepath

def print_result(status, filepath=None, model_id=None, message=""):
    model_name = ID_TO_ALIAS.get(model_id, model_id)
    print(json.dumps({
        "status": status, 
        "file_path": filepath, 
        "model_used": model_name, 
        "message": message
    }))

def resolve_model(model_input):
    return MODEL_ALIASES.get(model_input, model_input)

# --- Task Handlers ---

def optimize_prompt_internal(client, prompt, task_type, model_id):
    """Internal helper to enrich prompt without printing to stdout."""
    system_instruction = (
        f"You are a professional prompt engineer for {task_type} generation. "
        "Expand the user's short prompt into a detailed, high-quality descriptive prompt. "
        "Return ONLY the expanded prompt text."
    )
    try:
        response = client.models.generate_content(
            model=model_id, 
            contents=f"{system_instruction}\n\nUser Prompt: {prompt}"
        )
        return response.text.strip()
    except Exception as e:
        return prompt

def handle_optimize_prompt(args):
    """Uses Gemini 3.5 Flash (User default) to enrich the prompt. Returns pure text."""
    config = get_config()
    client = get_client()
    model_id = resolve_model(args.model or config.get("default_multimodal_model", "Gemini 3.5 Flash"))
    print(optimize_prompt_internal(client, args.prompt, args.task_type, model_id))

def handle_init(args):
    config = get_config()
    config["output_dir"] = args.output_dir or config.get("output_dir", DEFAULT_OUTPUT_DIR)
    config["default_image_model"] = args.image_model or config.get("default_image_model", "Gemini 3.1 Flash Image")
    config["default_multimodal_model"] = args.multimodal_model or config.get("default_multimodal_model", "Gemini 3.5 Flash")
    config["default_video_model"] = args.video_model or config.get("default_video_model", "Veo 3.1 Fast")
    save_config(config)
    print(json.dumps({"status": "SUCCESS", "message": f"Configuration saved to {CONFIG_FILE}"}))

def handle_image_gen(args):
    config = get_config()
    client = get_client()
    model_id = resolve_model(args.model or config.get("default_image_model", "Gemini 3.1 Flash Image"))
    prompt = args.prompt
    
    if args.optimize:
        mm_model = resolve_model(config.get("default_multimodal_model", "Gemini 3.5 Flash"))
        prompt = optimize_prompt_internal(client, prompt, "image", mm_model)
    
    extra_params = json.loads(args.extra_params) if args.extra_params else {}
    config_args = {
        "aspect_ratio": args.aspect_ratio,
        "number_of_images": 1,
    }
    if args.image_size:
        config_args["image_size"] = args.image_size
    config_args.update(extra_params)
    
    try:
        result = client.models.generate_images(
            model=model_id,
            prompt=prompt,
            config=types.GenerateImagesConfig(**config_args)
        )
        filepath = save_output(
            result.generated_images[0].image.image_bytes, 
            "png", "image", 
            config.get("output_dir")
        )
        print_result("SUCCESS", filepath, model_id, message=f"Prompt used: {prompt}")
    except Exception as e:
        print_result("ERROR", message=str(e))

def handle_video_gen(args):
    config = get_config()
    client = get_client()
    model_id = resolve_model(args.model or config.get("default_video_model", "Veo 3.1 Fast"))
    prompt = args.prompt

    if args.optimize:
        mm_model = resolve_model(config.get("default_multimodal_model", "Gemini 3.5 Flash"))
        prompt = optimize_prompt_internal(client, prompt, "video", mm_model)
        
    config_args = {
        "aspect_ratio": args.aspect_ratio,
        "number_of_videos": 1,
        "duration_seconds": args.duration,
        "resolution": args.resolution,
        "person_generation": args.person_generation,
        "generate_audio": args.audio
    }
    
    kwargs = {
        "model": model_id,
        "prompt": prompt,
        "config": types.GenerateVideosConfig(**config_args)
    }
    
    if args.starting_image:
        kwargs["image"] = types.Image.from_file(location=args.starting_image)
    
    try:
        operation = client.models.generate_videos(**kwargs)
        while not operation.done:
            time.sleep(10)
            operation = client.operations.get(operation)
        
        if operation.response:
            filepath = save_output(
                operation.result.generated_videos[0].video.video_bytes, 
                "mp4", "video", 
                config.get("output_dir")
            )
            print_result("SUCCESS", filepath, model_id, message=f"Prompt used: {prompt}")
        else:
            print_result("ERROR", message="Operation completed but no video returned.")
    except Exception as e:
        print_result("ERROR", message=str(e))

def handle_image_query(args):
    config = get_config()
    client = get_client()
    model_id = resolve_model(args.model or config.get("default_multimodal_model", "Gemini 3.5 Flash"))
    try:
        with open(args.file, "rb") as f:
            image_data = f.read()
        image_part = types.Part.from_bytes(data=image_data, mime_type="image/jpeg") 
        response = client.models.generate_content(
            model=model_id,
            contents=[args.prompt, image_part]
        )
        print_result("SUCCESS", model_id=model_id, message=response.text)
    except Exception as e:
        print_result("ERROR", message=str(e))

def handle_video_query(args):
    config = get_config()
    client = get_client()
    model_id = resolve_model(args.model or config.get("default_multimodal_model", "Gemini 3.5 Flash"))
    try:
        with open(args.file, "rb") as f:
            video_data = f.read()
        # Assume mp4 for simplicity, or detect from extension
        mime_type = "video/mp4"
        if args.file.lower().endswith(".mov"): mime_type = "video/quicktime"

        video_part = types.Part.from_bytes(data=video_data, mime_type=mime_type)
        response = client.models.generate_content(
            model=model_id,
            contents=[args.prompt, video_part]
        )
        print_result("SUCCESS", model_id=model_id, message=response.text)
    except Exception as e:
        print_result("ERROR", message=str(e))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Google Multimodal Agent Tool - Atomic Operations")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # init
    p_init = subparsers.add_parser("init")
    p_init.add_argument("--output_dir")
    p_init.add_argument("--image_model", help="Default image model alias")
    p_init.add_argument("--multimodal_model", help="Default multimodal model alias")
    p_init.add_argument("--video_model", help="Default video model alias")
    
    # optimize-prompt
    p_oprompt = subparsers.add_parser("optimize-prompt")
    p_oprompt.add_argument("--prompt", required=True)
    p_oprompt.add_argument("--task_type", required=True, choices=["image", "video"])
    p_oprompt.add_argument("--model")

    # image-gen
    p_igen = subparsers.add_parser("image-gen")
    p_igen.add_argument("--prompt", required=True)
    p_igen.add_argument("--model")
    p_igen.add_argument("--aspect_ratio", default="16:9", choices=["1:1", "9:16", "16:9", "3:4", "4:3"])
    p_igen.add_argument("--image_size", choices=["1K", "2K"])
    p_igen.add_argument("--optimize", action="store_true", help="Auto-enrich prompt with Gemini")
    p_igen.add_argument("--extra_params", help="JSON string for extra config")
    
    # image-query
    p_iquery = subparsers.add_parser("image-query")
    p_iquery.add_argument("--file", required=True)
    p_iquery.add_argument("--prompt", required=True)
    p_iquery.add_argument("--model")

    # video-query
    p_vquery = subparsers.add_parser("video-query")
    p_vquery.add_argument("--file", required=True)
    p_vquery.add_argument("--prompt", required=True)
    p_vquery.add_argument("--model")
    
    # video-gen
    p_vgen = subparsers.add_parser("video-gen")
    p_vgen.add_argument("--prompt", required=True)
    p_vgen.add_argument("--starting_image", help="Path to initial image frame")
    p_vgen.add_argument("--model")
    p_vgen.add_argument("--aspect_ratio", default="16:9", choices=["16:9", "9:16"])
    p_vgen.add_argument("--duration", type=int, default=6, choices=[4, 6, 8, 10])
    p_vgen.add_argument("--resolution", default="1080p", choices=["720p", "1080p", "4k"])
    p_vgen.add_argument("--person_generation", default="allow_adult", choices=["allow_adult", "dont_allow"])
    p_vgen.add_argument("--audio", action="store_true", default=False)
    p_vgen.add_argument("--optimize", action="store_true", help="Auto-enrich prompt with Gemini")
    
    args = parser.parse_args()
    
    if args.command == "init": handle_init(args)
    elif args.command == "optimize-prompt": handle_optimize_prompt(args)
    elif args.command == "image-gen": handle_image_gen(args)
    elif args.command == "image-query": handle_image_query(args)
    elif args.command == "video-query": handle_video_query(args)
    elif args.command == "video-gen": handle_video_gen(args)

