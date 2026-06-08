# Google 多模态智能体 Skill (混合架构版)

一套专为 **Gemini 企业级智能体平台** (Vertex AI) 打造的专业工具集，用于生成并分析图像和视频。支持高级编排与快速执行。

## 核心特性
- **混合工作流**: 同时支持 **原子化控制**（针对复杂任务的分步操作）和 **快捷执行**（带 `--optimize` 的一键生成）。
- **Agent 优化版 LLM**: 采用 `Gemini 3.5 Flash`，具备卓越的推理与媒体分析能力。
- **生产级生成**: 使用 `Gemini 3.1` 和 `Veo 3.1` 系列生成高保真素材。
- **媒体查询**: 深度理解图像和视频内容。
- **赠金额度兼容**: 完全支持抵扣 **Google Cloud 赠金额度**。

## 支持的模型 (官方平台 v2026.06)

| 类别 | 模型别名 | 适用场景 |
|:--- |:--- |:--- |
| **编排 / 查询** | `Gemini 3.5 Flash` | 推理、Agent 任务、媒体理解。 |
| **图片生成** | `Gemini 3.1 Flash Image` | 快速、高质量的生产级素材。 |
| **视频生成** | `Veo 3.1 Fast` | 低延迟、高保真视频。 |

## 安装

### 准备工作
- Python 3.9+
- 已启用 Vertex AI API 的 Google Cloud 项目。
- 已配置 [Google Cloud ADC](https://cloud.google.com/docs/authentication/provide-credentials-adc) 凭据。

### 步骤
1. **安装依赖**:
   ```bash
   pip install google-genai
   ```
2. **初始化配置**:
   ```bash
   python scripts/multimodal_tool.py init \
     --output_dir ~/workspace/outputs \
     --multimodal_model "Gemini 3.5 Flash"
   ```

## 使用模式

### 1. 快捷模式 (最快)
一键式提示词增强并生成。
```bash
python scripts/multimodal_tool.py image-gen --prompt "赛博朋克城市" --optimize
```

### 2. 原子模式 (精准控制)
专为调度器 Agent（如 OpenClaw）设计的解耦步骤。
```bash
# 第一步：优化提示词
python scripts/multimodal_tool.py optimize-prompt --prompt "赛博朋克城市" --task_type "image"

# 第二步：使用优化后的提示词进行生成
python scripts/multimodal_tool.py image-gen --prompt "从第一步获取的长描述..."
```

### 3. 媒体理解
分析图像或视频内容。
```bash
python scripts/multimodal_tool.py video-query --file ./input.mp4 --prompt "第5秒发生了什么？"
```

## 许可证
MIT
