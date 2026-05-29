# Google Multimodal Agent Skill

Hermes skill for working with Google's Gemini, Imagen, and Veo models to generate and analyze images and videos.

## What it does
- Image generation with Imagen 4 and Gemini Image models
- Video generation up to 60 seconds with Veo 3
- Image and video content analysis
- Automatic prompt optimization
- Customizable default models and output directory
- User-friendly model names instead of technical IDs

## Supported Models

### Multimodal LLMs
| Name | Model ID |
|:--- |:------- |
| Gemini 3.1 Flash-Lite | gemini-3.1-flash-lite |
| Gemini 3.5 Flash | gemini-3.5-flash |
| Gemini 3.1 Flash | gemini-3.1-flash-preview |

### Image Generation
| Name | Model ID |
|:--- |:------- |
| Gemini 3.1 Flash Image | gemini-3.1-flash-image |
| Gemini 3 Pro Image | gemini-3-pro-image |
| Gemini 2.5 Flash Image | gemini-2.5-flash-image |
| Imagen 4 Ultra | imagen-4.0-ultra-generate-001 |
| Imagen 4 | imagen-4.0-generate-001 |

### Video Generation
| Name | Model ID |
|:--- |:------- |
| Veo 3.1 Fast | veo-3.1-fast-generate-001 |
| Veo 3.1 | veo-3.1-generate-001 |
| Veo 3.1 Lite | veo-3.1-lite-generate-001 |

## Installation

You need Python 3.8+ and Google Cloud credentials.

Set up Google Cloud Application Default Credentials (ADC):
```bash
bash <(curl -sSL https://storage.googleapis.com/cloud-samples-data/adc/setup_adc.sh)
```

Install Python dependencies:
```bash
pip install google-generativeai
```

Clone into your Hermes skills folder:
```bash
cd ~/.hermes/skills/
git clone https://github.com/Slvyi/google-multimodal-agent.git
```

Initialize config:
```bash
cd ~/.hermes/skills/google-multimodal-agent
python scripts/multimodal_tool.py init \
  --output_dir ~/workspace/outputs \
  --image_model "Gemini 3.1 Flash Image" \
  --multimodal_model "Gemini 3.1 Flash-Lite" \
  --video_model "Veo 3.1 Fast"
```

## Usage

Generate an image:
```bash
python scripts/multimodal_tool.py image-gen --prompt "Japanese garden at sunset" --optimize
```

Generate a video:
```bash
python scripts/multimodal_tool.py video-gen --prompt "Ocean waves hitting rocks" --duration 8 --optimize
```

Analyze an image:
```bash
python scripts/multimodal_tool.py image-query --file ~/workspace/image.png --prompt "Describe this image"
```

Use a different model:
```bash
python scripts/multimodal_tool.py image-gen --prompt "Realistic portrait" --model "Imagen 4 Ultra" --optimize
```

## Project Structure

```
google-multimodal-agent/
├── README.md
├── README_CN.md
├── SKILL.md
├── SKILL_ZH.md
├── config.json          # Local config, not in repo
├── .gitignore
├── scripts/
│   └── multimodal_tool.py
├── assets/
├── references/
└── tests/
```

## Config

config.json stores your personal settings:
```json
{
    "output_dir": "/home/ubuntu/workspace/outputs",
    "default_image_model": "Gemini 3.1 Flash Image",
    "default_video_model": "Veo 3.1 Fast",
    "default_multimodal_model": "Gemini 3.1 Flash-Lite"
}
```

## License
MIT
