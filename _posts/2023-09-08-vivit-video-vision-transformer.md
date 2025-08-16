---
layout: single
title: "ViViT: A Video Vision Transformer \ub9ac\ubdf0"
date: 2023-09-08 19:09:00 +0900
categories: [paper review]
tags: [transformer, video, action recognition]
toc: true
---

## Summary

ViViT proposes a pure Transformer-based architecture for video classification. The model extracts tokens from spatio-temporal patches of a video and processes them with standard Transformer encoders. To reduce computational cost, several factorised variants decompose the attention into separate spatial and temporal stages, enabling efficient training and inference. ViViT achieves state-of-the-art accuracy on benchmarks such as Kinetics-400, Kinetics-600 and Epic-Kitchens【436434647704655†L125-L137】.

## Key points
- **Patch embeddings**: Frames are divided into 2D patches; sequences of patches over time are treated as tokens for a Transformer【436434647704655†L125-L137】.
- **Factorised attention variants**: The authors propose "factorised encoder" and "factorised self-attention" to separately model spatial and temporal dependencies, significantly reducing memory requirements【436434647704655†L125-L137】.
- **Performance**: ViViT surpasses convolutional baselines on several video classification datasets and scales well to longer clips【436434647704655†L125-L137】.

## Personal notes

ViViT is notable for being among the first to apply Transformers directly to videos. The factorisation techniques highlight the importance of balancing modelling capacity and efficiency.
