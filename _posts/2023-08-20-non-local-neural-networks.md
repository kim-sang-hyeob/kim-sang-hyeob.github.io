---
layout: single
title: "Non-local Neural Networks \ub9ac\"
date: 2023-08-20 13:59:00 +0900
categories: [paper review]
tags: [non-local, video, action recognition]
toc: true
---

## Summary

Non-local Neural Networks address the limitation of convolutional and recurrent networks in capturing long-range dependencies in space-time. They introduce non-local operations, which compute responses at a position as a weighted sum of features across all positions, allowing the model to capture global context. This technique significantly improves performance in tasks such as video classification and object detection【763947938353029†L34-L70】.

## Key points
- **Motivation**: Traditional convolutional operations are local and cannot effectively model long-range dependencies across space and time【763947938353029†L34-L70】.
- **Non-local operation**: Computes output at each position as a weighted sum over features of all positions in the input feature map; weighting function depends on pairwise similarity. This enables capturing global context without stacking many layers【763947938353029†L34-L70】.
- **Efficiency**: Although non-local operations are dense, they can be approximated and integrated into existing architectures with modest computational overhead.
- **Results**: Non-local blocks yield significant performance gains over 2D and 3D convolutional baselines in video classification tasks while requiring only RGB input【763947938353029†L34-L70】.

## Personal notes

The non-local approach elegantly addresses long-range dependency modeling and can be combined with standard CNN architectures. It's impressive that such a simple idea – computing weighted sums across all positions – provides notable gains.
