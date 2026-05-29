---
name: google-multimodal-agent
description: 当用户请求使用 Google 生成式 AI 模型（Imagen、Veo、Gemini）生成、分析或编辑图像和视频时使用。
---

# Google 多模态 Agent (v2026.05)

## 概述
本技能提供了一个辅助脚本 (`scripts/multimodal_tool.py`)，用于与 **Gemini Enterprise Agent Platform** 进行交互。它支持最新的图像生成、视频生成以及多模态理解模型。

## 当前默认模型设置
- **多模态理解/推理**: `Gemini 3.1 Flash-Lite`
- **图像生成 (Image)**: `Gemini 3.1 Flash Image` (Nano Banana 2)
- **视频生成 (Video)**: `Veo 3.1 Fast`

## 初始化
设置存储在技能目录中。如需重新初始化或更改默认值：
```bash
python scripts/multimodal_tool.py init --output_dir ~/workspace/outputs --image_model "Gemini 3.1 Flash Image" --multimodal_model "Gemini 3.1 Flash-Lite" --video_model "Veo 3.1 Fast"
```

## 支持的模型别名
请使用以下友好名称以获得最佳映射效果：

| 类别 | 友好名称 (Alias) | 模型 ID |
| :--- | :--- | :--- |
| **多模态 LLM** | `Gemini 3.1 Flash-Lite` | `gemini-3.1-flash-lite` |
| | `Gemini 3.5 Flash` | `gemini-3.5-flash` |
| | `Gemini 3 Pro` | `gemini-3.0-pro-preview-001` |
| **图像生成** | `Gemini 3.1 Flash Image` | `gemini-3.1-flash-image` |
| | `Imagen 4 Ultra` | `imagen-4.0-ultra-generate-001` |
| | `Imagen 4` | `imagen-4.0-generate-001` |
| **视频生成** | `Veo 3.1 Fast` | `veo-3.1-fast-generate-001` |
| | `Veo 3.1` | `veo-3.1-generate-preview` |
| | `Veo 3.1 Lite` | `veo-3.1-lite-generate-preview` |

## 提示词优化 (双轨制)
为了确保最高质量的视觉输出，请遵循以下流程：

### 1. 交互式轨道 (Agent 驱动)
如果用户的提示词过于简短（如“一只猫”），**不要**立即运行工具。
- 询问用户细节（风格、光影、情绪）。
- 提供一个丰富后的提示词版本供用户确认。

### 2. 自动化轨道 (脚本驱动)
在执行命令时始终带上 `--optimize` 标志。这将调用默认的 `Gemini 3.1 Flash-Lite` 将原始提示词扩充为专业级描述。

## 常用命令示例

### 图像生成
```bash
python scripts/multimodal_tool.py image-gen --prompt "赛博朋克风格的猫" --optimize
```
*（默认使用 Gemini 3.1 Flash Image）*

### 视频生成
```bash
python scripts/multimodal_tool.py video-gen --prompt "机器人在雨中漫步" --duration 8 --optimize
```
*（默认使用 Veo 3.1 Fast）*

### 图像/视频理解
```bash
python scripts/multimodal_tool.py image-query --file <路径> --prompt "分析这张图里的内容"
```
*（默认使用 Gemini 3.1 Flash-Lite）*
