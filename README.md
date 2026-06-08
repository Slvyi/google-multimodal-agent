# Google Multimodal Agent Skill (Hybrid Architecture)

A professional suite of tools for the **Gemini Enterprise Agent Platform** (Vertex AI) to generate and analyze images and videos. Designed for both high-level orchestration and fast execution.

## Key Features
- **Hybrid Workflow**: Supports both **Atomic Control** (discrete steps for complex tasks) and **Shortcut Execution** (one-step generation with `--optimize`).
- **Agent-Optimized LLM**: Powered by `Gemini 3.5 Flash` for superior reasoning and media analysis.
- **Production-Ready Generation**: High-fidelity assets with `Gemini 3.1` and `Veo 3.1` series.
- **Media Query**: Deep multimodal understanding for both images and videos.
- **Promotional Credit Compatible**: Fully compatible with **Google Cloud Promotional Credits**.

## Supported Models (Official Platform v2026.06)

| Category | Model Alias | Best For |
|:--- |:--- |:--- |
| **Orchestration/Query** | `Gemini 3.5 Flash` | Reasoning, Agentic Tasks, Media Understanding. |
| **Image Generation** | `Gemini 3.1 Flash Image` | Fast, high-quality production assets. |
| **Video Generation** | `Veo 3.1 Fast` | Low-latency, high-fidelity video. |

## Installation

### Prerequisites
- Python 3.9+
- Google Cloud Project with Vertex AI API enabled.
- [Google Cloud ADC](https://cloud.google.com/docs/authentication/provide-credentials-adc) configured.

### Setup
1. **Install dependencies**:
   ```bash
   pip install google-genai
   ```
2. **Initialize configuration**:
   ```bash
   python scripts/multimodal_tool.py init \
     --output_dir ~/workspace/outputs \
     --multimodal_model "Gemini 3.5 Flash"
   ```

## Usage Patterns

### 1. Shortcut Mode (Fastest)
One-step prompt enrichment and generation.
```bash
python scripts/multimodal_tool.py image-gen --prompt "Cyberpunk city" --optimize
```

### 2. Atomic Mode (Precise Control)
Decoupled steps for Orchestrator Agents (e.g., OpenClaw).
```bash
# Step 1: Optimize prompt
python scripts/multimodal_tool.py optimize-prompt --prompt "Cyberpunk city" --task_type "image"

# Step 2: Generate with optimized prompt
python scripts/multimodal_tool.py image-gen --prompt "The resulting long prompt from step 1..."
```

### 3. Media Understanding
Analyze images or videos.
```bash
python scripts/multimodal_tool.py video-query --file ./input.mp4 --prompt "What happens at 0:05?"
```

## License
MIT
