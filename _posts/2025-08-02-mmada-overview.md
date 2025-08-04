---
layout: single
title: "MMaDA: Multimodal Large Diffusion Language Models"
date: 2025-08-02
categories: ["research"]
tags: ["MMaDA", "multimodal", "diffusion", "language model"]
toc: true
author_profile: true
---




MMaDA (Multimodal Large Diffusion Language Models) is a unified multimodal model designed to handle text and images within a single diffusion-based architecture. Unlike earlier systems that combine an autoregressive language model with a separate diffusion model for images, MMaDA shares one model across modalities to provide a consistent representation space.

## Unified diffusion architecture

In MMaDA, text is tokenized into discrete tokens while images are mapped to VQ tokens, and these sequences are concatenated. A diffusion model operates on the combined sequence, and a unified cross-entropy mask-recover objective allows the model to learn from language and visual data together.

## Three-stage training pipeline

1. **Stage 1 – Pretraining**: The model is pretrained on diverse tasks such as language modeling, multimodal question answering, captioning and text-to-image generation to build a broad base of knowledge.
2. **Stage 2 – Mixed Long Chain-of-Thought Fine Tuning**: To strengthen reasoning, the model is fine-tuned on long chain-of-thought examples that include math problems, multimodal reasoning and text-to-image generation.
3. **Stage 3 – Unified Reinforcement Learning (UniGRPO)**: A unified policy gradient algorithm adapts reinforcement learning to the diffusion model, optimising rewards for text reasoning, multimodal reasoning and image generation simultaneously.

## Results and significance

Experiments show that MMaDA outperforms existing models on multimodal understanding tasks, image generation benchmarks and pure language benchmarks. Performance improves consistently when moving from Stage 1 to Stage 2 and Stage 3. By extending diffusion to the language domain and unifying training across modalities, MMaDA demonstrates a promising direction for future multimodal AI systems.


<img width="1080" height="7560" alt="MMaDAㅡ" src="https://github.com/user-attachments/assets/ec536ab8-a048-43e7-b71c-7ae6bb86d4a5" />
