# Google Multimodal Agent Skill

A Hermes skill for generating, analyzing, and editing images and videos using Google's latest generative AI models (Gemini, Imagen, Veo) via the Gemini Enterprise Agent Platform.

## ✨ Features

- 🖼️ **Image Generation** - Generate high-quality images using Imagen 4 and Gemini Image models
- 🎥 **Video Generation** - Create videos up to 60 seconds with Veo 3 models
- 🔍 **Multimodal Understanding** - Analyze and query images and video content
- 🚀 **Prompt Optimization** - Automatic prompt enrichment using Gemini 3.1 Flash-Lite
- ⚙️ **Customizable Defaults** - Configure default models and output directory
- 📝 **Model Aliases** - User-friendly model names instead of technical IDs

## 🧰 Supported Models

### Multimodal LLMs
| Friendly Name | Model ID |
|:------------ |:------- |
| `Gemini 3.1 Flash-Lite` | `gemini-3.1-flash-lite` |
| `Gemini 3.5 Flash` | `gemini-3.5-flash` |
| `Gemini 3 Pro` | `gemini-3.0-pro-preview-001` |

### Image Generation
| Friendly Name | Model ID |
|:------------ |:------- |
| `Gemini 3.1 Flash Image` | `gemini-3.1-flash-image` |
| `Imagen 4 Ultra` | `imagen-4.0-ultra-generate-001` |
| `Imagen 4` | `imagen-4.0-generate-001` |

### Video Generation
| Friendly Name | Model ID |
|:------------ |:------- |
| `Veo 3.1 Fast` | `veo-3.1-fast-generate-001` |
| `Veo 3.1` | `veo-3.1-generate-preview` |
| `Veo 3.1 Lite` | `veo-3.1-lite-generate-preview` |

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Google Cloud account with Vertex AI enabled
- Google Cloud credentials configured

### Installation for Hermes

1. Clone or copy this skill to your Hermes skills directory:
   ```bash
   cd ~/.hermes/skills/
   git clone https://github.com/Slvyi/google-multimodal-agent.git
   ```

2. Install dependencies:
   ```bash
   pip install google-generativeai
   ```

3. Initialize configuration:
   ```bash
   cd ~/.hermes/skills/google-multimodal-agent
   python scripts/multimodal_tool.py init \
     --output_dir ~/workspace/outputs \
     --image_model "Gemini 3.1 Flash Image" \
     --multimodal_model "Gemini 3.1 Flash-Lite" \
     --video_model "Veo 3.1 Fast"
   ```

## 💡 Usage

### Generate an Image
```bash
python scripts/multimodal_tool.py image-gen --prompt "A serene Japanese garden at sunset" --optimize
```

### Generate a Video
```bash
python scripts/multimodal_tool.py video-gen --prompt "Ocean waves crashing on rocks" --duration 8 --optimize
```

### Analyze an Image
```bash
python scripts/multimodal_tool.py image-query --file ~/workspace/image.png --prompt "Describe this image in detail"
```

### Specify a Different Model
```bash
python scripts/multimodal_tool.py image-gen --prompt "Ultra realistic portrait" --model "Imagen 4 Ultra" --optimize
```

## 📁 Project Structure

```
google-multimodal-agent/
├── README.md           # This file
├── SKILL.md            # Hermes skill definition (English)
├── SKILL_ZH.md         # Hermes skill definition (Chinese)
├── config.json         # Configuration file (not in repo)
├── .gitignore          # Git ignore rules
├── scripts/
│   └── multimodal_tool.py  # Main script
├── assets/             # Skill assets
├── references/         # Reference documents
└── tests/              # Test files
```

## ⚙️ Configuration

The `config.json` file stores your personal settings:

```json
{
    "output_dir": "/home/ubuntu/workspace/outputs",
    "default_image_model": "Gemini 3.1 Flash Image",
    "default_video_model": "Veo 3.1 Fast",
    "default_multimodal_model": "Gemini 3.1 Flash-Lite"
}
```

## 🤖 Hermes Integration

This skill is designed for use with Hermes Agent. When installed, Hermes will automatically:
- Load the skill definition from `SKILL.md`
- Recognize image/video generation requests
- Apply prompt optimization best practices
- Follow the user's preferred model selection order

## 📄 License

MIT License - feel free to use and modify!

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.
