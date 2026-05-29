---
name: google-multimodal-agent
description: Use when the user requests generating, analyzing, or editing images and videos using Google's generative AI models (Imagen, Veo, Gemini).
---

# Google Multimodal Agent (User Defaults v2026.05)

## Overview
This skill provides a helper script (`scripts/multimodal_tool.py`) to interact with the **Gemini Enterprise Agent Platform**. 

## Current Default Models
- **Multimodal (Understanding & Reasoning)**: `Gemini 3.1 Flash-Lite`
- **Image Generation**: `Gemini 3.1 Flash Image` (Nano Banana 2)
- **Video Generation**: `Veo 3.1 Fast` (`veo-3.1-fast-generate-001`)

## Initialization
Settings are stored in the skill directory. To re-initialize:
```bash
python scripts/multimodal_tool.py init --output_dir ~/workspace/outputs --image_model "Gemini 3.1 Flash Image" --multimodal_model "Gemini 3.1 Flash-Lite" --video_model "Veo 3.1 Fast"
```

## Supported Model Aliases
Use these friendly names for best results:

| Category | Friendly Name (Alias) | Model ID |
| :--- | :--- | :--- |
| **Multimodal LLM** | `Gemini 3.1 Flash-Lite` | `gemini-3.1-flash-lite` |
| | `Gemini 3.5 Flash` | `gemini-3.5-flash` |
| | `Gemini 3.1 Flash` | `gemini-3.1-flash-preview` |
| **Image Generation** | `Gemini 3.1 Flash Image` | `gemini-3.1-flash-image` |
| | `Gemini 3 Pro Image` | `gemini-3-pro-image` |
| | `Gemini 2.5 Flash Image` | `gemini-2.5-flash-image` |
| | `Imagen 4 Ultra` | `imagen-4.0-ultra-generate-001` |
| | `Imagen 4` | `imagen-4.0-generate-001` |
| **Video Generation** | `Veo 3.1 Fast` | `veo-3.1-fast-generate-001` |
| | `Veo 3.1` | `veo-3.1-generate-001` |
| | `Veo 3.1 Lite` | `veo-3.1-lite-generate-001` |

## Prompt Optimization (Dual-Track)
1. **Interactive**: Agent clarifies vague prompts with the user.
2. **Automatic**: Script uses `Gemini 3.1 Flash-Lite` (default) to enrich prompts via the `--optimize` flag.

## CLI Usage
- **Image**: `python scripts/multimodal_tool.py image-gen --prompt "..." --optimize` (Uses `Gemini 3.1 Flash Image` by default)
- **Video**: `python scripts/multimodal_tool.py video-gen --prompt "..." --duration 8 --optimize` (Uses `Veo 3.1 Fast` by default)
- **Query**: `python scripts/multimodal_tool.py image-query --file <path> --prompt "..."` (Uses `Gemini 3.1 Flash-Lite` by default)
