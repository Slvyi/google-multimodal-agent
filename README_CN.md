# Google 多模态 Agent 技能

这是一个 Hermes 技能，用于通过 Gemini Enterprise Agent Platform 使用 Google 最新的生成式 AI 模型（Gemini、Imagen、Veo）生成、分析和编辑图像和视频。

## ✨ 功能特性

- 🖼️ **图像生成** - 使用 Imagen 4 和 Gemini 图像模型生成高质量图像
- 🎥 **视频生成** - 使用 Veo 3 模型创建最长 60 秒的视频
- 🔍 **多模态理解** - 分析和查询图像与视频内容
- 🚀 **提示词优化** - 使用 Gemini 3.1 Flash-Lite 自动丰富提示词
- ⚙️ **可自定义默认值** - 配置默认模型和输出目录
- 📝 **模型别名** - 使用友好名称替代技术 ID

## 🧰 支持的模型

### 多模态大语言模型
| 友好名称 | 模型 ID |
|:-------- |:------- |
| `Gemini 3.1 Flash-Lite` | `gemini-3.1-flash-lite` |
| `Gemini 3.5 Flash` | `gemini-3.5-flash` |
| `Gemini 3 Pro` | `gemini-3.0-pro-preview-001` |

### 图像生成
| 友好名称 | 模型 ID |
|:-------- |:------- |
| `Gemini 3.1 Flash Image` | `gemini-3.1-flash-image` |
| `Imagen 4 Ultra` | `imagen-4.0-ultra-generate-001` |
| `Imagen 4` | `imagen-4.0-generate-001` |

### 视频生成
| 友好名称 | 模型 ID |
|:-------- |:------- |
| `Veo 3.1 Fast` | `veo-3.1-fast-generate-001` |
| `Veo 3.1` | `veo-3.1-generate-preview` |
| `Veo 3.1 Lite` | `veo-3.1-lite-generate-preview` |

## 🚀 快速开始

### 前置要求
- Python 3.8+
- 启用了 Vertex AI 的 Google Cloud 账号
- 配置好的 Google Cloud 凭证

### Hermes 安装

1. 克隆或复制此技能到你的 Hermes 技能目录：
   ```bash
   cd ~/.hermes/skills/
   git clone https://github.com/Slvyi/google-multimodal-agent.git
   ```

2. 安装依赖：
   ```bash
   pip install google-generativeai
   ```

3. 初始化配置：
   ```bash
   cd ~/.hermes/skills/google-multimodal-agent
   python scripts/multimodal_tool.py init \
     --output_dir ~/workspace/outputs \
     --image_model "Gemini 3.1 Flash Image" \
     --multimodal_model "Gemini 3.1 Flash-Lite" \
     --video_model "Veo 3.1 Fast"
   ```

## 💡 使用方法

### 生成图像
```bash
python scripts/multimodal_tool.py image-gen --prompt "夕阳下的宁静日式花园" --optimize
```

### 生成视频
```bash
python scripts/multimodal_tool.py video-gen --prompt "海浪拍打岩石" --duration 8 --optimize
```

### 分析图像
```bash
python scripts/multimodal_tool.py image-query --file ~/workspace/image.png --prompt "详细描述这张图片"
```

### 指定不同的模型
```bash
python scripts/multimodal_tool.py image-gen --prompt "超写实人像" --model "Imagen 4 Ultra" --optimize
```

## 📁 项目结构

```
google-multimodal-agent/
├── README.md           # 英文 README
├── README_CN.md        # 中文 README（本文件）
├── SKILL.md            # Hermes 技能定义（英文）
├── SKILL_ZH.md         # Hermes 技能定义（中文）
├── config.json         # 配置文件（不在仓库中）
├── .gitignore          # Git 忽略规则
├── scripts/
│   └── multimodal_tool.py  # 主脚本
├── assets/             # 技能资源
├── references/         # 参考文档
└── tests/              # 测试文件
```

## ⚙️ 配置说明

`config.json` 文件存储你的个人设置：

```json
{
    "output_dir": "/home/ubuntu/workspace/outputs",
    "default_image_model": "Gemini 3.1 Flash Image",
    "default_video_model": "Veo 3.1 Fast",
    "default_multimodal_model": "Gemini 3.1 Flash-Lite"
}
```

## 🤖 Hermes 集成

此技能专为 Hermes Agent 设计。安装后，Hermes 会自动：
- 从 `SKILL.md` 加载技能定义
- 识别图像/视频生成请求
- 应用提示词优化最佳实践
- 遵循用户偏好的模型选择顺序

## 📄 许可证

MIT 许可证 - 可自由使用和修改！

## 🤝 贡献

欢迎贡献！随时可以提交 issue 或 pull request。
