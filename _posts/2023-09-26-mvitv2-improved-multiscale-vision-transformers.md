---
layout: single
title: "MViTv2: Improved Multiscale Vision Transformers for Classification and Detection"
date: 2023-09-26 18:27:00 +0900
categories: [paper review]
tags: [transformer, video, multiscale]
toc: true
---

## Summary

MViTv2 is a unified architecture for image and video recognition that improves upon the original Multiscale Vision Transformer (MViT). Key innovations include decomposed relative positional embeddings to better encode spatiotemporal relationships and residual pooling connections for efficient feature aggregation. MViTv2 achieves state-of-the-art results across tasks such as ImageNet classification and COCO object detection, with 88.8% top-1 accuracy on ImageNet-1K and 58.7 box AP on COCO【944130963508823†L214-L224】.

## Key points
- **Unified model**: The same backbone can be used for image and video classification as well as object detection【944130963508823†L214-L224】.
- **Decomposed relative positional encoding**: Enhances the model’s ability to capture spatial and temporal relationships across scales【944130963508823†L214-L224】.
- **Residual pooling connections**: Introduce shortcuts between scales to improve gradient flow and feature reuse【944130963508823†L214-L224】.
- **Performance**: Surpasses MViT and other baselines on image and video recognition benchmarks【944130963508823†L214-L224】.

## Personal notes

MViTv2 demonstrates how incremental architectural refinements can yield substantial gains. Its unified design simplifies deploying the same model across tasks.
