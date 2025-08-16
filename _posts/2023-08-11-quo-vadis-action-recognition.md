---
layout: single
title: "Quo Vadis, Action Recognition? A New Model and the Kinetics Dataset (2018)"
date: 2023-08-11 22:38:00 +0900
categories: [paper review]
tags: [action recognition, kinetics, video, dataset]
toc: true
---

## Summary

This paper introduces the **Kinetics** dataset, a large-scale collection of short video clips (10 s each) from YouTube covering 400 human action classes with approximately 400 video examples per class. Prior video datasets contained only a few action classes and small numbers of clips, often captured in controlled settings, which limited the ability of deep learning models to generalize. Kinetics curates clips with diverse backgrounds and actions and provides high-quality annotations. The authors show that models trained on this dataset outperform those trained on previous datasets, highlighting the importance of scale and diversity in video action recognition research.

The paper also surveys contemporary architectures for action recognition. Key approaches include:

- **ConvNet + LSTM**: use convolutional neural networks on individual frames followed by recurrent layers to model temporal dynamics.
- **3D Convolutional Networks**: extend 2D convolutions to the spatiotemporal domain to jointly capture spatial and temporal information.
- **Two-Stream Networks**: employ separate CNNs for RGB frames and optical flow to capture appearance and motion cues separately and fuse their predictions.

## Personal notes

I appreciated how the paper emphasizes the need for a large, diverse dataset to train modern deep models and how Kinetics helps bridge the gap between research and real-world applications. The overview of different action recognition architectures provides context for subsequent papers on 3D convolutional and non-local networks. In future work, I plan to compare models trained on Kinetics to those trained on previous datasets and explore combinations of conv-based and transformer-based architectures.
