---
permalink: /zh-cn/
title: ""
excerpt: ""
lang: zh-CN
layout: default_zh
author_profile: true
redirect_from: 
  - /zh/
---

{% assign url = "https://chence17.github.io/assets/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

我目前在[墨尔本大学理学院数学与统计系](https://www.unimelb.edu.au/)攻读博士学位，导师为[宫明明教授 (Prof. Mingming Gong)](https://mingming-gong.github.io/)。同时，我在新加坡 [HeyGen](https://www.heygen.com) 担任 AI 研究实习生，由[任意 (Mr. Yi Ren)](https://rayeren.github.io/) 和[洪智滨 (Mr. Zhibin Hong)](https://openreview.net/profile?id=~Zhibin_Hong1) 指导。此前，我于 2023 年在[香港中文大学（深圳）(CUHK-SZ)](https://www.cuhk.edu.cn/) 获得哲学硕士学位，导师为[韩晓光教授 (Prof. Xiaoguang Han)](https://scholar.google.com/citations?user=z-rqsR4AAAAJ&hl=en)；于 2021 年在[清华大学](https://www.tsinghua.edu.cn/) 获得工学学士学位，导师为[李一鹏教授 (Prof. Yipeng Li)](https://www.au.tsinghua.edu.cn/info/1080/3167.htm)。

我的研究方向包括生成式模型、视觉语言模型以及多模态语言模型。我已在 CVPR、ECCV、ICLR 等顶级国际 AI 会议上发表 10 余篇论文，累计<a href='https://scholar.google.com/citations?user=tX8IWwMAAAAJ'>Google Scholar 引用 <strong><span id='total_cit'>700+</span></strong></a> (<a href='https://scholar.google.com/citations?user=tX8IWwMAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&cacheSeconds=3600&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>)。

如您有意向进行任何形式的**学术合作**，欢迎随时通过 [antonio.chan.cc@outlook.com](mailto:antonio.chan.cc@outlook.com) 与我联系。


<span class='anchor' id='-新闻'></span>
# 🔥 新闻
- *2026.07*: &nbsp;🎉 一篇论文被 SIGGRAPH Asia 2026 接收。
- *2026.06*: &nbsp;🎉 一篇论文被 ECCV 2026 接收。
- *2026.02*: &nbsp;🎉 一篇论文被 CVPR 2026 接收。
- *2026.01*: &nbsp;🎉 一篇论文被 ICLR 2026 接收。
- *2025.06*: &nbsp;🎉 加入新加坡 HeyGen 担任 AI 研究实习生！
- *2024.07*: &nbsp;🎉 一篇论文被 ECCV 2024 接收。
- *2023.02*: &nbsp;🎉 一篇论文被 CVPR 2023 接收。


<span class='anchor' id='-论文发表'></span>
# 📝 论文发表

> \* 表示同等贡献。

## 视频生成与理解

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ECCV 2026</div><img src='/images/teaser/2026TransVLM.png' alt="TransVLM" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[TransVLM: A Vision-Language Framework and Benchmark for Detecting Any Shot Transitions](https://arxiv.org/abs/2604.27975) \\
**_<u>Ce Chen</u>_**, Yi Ren, Yuanming Li, Viktor Goriachko, Zhenhui Ye, Zujin Guo, Zhibin Hong, Mingming Gong

[**项目主页**](https://chence17.github.io/TransVLM/) \| [**arXiv**](https://arxiv.org/abs/2604.27975) \| [**GitHub**](https://github.com/chence17/TransVLM) \| [**博客**](https://www.heygen.com/research/transvlm)
- 提出镜头转场检测 (STD) 任务和 TransVLM 框架，通过注入光流作为运动先验，使 VLM 能够检测视频转场的连续时间片段。
- 已在 HeyGen 部署至生产环境。
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">SIGGRAPH Asia 2026</div><img src='/images/teaser/2026TAVR.png' alt="TAVR" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[TAVR: Generate Your Talking Avatar from Video Reference](https://arxiv.org/abs/2604.27918) \\
Zujin Guo, Zhenhui Ye, Yi Ren, Yuanming Li, **_<u>Ce Chen</u>_**, Zhibin Hong, Chen Change Loy

[**arXiv**](https://arxiv.org/abs/2604.27918)
- 提出一种基于视频参考的跨场景数字人视频生成新框架，融合了 token 选择机制与三阶段训练策略。
- 已在 HeyGen 部署至生产环境。
</div>
</div>


<div class='paper-box' style='border-bottom: none;'><div class='paper-box-image'><div><div class="badge">arXiv 2026</div><img src='/images/teaser/2026AvatarV.png' alt="Avatar V" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Avatar V: Scaling Video-Reference Avatar Video Generation](https://arxiv.org/abs/2606.13872) \\
Benjamin Liang, **_<u>Ce Chen</u>_**, Desmond Lin, Ivan Somov, Jiajun Zhao, Jiewei Yuan, Jingfeng Zhang, Junhao Huang, Nik Nolte, Pedram Haqiqi, Penghan Wang, Rong Yan, Rui Zhang, Sam Prokopchuk, Sivan Wang, Viktor Goriachko, Yi Ren, Yuanming Li, Yutao Chen, Zhenhui Ye, Zhibin Hong, Zilong Nie, Zujin Guo

[**arXiv**](https://arxiv.org/abs/2606.13872) \| [**博客**](https://www.heygen.com/research/avatar-v-model)
- 一个生产级规模的视频参考驱动数字人生成框架，提出 Sparse Reference Attention 实现长参考视频的线性复杂度条件建模。
- 已在 HeyGen 部署至生产环境，在数千块 GPU 上训练，数据引擎策划超 1 亿条训练片段。
</div>
</div>


## 图像生成与理解

<div class='paper-box' style='border-bottom: none;'><div class='paper-box-image'><div><div class="badge">CVPR 2026</div><img src='/images/teaser/2026Mobile-VTON.png' alt="Mobile-VTON" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Mobile-VTON: High-Fidelity On-Device Virtual Try-On](https://arxiv.org/abs/2603.00947) \\
Zhenchen Wan\*, **_<u>Ce Chen</u>_**\*, Runqi Lin, Jiaxin Huang, Tianxi Chen, Yanwu Xu, Tongliang Liu, Mingming Gong

[**项目主页**](https://zhenchenwan.github.io/Mobile-VTON/) \| [**arXiv**](https://arxiv.org/abs/2603.00947) \| [**GitHub**](https://github.com/tmllab/2026_CVPR_Mobile-VTON) \| [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-blue?label=Demo)](https://huggingface.co/FlashStight/Mobile-VTON)
- 一个保护隐私的虚拟试穿框架，支持在普通移动设备上完全离线运行。提出模块化 TGT 架构与特征引导对抗蒸馏策略。
- 在 VITON-HD 和 DressCode 数据集上以 1024×768 分辨率达到与服务器端方法相当甚至更优的性能。
</div>
</div>


## 3D/4D 生成与理解

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2026</div><img src='/images/teaser/2026Condition.png' alt="Condition Matters" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Condition Matters in Full-Head 3D GANs](https://arxiv.org/abs/2602.07198) \\
Heyuan Li, Huimin Zhang, Yuda Qiu, Zhengwentai Sun, Keru Zheng, Lingteng Qiu, Peihao Li, Qi Zuo, **_<u>Ce Chen</u>_**, Yujian Zheng, Yuming Gu, Zilong Dong, Xiaoguang Han

[**项目主页**](https://lhyfst.github.io/balancehead) \| [**arXiv**](https://arxiv.org/abs/2602.07198) \| [**GitHub**](https://github.com/lhyfst/BalanceHead)
- 提出视角不变的语义特征条件建模，将 3D 头部生成能力与观察方向解耦，在全头部合成中实现更高的保真度和多样性。
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">arXiv 2024</div><img src='/images/teaser/2024CT4D.png' alt="CT4D" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[CT4D: Consistent Text-to-4D Generation with Animatable Meshes](https://arxiv.org/abs/2408.08342) \\
**_<u>Ce Chen</u>_**, Shaoli Huang, Xuelin Chen, Guangyi Chen, Xiaoguang Han, Kun Zhang, Mingming Gong

[**arXiv**](https://arxiv.org/abs/2408.08342)
- 提出一种基于可驱动网格的全新 text-to-4D 框架，引入 Generate-Refine-Animate (GRA) 算法实现文本对齐的网格生成与一致驱动。
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ECCV 2024 <span style="color:red">(Oral, 前 1.5%)</span></div><img src='/images/teaser/2024SphereHead.png' alt="SphereHead" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[SphereHead: Stable 3D Full-head Synthesis with Spherical Tri-plane Representation](https://arxiv.org/abs/2404.05680) \\
Heyuan Li, **_<u>Ce Chen</u>_**, Tianhao Shi, Yuda Qiu, Sizhe An, Guanying Chen, Xiaoguang Han

[**项目主页**](https://lhyfst.github.io/spherehead/) \| [**arXiv**](https://arxiv.org/abs/2404.05680) \| [**GitHub**](https://github.com/lhyfst/SphereHead)
- 提出球面坐标系下的 spherical tri-plane 表示，有效缓解全头部 3D GAN 合成中的"镜像伪影"问题，并提出视角-图像一致性损失。
</div>
</div>


<div class='paper-box' style='border-bottom: none;'><div class='paper-box-image'><div><div class="badge">CVPR 2023</div><img src='/images/teaser/2023SCoDA.png' alt="SCoDA" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[SCoDA: Domain Adaptive Shape Completion for Real Scans](https://arxiv.org/abs/2304.10179) \\
Yushuang Wu, Zizheng Yan, **_<u>Ce Chen</u>_**, Lai Wei, Xiao Li, Guanbin Li, Yihao Li, Shuguang Cui, Xiaoguang Han

[**项目主页**](https://yushuang-wu.github.io/SCoDA) \| [**arXiv**](https://arxiv.org/abs/2304.10179) \| [**GitHub**](https://github.com/yushuang-wu/SCoDA)
- 提出 SCoDA 新任务（真实扫描的域自适应形状补全）及 ScanSalon 数据集，设计了跨域特征融合模块和体积一致性自训练框架。
</div>
</div>


## 医学图像分析

<div class='paper-box' style='border-bottom: none;'><div class='paper-box-image'><div><div class="badge">arXiv 2023</div><img src='/images/teaser/2023DenseMP.png' alt="DenseMP" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[DenseMP: Unsupervised Dense Pre-training for Few-shot Medical Image Segmentation](https://arxiv.org/abs/2307.09604) \\
Zhaoxin Fan, Puquan Pan, Zeren Zhang, **_<u>Ce Chen</u>_**, Tianyang Wang, Siyang Zheng, Min Xu

[**arXiv**](https://arxiv.org/abs/2307.09604)
- 提出两阶段无监督密集预训练流水线，结合分割感知的密集对比学习与超像素引导预训练，在 Abd-CT 和 Abd-MRI 数据集上达到 SOTA。
</div>
</div>


## 超分辨率

<div class='paper-box' style='border-bottom: none;'><div class='paper-box-image'><div><div class="badge">CVPR 2020</div><img src='/images/teaser/2020SPSR.png' alt="SPSR" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Structure-Preserving Super Resolution with Gradient Guidance](https://arxiv.org/abs/2003.13081) \\
Cheng Ma, Yongming Rao, Yean Cheng, **_<u>Ce Chen</u>_**, Jiwen Lu, Jie Zhou

[**arXiv**](https://arxiv.org/abs/2003.13081) \| [**GitHub**](https://github.com/Maclory/SPSR)
- 提出利用梯度图引导图像恢复的结构保持超分辨率方法，设计了梯度分支和梯度损失以施加二阶结构约束。
- 已被引用 380 余次。
</div>
</div>


<span class='anchor' id='-荣誉与奖项'></span>
# 🎖 荣誉与奖项
- *2026.03* &nbsp;🎓&nbsp; 墨尔本研究奖学金 (Melbourne Research Scholarship)
- *2026.03* &nbsp;🎓&nbsp; Rowden White 奖学金 (Rowden White Scholarship)


<span class='anchor' id='-教育背景'></span>
# 📖 教育背景

<div class='education-item'>
<div class='edu-logo'><img src='/images/unimelb-logo.png' alt='UniMelb'></div>
<div class='edu-text' markdown="1">
🎓&nbsp; **博士研究生 (Ph.D.)** \\
📚&nbsp; 理学院，数学与统计系 \\
🏫&nbsp; [墨尔本大学 (University of Melbourne)](https://www.unimelb.edu.au/) \\
📅&nbsp; 2026年3月 – 至今 \\
👨‍🏫&nbsp; 导师：[宫明明教授 (Prof. Mingming Gong)](https://mingming-gong.github.io/)
</div>
</div>

<div class='education-item'>
<div class='edu-logo'><img src='/images/cuhksz-logo.png' alt='CUHK-SZ'></div>
<div class='edu-text' markdown="1">
🎓&nbsp; **哲学硕士 (M.Phil.)** \\
📚&nbsp; 理工学院，计算机与信息工程 \\
🏫&nbsp; [香港中文大学（深圳）(CUHK-SZ)](https://www.cuhk.edu.cn/) \\
📅&nbsp; 2021年8月 – 2023年7月 \\
👨‍🏫&nbsp; 导师：[韩晓光教授 (Prof. Xiaoguang Han)](https://scholar.google.com/citations?user=z-rqsR4AAAAJ&hl=en) \| 绩点: 3.98 / 4.0 (排名 1/32)
</div>
</div>

<div class='education-item'>
<div class='edu-logo'><img src='/images/thu-logo.png' alt='THU'></div>
<div class='edu-text' markdown="1">
🎓&nbsp; **工学学士 (B.Eng.)** \\
📚&nbsp; 自动化系 \\
🏫&nbsp; [清华大学 (Tsinghua University)](https://www.tsinghua.edu.cn/) \\
📅&nbsp; 2017年8月 – 2021年7月 \\
👨‍🏫&nbsp; 导师：[李一鹏教授 (Prof. Yipeng Li)](https://www.au.tsinghua.edu.cn/info/1080/3167.htm) \| 绩点: 3.44 / 4.0
</div>
</div>


<span class='anchor' id='-实习经历'></span>
# 💻 实习经历

<div class='internship-item'>
<div class='intern-logo'><img src='/images/heygen-logo.png' alt='HeyGen'></div>
<div class='intern-text' markdown="1">
💼&nbsp; **AI 研究实习生** \\
🏢&nbsp; [HeyGen](https://www.heygen.com) \\
📍&nbsp; 新加坡 \\
📅&nbsp; 2025年6月 – 至今 \\
📝&nbsp; 导师：[任意 (Mr. Yi Ren)](https://rayeren.github.io/)。研究基于扩散模型的精确、高质量人体视频生成。
</div>
</div>

<div class='internship-item'>
<div class='intern-logo'><img src='/images/mbzuai-logo.png' alt='MBZUAI'></div>
<div class='intern-text' markdown="1">
💼&nbsp; **研究助理** \\
🏢&nbsp; 机器学习系，[穆罕默德·本·扎耶德人工智能大学 (MBZUAI)](https://mbzuai.ac.ae/) \\
📍&nbsp; 阿联酋阿布扎比 \\
📅&nbsp; 2024年2月 – 2025年6月 \\
📝&nbsp; 导师：[宫明明教授 (Prof. Mingming Gong)](https://mingming-gong.github.io/) 和 [张坤教授 (Prof. Kun Zhang)](https://www.andrew.cmu.edu/user/kunz1/)。研究 text-to-4D 生成、端侧 text-to-image 以及虚拟试穿。
</div>
</div>

<div class='internship-item'>
<div class='intern-logo'><img src='/images/cuhksz-logo.png' alt='CUHK-SZ'></div>
<div class='intern-text' markdown="1">
💼&nbsp; **研究助理** \\
🏢&nbsp; 理工学院，[香港中文大学（深圳）(CUHK-SZ)](https://www.cuhk.edu.cn/) \\
📍&nbsp; 中国广东深圳 \\
📅&nbsp; 2023年8月 – 2024年1月 \\
📝&nbsp; 导师：[韩晓光教授 (Prof. Xiaoguang Han)](https://scholar.google.com/citations?user=z-rqsR4AAAAJ&hl=en)。研究基于 spherical tri-plane 表示的高保真 3D 人头生成。
</div>
</div>

<div class='internship-item'>
<div class='intern-logo'><img src='/images/tencent-logo.png' alt='Tencent'></div>
<div class='intern-text' markdown="1">
💼&nbsp; **计算机视觉算法工程师实习生** \\
🏢&nbsp; 微信事业群，[腾讯 (Tencent)](https://www.tencent.com/) \\
📍&nbsp; 中国北京 \\
📅&nbsp; 2021年6月 – 2021年8月 \\
📝&nbsp; 开发表格识别系统，将摄像头拍摄或 PDF 截取的表格图片转换为结构化 HTML，已成为公司电子办公系统的一部分。
</div>
</div>

<div class='internship-item'>
<div class='intern-logo'><img src='/images/bytedance-logo.png' alt='ByteDance'></div>
<div class='intern-text' markdown="1">
💼&nbsp; **计算机视觉算法工程师实习生** \\
🏢&nbsp; AI Lab，[字节跳动 (ByteDance)](https://www.bytedance.com/) \\
📍&nbsp; 中国北京 \\
📅&nbsp; 2020年6月 – 2020年11月 \\
📝&nbsp; 开发户型图矢量化系统，实现结构化房间解析，识别准确率超过 90%，转化效率提升 5 倍以上。
</div>
</div>


<span class='anchor' id='-学术服务'></span>
# 📋 学术服务
- 📖&nbsp; 会议审稿人：NeurIPS 2026, ECCV 2026, CVPR 2026, ICLR 2026, NeurIPS 2025
- 📖&nbsp; 期刊审稿人：IEEE Transactions on Multimedia, IEEE Signal Processing Letters, IEEE Transactions on Image Processing
