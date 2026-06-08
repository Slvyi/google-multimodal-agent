---
name: google-multimodal-agent
description: 当用户请求使用 Google 的生成式 AI 模型（Imagen、Veo、Gemini）生成、分析或编辑图像和视频时使用。
---

# Google 多模态智能体 (混合 Agent 版 v2026.06)

## 概览
此 Skill 为 **AI 调度器 (Orchestrators)** 提供了一套灵活的工具集。它既支持 **原子化控制**（分步精确操作），也支持 **快捷执行**（一键式命令）。所有操作均可由 **Google Cloud 赠金额度** 抵扣。

## 调度器工作流模式
主控 Agent 可以根据场景选择以下两种模式之一：

### 模式 A：原子化控制 (推荐用于复杂任务)
1. **智囊**: 调用 `optimize-prompt` 获取专家级描述。
2. **审核**: 你（Agent）可以根据上下文审核或修改提示词。
3. **执行**: 使用最终确定的提示词调用 `image-gen` 或 `video-gen`。

### 模式 B：快捷执行 (推荐用于简单任务)
- 直接调用 `image-gen` 或 `video-gen` 并带上 `--optimize` 标志。这将自动使用 Gemini 3.5 Flash 在生成媒体之前一步到位地丰富提示词。

## 默认配置
- **LLM/编排**: `Gemini 3.5 Flash` (默认用于提示词优化和媒体查询)
- **图片生成**: `Gemini 3.1 Flash Image`
- **视频生成**: `Veo 3.1 Fast`

## CLI 命令

### 1. 媒体生成 (执行侧)
严格根据提示词执行生成。使用 `--optimize` 可实现一键增强。
- `python scripts/multimodal_tool.py image-gen --prompt "..." [--optimize] [--aspect_ratio 16:9]`
- `python scripts/multimodal_tool.py video-gen --prompt "..." [--optimize] [--duration 6]`

### 2. 提示词工程 (智囊侧)
仅扩充提示词，不执行生成。
- `python scripts/multimodal_tool.py optimize-prompt --prompt "..." --task_type "image|video"`

### 3. 媒体理解 (眼睛侧)
分析媒体内容并回答自然语言问题。
- `python scripts/multimodal_tool.py image-query --file <路径> --prompt "..."`
- `python scripts/multimodal_tool.py video-query --file <路径> --prompt "..."`

## 初始化
```bash
python scripts/multimodal_tool.py init --multimodal_model "Gemini 3.5 Flash" --image_model "Gemini 3.1 Flash Image" --video_model "Veo 3.1 Fast"
```
