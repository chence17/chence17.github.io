---
permalink: /
title: ""
excerpt: ""
lang: en
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% assign url = "https://chence17.github.io/assets/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I am currently a Ph.D. student at the [School of Mathematics and Statistics, University of Melbourne](https://www.unimelb.edu.au/), supervised by [Prof. Mingming Gong (宫明明)](https://mingming-gong.github.io/). Meanwhile, I work as an AI Research Intern at [HeyGen](https://www.heygen.com), Singapore, mentored by [Mr. Yi Ren (任意)](https://rayeren.github.io/) and [Mr. Zhibin Hong (洪智滨)](https://openreview.net/profile?id=~Zhibin_Hong1). Before that, I received my M.Phil. degree from [The Chinese University of Hong Kong, Shenzhen (CUHK-SZ)](https://www.cuhk.edu.cn/) in 2023, supervised by [Prof. Xiaoguang Han (韩晓光)](https://scholar.google.com/citations?user=z-rqsR4AAAAJ&hl=en), and my B.Eng. degree from [Tsinghua University](https://www.tsinghua.edu.cn/) in 2021, supervised by [Prof. Yipeng Li (李一鹏)](https://www.au.tsinghua.edu.cn/info/1080/3167.htm).

My research interests include generative models, visual language models and multimodal language models. I have published 10+ papers at top international AI conferences such as CVPR, ECCV, and ICLR, with total <a href='https://scholar.google.com/citations?user=tX8IWwMAAAAJ'>google scholar citations <strong><span id='total_cit'>700+</span></strong></a> (<a href='https://scholar.google.com/citations?user=tX8IWwMAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&cacheSeconds=3600&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>).

If you are interested in any form of **academic cooperation**, please feel free to email me at [antonio.chan.cc@outlook.com](mailto:antonio.chan.cc@outlook.com).


# 🔥 News
- *2026.06*: &nbsp;🎉 One paper is accepted by ECCV 2026.
- *2026.02*: &nbsp;🎉 One paper is accepted by CVPR 2026.
- *2026.01*: &nbsp;🎉 One paper is accepted by ICLR 2026.
- *2025.06*: &nbsp;🎉 I join HeyGen as an AI research intern in Singapore!
- *2024.07*: &nbsp;🎉 One paper is accepted by ECCV 2024.
- *2023.02*: &nbsp;🎉 One paper is accepted by CVPR 2023.


# 📝 Publications 

> \* indicates equal contribution.

## Video Generation & Understanding

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ECCV 2026</div><img src='/images/teaser/2026TransVLM.png' alt="TransVLM" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[TransVLM: A Vision-Language Framework and Benchmark for Detecting Any Shot Transitions](https://arxiv.org/abs/2604.27975) \\
**_<u>Ce Chen</u>_**, Yi Ren, Yuanming Li, Viktor Goriachko, Zhenhui Ye, Zujin Guo, Zhibin Hong, Mingming Gong

[**Project**](https://chence17.github.io/TransVLM/) \| [**arXiv**](https://arxiv.org/abs/2604.27975) \| [**GitHub**](https://github.com/chence17/TransVLM) \| [**Blog**](https://www.heygen.com/research/transvlm)
- Proposes the Shot Transition Detection (STD) task and TransVLM, a VLM framework that injects optical flow as motion prior for detecting continuous temporal segments of video transitions.
- Deployed to production at HeyGen.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">arXiv 2026</div><img src='/images/teaser/2026TAVR.png' alt="TAVR" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[TAVR: Generate Your Talking Avatar from Video Reference](https://arxiv.org/abs/2604.27918) \\
Zujin Guo, Zhenhui Ye, Yi Ren, Yuanming Li, **_<u>Ce Chen</u>_**, Zhibin Hong, Chen Change Loy

[**arXiv**](https://arxiv.org/abs/2604.27918)
- A novel framework for cross-scene talking avatar generation from video references, integrating token selection and a three-stage training scheme.
- Deployed to production at HeyGen.
</div>
</div>


<div class='paper-box' style='border-bottom: none;'><div class='paper-box-image'><div><div class="badge">arXiv 2026</div><img src='/images/teaser/2026AvatarV.png' alt="Avatar V" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Avatar V: Scaling Video-Reference Avatar Video Generation](https://arxiv.org/abs/2606.13872) \\
Benjamin Liang, **_<u>Ce Chen</u>_**, Desmond Lin, Ivan Somov, Jiajun Zhao, Jiewei Yuan, Jingfeng Zhang, Junhao Huang, Nik Nolte, Pedram Haqiqi, Penghan Wang, Rong Yan, Rui Zhang, Sam Prokopchuk, Sivan Wang, Viktor Goriachko, Yi Ren, Yuanming Li, Yutao Chen, Zhenhui Ye, Zhibin Hong, Zilong Nie, Zujin Guo

[**arXiv**](https://arxiv.org/abs/2606.13872) \| [**Blog**](https://www.heygen.com/research/avatar-v-model)
- A production-scale framework for video-reference-conditioned avatar generation. Introduces Sparse Reference Attention for linear-complexity conditioning on long references.
- Deployed to production at HeyGen, trained across thousands of GPUs with a data engine curating 100M+ training clips.
</div>
</div>


## Image Generation & Understanding

<div class='paper-box' style='border-bottom: none;'><div class='paper-box-image'><div><div class="badge">CVPR 2026</div><img src='/images/teaser/2026Mobile-VTON.png' alt="Mobile-VTON" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Mobile-VTON: High-Fidelity On-Device Virtual Try-On](https://arxiv.org/abs/2603.00947) \\
Zhenchen Wan\*, **_<u>Ce Chen</u>_**\*, Runqi Lin, Jiaxin Huang, Tianxi Chen, Yanwu Xu, Tongliang Liu, Mingming Gong

[**Project**](https://zhenchenwan.github.io/Mobile-VTON/) \| [**arXiv**](https://arxiv.org/abs/2603.00947) \| [**GitHub**](https://github.com/tmllab/2026_CVPR_Mobile-VTON) \| [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-blue?label=Demo)](https://huggingface.co/FlashStight/Mobile-VTON)
- A privacy-preserving virtual try-on framework enabling fully offline execution on commodity mobile devices. Introduces a modular TGT architecture with Feature-Guided Adversarial Distillation.
- Matches or outperforms server-based baselines at 1024×768 resolution on VITON-HD and DressCode.
</div>
</div>


## 3D/4D Generation & Understanding

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2026</div><img src='/images/teaser/2026Condition.png' alt="Condition Matters" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Condition Matters in Full-Head 3D GANs](https://arxiv.org/abs/2602.07198) \\
Heyuan Li, Huimin Zhang, Yuda Qiu, Zhengwentai Sun, Keru Zheng, Lingteng Qiu, Peihao Li, Qi Zuo, **_<u>Ce Chen</u>_**, Yujian Zheng, Yuming Gu, Zilong Dong, Xiaoguang Han

[**Project**](https://lhyfst.github.io/balancehead) \| [**arXiv**](https://arxiv.org/abs/2602.07198) \| [**GitHub**](https://github.com/lhyfst/BalanceHead)
- Proposes view-invariant semantic feature conditioning to decouple 3D head generation from viewing direction, achieving higher fidelity and diversity in full-head synthesis.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">arXiv 2024</div><img src='/images/teaser/2024CT4D.png' alt="CT4D" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[CT4D: Consistent Text-to-4D Generation with Animatable Meshes](https://arxiv.org/abs/2408.08342) \\
**_<u>Ce Chen</u>_**, Shaoli Huang, Xuelin Chen, Guangyi Chen, Xiaoguang Han, Kun Zhang, Mingming Gong

[**arXiv**](https://arxiv.org/abs/2408.08342)
- Presents a novel text-to-4D framework operating on animatable meshes. Introduces the Generate-Refine-Animate (GRA) algorithm for text-aligned mesh generation and uniform driving functions for surface continuity.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ECCV 2024 <span style="color:red">(Oral, Top 1.5%)</span></div><img src='/images/teaser/2024SphereHead.png' alt="SphereHead" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[SphereHead: Stable 3D Full-head Synthesis with Spherical Tri-plane Representation](https://arxiv.org/abs/2404.05680) \\
Heyuan Li, **_<u>Ce Chen</u>_**, Tianhao Shi, Yuda Qiu, Sizhe An, Guanying Chen, Xiaoguang Han

[**Project**](https://lhyfst.github.io/spherehead/) \| [**arXiv**](https://arxiv.org/abs/2404.05680) \| [**GitHub**](https://github.com/lhyfst/SphereHead)
- Proposes a spherical tri-plane representation in the spherical coordinate system that mitigates "mirroring" artifacts in full-head 3D GAN synthesis, along with a view-image consistency loss.
</div>
</div>


<div class='paper-box' style='border-bottom: none;'><div class='paper-box-image'><div><div class="badge">CVPR 2023</div><img src='/images/teaser/2023SCoDA.png' alt="SCoDA" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[SCoDA: Domain Adaptive Shape Completion for Real Scans](https://arxiv.org/abs/2304.10179) \\
Yushuang Wu, Zizheng Yan, **_<u>Ce Chen</u>_**, Lai Wei, Xiao Li, Guanbin Li, Yihao Li, Shuguang Cui, Xiaoguang Han

[**Project**](https://yushuang-wu.github.io/SCoDA) \| [**arXiv**](https://arxiv.org/abs/2304.10179) \| [**GitHub**](https://github.com/yushuang-wu/SCoDA)
- Proposes the novel SCoDA task for domain adaptive shape completion on real scans, along with the ScanSalon dataset. Introduces cross-domain feature fusion and volume-consistent self-training.
</div>
</div>


## Medical Image Analysis

<div class='paper-box' style='border-bottom: none;'><div class='paper-box-image'><div><div class="badge">arXiv 2023</div><img src='/images/teaser/2023DenseMP.png' alt="DenseMP" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[DenseMP: Unsupervised Dense Pre-training for Few-shot Medical Image Segmentation](https://arxiv.org/abs/2307.09604) \\
Zhaoxin Fan, Puquan Pan, Zeren Zhang, **_<u>Ce Chen</u>_**, Tianyang Wang, Siyang Zheng, Min Xu

[**arXiv**](https://arxiv.org/abs/2307.09604)
- Introduces a two-stage unsupervised dense pre-training pipeline with segmentation-aware dense contrastive learning and superpixel guided pre-training, achieving state-of-the-art few-shot segmentation on Abd-CT and Abd-MRI.
</div>
</div>


## Super Resolution

<div class='paper-box' style='border-bottom: none;'><div class='paper-box-image'><div><div class="badge">CVPR 2020</div><img src='/images/teaser/2020SPSR.png' alt="SPSR" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Structure-Preserving Super Resolution with Gradient Guidance](https://arxiv.org/abs/2003.13081) \\
Cheng Ma, Yongming Rao, Yean Cheng, **_<u>Ce Chen</u>_**, Jiwen Lu, Jie Zhou

[**arXiv**](https://arxiv.org/abs/2003.13081) \| [**GitHub**](https://github.com/Maclory/SPSR)
- Proposes a structure-preserving super resolution method that exploits gradient maps to guide image recovery. Introduces a gradient branch and gradient loss for second-order structural constraints.
- Cited 380+ times.
</div>
</div>


# 🎖 Honors and Awards
- *2026.03* &nbsp;🎓&nbsp; Melbourne Research Scholarship
- *2026.03* &nbsp;🎓&nbsp; Rowden White Scholarship


# 📖 Educations

<div class='education-item'>
<div class='edu-logo'><img src='/images/unimelb-logo.png' alt='UniMelb'></div>
<div class='edu-text' markdown="1">
🎓&nbsp; **Ph.D.** \\
📚&nbsp; School of Mathematics and Statistics, Faculty of Science \\
🏫&nbsp; [University of Melbourne (UniMelb)](https://www.unimelb.edu.au/) \\
📅&nbsp; Mar.2026 – Now \\
👨‍🏫&nbsp; Supervisor: [Prof. Mingming Gong (宫明明)](https://mingming-gong.github.io/)
</div>
</div>

<div class='education-item'>
<div class='edu-logo'><img src='/images/cuhksz-logo.png' alt='CUHK-SZ'></div>
<div class='edu-text' markdown="1">
🎓&nbsp; **M.Phil.** \\
📚&nbsp; Computer & Information Engineering, School of Science and Engineering \\
🏫&nbsp; [The Chinese University of Hong Kong, Shenzhen (CUHK-SZ)](https://www.cuhk.edu.cn/) \\
📅&nbsp; Aug.2021 – Jul.2023 \\
👨‍🏫&nbsp; Supervisor: [Prof. Xiaoguang Han (韩晓光)](https://scholar.google.com/citations?user=z-rqsR4AAAAJ&hl=en) \| GPA: 3.98 / 4.0 (Rank 1/32)
</div>
</div>

<div class='education-item'>
<div class='edu-logo'><img src='/images/thu-logo.png' alt='THU'></div>
<div class='edu-text' markdown="1">
🎓&nbsp; **B.Eng.** \\
📚&nbsp; Department of Automation \\
🏫&nbsp; [Tsinghua University (THU)](https://www.tsinghua.edu.cn/) \\
📅&nbsp; Aug.2017 – Jul.2021 \\
👨‍🏫&nbsp; Supervisor: [Prof. Yipeng Li (李一鹏)](https://www.au.tsinghua.edu.cn/info/1080/3167.htm) \| GPA: 3.44 / 4.0
</div>
</div>


# 💻 Internships

<div class='internship-item'>
<div class='intern-logo'><img src='/images/heygen-logo.png' alt='HeyGen'></div>
<div class='intern-text' markdown="1">
💼&nbsp; **AI Research Intern** \\
🏢&nbsp; [HeyGen](https://www.heygen.com) \\
📍&nbsp; Singapore \\
📅&nbsp; Jun.2025 – Now \\
📝&nbsp; Mentor: [Mr. Yi Ren (任意)](https://rayeren.github.io/). Research on accurate and detailed human video generation via diffusion models.
</div>
</div>

<div class='internship-item'>
<div class='intern-logo'><img src='/images/mbzuai-logo.png' alt='MBZUAI'></div>
<div class='intern-text' markdown="1">
💼&nbsp; **Research Assistant** \\
🏢&nbsp; Machine Learning Department, [Mohamed bin Zayed University of Artificial Intelligence (MBZUAI)](https://mbzuai.ac.ae/) \\
📍&nbsp; Abu Dhabi, UAE \\
📅&nbsp; Feb.2024 – Jun.2025 \\
📝&nbsp; Supervisor: [Prof. Mingming Gong (宫明明)](https://mingming-gong.github.io/) & [Prof. Kun Zhang (张坤)](https://www.andrew.cmu.edu/user/kunz1/). Research on text-to-4D generation, on-device text-to-image, and virtual try-on.
</div>
</div>

<div class='internship-item'>
<div class='intern-logo'><img src='/images/cuhksz-logo.png' alt='CUHK-SZ'></div>
<div class='intern-text' markdown="1">
💼&nbsp; **Research Assistant** \\
🏢&nbsp; School of Science and Engineering, [The Chinese University of Hong Kong, Shenzhen (CUHK-SZ)](https://www.cuhk.edu.cn/) \\
📍&nbsp; Shenzhen, Guangdong, China \\
📅&nbsp; Aug.2023 – Jan.2024 \\
📝&nbsp; Supervisor: [Prof. Xiaoguang Han (韩晓光)](https://scholar.google.com/citations?user=z-rqsR4AAAAJ&hl=en). Research on photorealistic 3D human head generation with spherical tri-plane representation.
</div>
</div>

<div class='internship-item'>
<div class='intern-logo'><img src='/images/tencent-logo.png' alt='Tencent'></div>
<div class='intern-text' markdown="1">
💼&nbsp; **Computer Vision Algorithm Engineer Intern** \\
🏢&nbsp; WeChat Group, [Tencent](https://www.tencent.com/) \\
📍&nbsp; Beijing, China \\
📅&nbsp; Jun.2021 – Aug.2021 \\
📝&nbsp; Developed table recognition system converting camera-captured or PDF table images to structured HTML, deployed as part of the company's e-office system.
</div>
</div>

<div class='internship-item'>
<div class='intern-logo'><img src='/images/bytedance-logo.png' alt='ByteDance'></div>
<div class='intern-text' markdown="1">
💼&nbsp; **Computer Vision Algorithm Engineer Intern** \\
🏢&nbsp; AI Lab, [ByteDance](https://www.bytedance.com/) \\
📍&nbsp; Beijing, China \\
📅&nbsp; Jun.2020 – Nov.2020 \\
📝&nbsp; Developed apartment layout diagram vectorization system for structured room parsing, achieving >90% recognition accuracy with >5× efficiency improvement.
</div>
</div>


# 📋 Academic Services
- 📖&nbsp; Conference Reviewer: NeurIPS 2026, ECCV 2026, CVPR 2026, ICLR 2026, NeurIPS 2025
- 📖&nbsp; Journal Reviewer: IEEE Transactions on Multimedia, IEEE Signal Processing Letters, IEEE Transactions on Image Processing
