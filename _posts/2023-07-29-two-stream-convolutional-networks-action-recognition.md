---
layout: single
title: "Two-stream Convolutional Networks for Action Recognition in Videos"
date: 2023-07-29 21:27:00 +0900
categories: [paper review]
tags: [two-stream, action recognition, video]
toc: true
---

## Summary

The two-stream architecture introduces separate spatial and temporal convolutional networks: one processes individual RGB frames to capture appearance, and the other processes stacks of optical flow to model motion【774602880865830†L20-L27】. Predictions from the two streams are fused late in the network to obtain action recognition scores. Multi-task training using both streams and multi-task multi-class classification improves performance【774602880865830†L42-L47】.

## Key points
- **Spatial stream**: A CNN trained on RGB frames extracts spatial appearance features【774602880865830†L20-L27】.
- **Temporal stream**: A second CNN uses stacked optical flow fields to capture motion patterns, making the network sensitive to direction and speed【774602880865830†L20-L27】.
- **Fusion**: Late fusion combines the softmax scores or feature embeddings from both streams, leveraging complementary information【774602880865830†L20-L27】.
- **Multi-task learning**: Joint training across multiple datasets or tasks helps reduce overfitting and improves generalisation【774602880865830†L42-L47】.

## Personal notes

By disentangling appearance and motion cues, the two-stream approach provides a simple yet effective baseline for video action recognition. Its modular design inspired many later works.
