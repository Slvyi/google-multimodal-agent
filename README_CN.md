# Google Multimodal Agent Skill

Hermes 技能，调用 Google 的 Gemini、Imagen、Veo 模型处理图片和视频。

## 功能
- 生成图片（Imagen 4 / Gemini Image）
- 生成视频（Veo 3，最长60秒）
- 分析图片/视频内容
- 自动优化提示词
- 可以自己改默认模型和输出目录
- 模型用友好名称，不用记ID

## 支持的模型

### 多模态理解模型
| 名称 | 对应ID |
|:--- |:----- |
| Gemini 3.1 Flash-Lite | gemini-3.1-flash-lite |
| Gemini 3.5 Flash | gemini-3.5-flash |
| Gemini 3.1 Flash | gemini-3.1-flash-preview |

### 图片生成
| 名称 | 对应ID |
|:--- |:----- |
| Gemini 3.1 Flash Image | gemini-3.1-flash-image |
| Gemini 3 Pro Image | gemini-3-pro-image |
| Gemini 2.5 Flash Image | gemini-2.5-flash-image |
| Imagen 4 Ultra | imagen-4.0-ultra-generate-001 |
| Imagen 4 | imagen-4.0-generate-001 |

### 视频生成
| 名称 | 对应ID |
|:--- |:----- |
| Veo 3.1 Fast | veo-3.1-fast-generate-001 |
| Veo 3.1 | veo-3.1-generate-001 |
| Veo 3.1 Lite | veo-3.1-lite-generate-001 |

## 安装

需要先装好 Python 3.8+，还有 Google Cloud 凭证。

配置 Google Cloud 应用程序默认凭证 (ADC)：
```bash
bash <(curl -sSL https://storage.googleapis.com/cloud-samples-data/adc/setup_adc.sh)
```

安装 Python 依赖：
```bash
pip install google-generativeai
```

放到 Hermes 技能目录：
```bash
cd ~/.hermes/skills/
git clone https://github.com/Slvyi/google-multimodal-agent.git
```

初始化配置：
```bash
cd ~/.hermes/skills/google-multimodal-agent
python scripts/multimodal_tool.py init \
  --output_dir ~/workspace/outputs \
  --image_model "Gemini 3.1 Flash Image" \
  --multimodal_model "Gemini 3.1 Flash-Lite" \
  --video_model "Veo 3.1 Fast"
```

## 怎么用

生成图片：
```bash
python scripts/multimodal_tool.py image-gen --prompt "夕阳下的日式花园" --optimize
```

生成视频：
```bash
python scripts/multimodal_tool.py video-gen --prompt "海浪拍岩石" --duration 8 --optimize
```

分析图片：
```bash
python scripts/multimodal_tool.py image-query --file ~/workspace/image.png --prompt "描述这张图"
```

换个模型生成：
```bash
python scripts/multimodal_tool.py image-gen --prompt "写实人像" --model "Imagen 4 Ultra" --optimize
```

## 目录结构

```
google-multimodal-agent/
├── README.md
├── README_CN.md
├── SKILL.md
├── SKILL_ZH.md
├── config.json          # 自己的配置，不上传
├── .gitignore
├── scripts/
│   └── multimodal_tool.py
├── assets/
├── references/
└── tests/
```

## 配置

config.json 里存这些：
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
