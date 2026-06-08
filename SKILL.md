---
name: google-multimodal-agent
description: Use when the user requests generating, analyzing, or editing images and videos using Google's generative AI models (Imagen, Veo, Gemini).
---

# Google Multimodal Agent (Hybrid Agentic v2026.06)

## Overview
This skill is a versatile toolset for **AI Orchestrators**. It supports both **Atomic Control** (discrete steps) and **Shortcut Execution** (all-in-one commands). All operations are billed against **Google Cloud Promotional Credits**.

## Orchestrator Workflow Rules
The orchestrating Agent can choose between two interaction patterns:

### Pattern A: Atomic Control (Recommended for Complex Tasks)
1. **Brain**: Call `optimize-prompt` to get an expert description.
2. **Review**: You (the Agent) can review/edit the prompt based on context.
3. **Execution**: Call `image-gen` or `video-gen` with the finalized prompt.

### Pattern B: Shortcut Execution (Recommended for Simple Tasks)
- Directly call `image-gen` or `video-gen` with the `--optimize` flag. This will automatically use Gemini 3.5 Flash to enrich the prompt before generating the media in a single step.

## Default Config
- **LLM/Orchestration**: `Gemini 3.5 Flash` (Default for prompt optimization and media query)
- **Image Generation**: `Gemini 3.1 Flash Image`
- **Video Generation**: `Veo 3.1 Fast`

## CLI Commands

### 1. Generation (The Hands)
Strictly executes generation. Use `--optimize` for one-step enrichment.
- `python scripts/multimodal_tool.py image-gen --prompt "..." [--optimize] [--aspect_ratio 16:9]`
- `python scripts/multimodal_tool.py video-gen --prompt "..." [--optimize] [--duration 6]`

### 2. Prompt Engineering (The Brain)
Enriches a simple prompt without executing generation.
- `python scripts/multimodal_tool.py optimize-prompt --prompt "..." --task_type "image|video"`

### 3. Media Understanding (The Eyes)
Analyzes content and answers questions.
- `python scripts/multimodal_tool.py image-query --file <path> --prompt "..."`
- `python scripts/multimodal_tool.py video-query --file <path> --prompt "..."`

## Initialization
```bash
python scripts/multimodal_tool.py init --multimodal_model "Gemini 3.5 Flash" --image_model "Gemini 3.1 Flash Image" --video_model "Veo 3.1 Fast"
```
