# Music Mixing Secrets

**用图解拆开混音问题，用试听做出判断。**

写给正在学习人声处理与节奏组混音的音乐人。这里收录中文图文教程、详细研究报告与可编辑源码，从信号路由和参数含义出发，理解每一步在改变什么。

## 图文教程

点击封面进入专题，或从下方直接阅读报告与完整图文。

<p>
  <a href="posts/delay-v3/"><img src="posts/delay-v3/source/output/xhs-01-cover.png" alt="低 Wet 人声 Ping Pong Delay：给人声一点空间" width="280"></a>
  <a href="posts/ms-return/"><img src="posts/ms-return/source/output/xhs-01-cover.png" alt="人声空间与 Side EQ：先查效果返回，再决定要不要收窄" width="280"></a>
  <a href="posts/drums-bass/"><img src="posts/drums-bass/source/output/xhs-01-cover.png" alt="鼓与 Bass：先把地基搭稳" width="280"></a>
</p>

### 01 · 给人声一点空间

低 Wet 的 Ping Pong Delay：把延迟时间、反馈、干湿混合与滤波分开理解，控制重复声的节奏与存在感。

[研究报告](posts/delay-v3/RESEARCH_REPORT.md) · [完整图文 PDF](posts/delay-v3/source/output/vocal-delay-v3.pdf) · [逐页图片](posts/delay-v3/source/output/) · [HTML 源码](posts/delay-v3/source/index.html)

### 02 · 人声空间与 Side EQ

加上空间后中频变糊？从效果返回查起，理解 M/S 的和差关系，以及何时值得尝试局部 Side EQ。

[研究报告](posts/ms-return/RESEARCH_REPORT.md) · [完整图文 PDF](posts/ms-return/source/output/vocal-side-eq.pdf) · [逐页图片](posts/ms-return/source/output/) · [HTML 源码](posts/ms-return/source/index.html)

### 03 · 鼓与 Bass，先把地基搭稳

从 Kick、Bass 与 Snare 的关系出发，依次检查音量平衡、时间与极性、频率分工和前后层次。

[研究报告](posts/drums-bass/RESEARCH_REPORT.md) · [完整图文 PDF](posts/drums-bass/source/output/drums-bass.pdf) · [逐页图片](posts/drums-bass/source/output/) · [HTML 源码](posts/drums-bass/source/index.html)

## 怎么使用

- **先看图文**：用 PDF 或逐页图片了解主题，再带着具体问题阅读研究报告。
- **再查原理**：报告附有图解、计算与来源，区分产品功能、数学示意和试听建议。参数只作为尝试的起点，请放回自己的歌曲中比较。
- **需要编辑**：下载仓库，保留各专题的 `source/` 目录结构，在浏览器中打开 `index.html`；修改与导出方法见各专题说明。

## 引用

```bibtex
@misc{wang2026musicmixingsecrets,
  author = {Kangdi, Wang},
  title = {Music Mixing Secrets},
  year = {2026},
  howpublished = {GitHub repository},
  url = {https://github.com/DDDPG/music-mixing-secrets},
  note = {Illustrated mixing tutorials, research reports, and editable source}
}
```

[下载 BibTeX](CITATION.bib) · 引用具体结论时，请同时注明对应专题及其原始来源。

<details>
<summary>更多文档与历史版本</summary>

[历史版本](history/) · [制作流程](WORKFLOW.md) · [版本记录](CHANGELOG.md) · [档案说明](ARCHIVE_NOTES.md)

</details>

素材与源码适用不同的授权条款，转载或修改前请阅读[版权与许可说明](RIGHTS.md)。
