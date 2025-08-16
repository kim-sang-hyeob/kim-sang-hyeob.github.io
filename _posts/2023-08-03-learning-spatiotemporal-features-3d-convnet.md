---
layout: single
title: "Learning Spatiotemporal Features with 3D ConvNets"
date: 2023-08-03 21:04:00 +0900
categories: [paper review]
tags: [3d convolution, action recognition, video]
toc: true
---

## Summary

This paper shows that 3D convolutional neural networks can learn spatiotemporal features directly from video volumes and outperform models built with 2D convolutions. By extending convolution kernels to 3D (e.g., 3×3×3), the network jointly captures spatial and temporal dimensions【196262698603811†L25-L35】. The authors evaluate network depth and kernel size and conclude that moderately deep networks with 3×3×3 kernels and homogeneous structures achieve the best performance on action recognition benchmarks【196262698603811†L37-L50】.

## Key points
- **3D convolutions**: Extend standard 2D convolutions to operate on volumes of consecutive frames, capturing motion information natively【196262698603811†L25-L35】.
- **Architecture depth**: Experiments show that deeper 3D ConvNets (up to 6–7 layers) improve performance, but beyond a point there are diminishing returns【196262698603811†L37-L50】.
- **Kernel size**: A 3×3×3 kernel provides a good trade-off between capturing motion and computational cost【196262698603811†L37-L50】.
- **Dataset evaluation**: The model is validated on action recognition datasets and demonstrates significant gains over 2D CNNs.

## Personal notes

3D ConvNets elegantly incorporate temporal information into convolution operations. It’s interesting that such a straightforward extension of 2D filters can achieve competitive results when combined with careful depth and kernel size selection.
