---
layout: single
title: "[paper review] Meshed-Memory Transformer"
date: 2024-12-24 19:48:00 +0900
categories: [paper review]
tags: [transformer, image captioning, meshed memory transformer]
toc: true
---

이 리뷰에서는 2020 CVPR에서 발행된 Meshed‑Memory Transformer(M2) 노동을 간단히 정리한다.

## 요약
- 기존 Transformer 기반 이미지 캐프닝 모델은 이미지 속 객체들의 관계를 제대로 표현하지 못한다. M2 모델은 이미지 영역들의 관계를 여러 수준으로 나타낼 수 있기 위해 **멜신드 메모리(Meshed Memory)** 구조를 도출한다【114943194098861†L492-L503】.
- 인코더는 여러 레벨의 특징을 추출하고, 각 레벨을 연결하는 **persistent memory vector**를 사용하여 이미지 영역 사이의 전국 관계를 모니토링한다【114943194098861†L492-L503】.
- 디코더는 메모리와 인코더의 모든 레벨에 **완 열 연결된 멜신 형태의 아템션**을 통해 접근하며, gating mechanism을 이용하여 각 레벨의 중요도를 동적으로 조절한다. 이를 통해 장면 이호 와 문장 생성 사이의 상협 작업이 강화된다【114943194098861†L492-L503】.
- 이러한 설계를 통해 MS‑COCO, Flickr30K 등 이미지 캐프닝 벌치버크에서 SOTA 성능을 달성하여하였다.

## 메모
- M2 모델의 태요현은 여러 수준의 실사 특쳝과 persistent memory를 결합하여 지역적 및 그룹 관계를 모두 공합한다.
- 노동에서는 memory vector의 크기, 레벨 수 등 하이퍼파라미터에 대한 실험도 진행했다.
- 실제 구현에서는 PyTorch의 Transformer 모듈을 기반으로 하며, positional encoding 대신 learnable parameters를 사용한다.
