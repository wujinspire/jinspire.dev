---
layout: post
title: "AI仍然无法读取Google Scholar的数字"
excerpt: "测试表明，在查找谷歌学术最高引用学者时，多数AI出现严重幻觉。仅Gemini表现优异，这意味着通用人工智能依然遥远。"
date: 2025-11-02
lang: zh
pair: yoshua-1m-citation.en
translated_by: Gemini
---

- 祝贺 **Yoshua Bengio** 达到 **100万引用**！
- 我一直想知道谁拥有 **最多的引用**，以及 **前10名**。所以我用AI帮我寻找答案。
- **令人惊讶的是，AI搜索甚至深度研究都没有找到正确的结果**，并且产生了很多幻觉 —— 尽管这真的 **很简单的** 验证。
- 分数：
  - GPT 5 + Web Search: **3.66** / 10
  - GPT 5 Deep Research: **2.66** / 10
  - **Gemini 2.5**: 🥈 **6** / 10
  - **Gemini 2.5 Deep Research**: 🥇 **9.33** / 10
  - Claude 4.5 Sonnect Research: **3** / 10
  - Manus: 服务器宕机
  - **Perplexity**: 🥉 **4.66** / 10
- 我相信AI用于研究和一般浏览器使用，但似乎AI的发展并没有我预期的那么快。AGI还很遥远吗？

# 故事

祝贺Yoshua Bengio达到100万引用！

我一直有这个想法，通过4个简单的问题来测试AI的能力：
- 谁拥有最多的引用？
- 哪篇论文拥有最多的引用？
- 哪个github拥有最多的star？
- 哪个模型拥有最多的下载量？

上述问题的好处是它们非常容易验证。AI能搞定这份工作吗？

**令人惊讶的是，AI并没有我预期的那么好，即使是关于引用的第一个问题，这显然是最简单的一个。**

现在，让我们试一试AI，看看它的表现如何。

# 提示词 (Prompt)

我对简单的浏览器使用和深度研究都使用以下提示词。

***Who has the most citations?** Please list the top 10 names and their count. Use Google Scholar as the ground truth. Also give me the link to the Google Scholar page for each person.*
(***谁拥有最多的引用？** 请列出前10个名字和他们的计数。使用Google Scholar作为基本事实。还要给我每个人Google Scholar页面的链接。*)

评分标准：
- 名字，引用，链接各值0.33分。
- 如果名字出现在前10名中，它就算数。
- 如果名字不正确，其余的总是计0分。
- ✅ 表示正确
- 空白表示不相关
- 🥹 表示引用非常接近真相
- ❌ 表示不正确

## GPT5 + web search

1. ✅ Yoshua Bengio, 🥹 Citations: 1,000,000+, ✅ https://scholar.google.com/citations?hl=en&user=kukA0LcAAAAJ&utm_source=chatgpt.com
2. ✅ Geoffrey E. Hinton, ✅ Citations: 975,672, ✅ https://scholar.google.com/citations?hl=en&user=JicYPdAAAAAJ
3. ✅ Kaiming He, ✅ Citations: 759,096, ✅ https://scholar.google.com/citations?hl=en&user=DhtAFkwAAAAJ
4. ✅ John P. A. Ioannidis, ✅ Citations: 660,135, ✅ https://scholar.google.com/citations?hl=en&user=JiiMY_wAAAAJ
5. Ronald C. Kessler, Citations: 620,716, https://scholar.google.com/citations?hl=en&user=EicYvbwAAAAJ
6. Salim Yusuf, Citations: 538,991, https://scholar.google.com/citations?hl=en&user=mF0tslEAAAAJ
7. Robert Langer, Citations: 460,975, https://scholar.google.com/citations?hl=en&user=5HX--AYAAAAJ
8. Yann LeCun, Citations: 434,072, https://scholar.google.com/citations?hl=en&user=WLN3QrAAAAAJ
9. Michael I. Jordan, Citations: 343,289, https://scholar.google.com/citations?hl=en&user=yxUduqMAAAAJ
10. Andrew Y. (Andrew) Ng, Citations: 298,734, https://scholar.google.com/citations?hl=en&user=mG4imMEAAAAJ

总分: ✅ 3.66 / 10

## GPT 5 Deep Research

1. ✅ Michel Foucault, ✅ Citations: ~1,360,000, ❌ https://www.astralcodexten.com/p/your-book-review-how-language-began

2. ✅ Yoshua Bengio, 🥹 Citations: over 1,000,000, ❌ https://eu.36kr.com/en/p/3525357754522499#:~:text=Yoshua%20Bengio%20has%20become%20the,the%20academic%20influence%20of%20AI

3. ✅ Geoffrey Hinton, 🥹 Citations: ≈970,000, ❌ https://eu.36kr.com/en/p/3525357754522499#:~:text=Yoshua%20Bengio%20has%20become%20the,the%20academic%20influence%20of%20AI

4. Ahmedin Jemal, Citations: 948,985, ❌ https://www.adscientificindex.com/citation-ranking/#:~:text=

5. ❌ Pierre Bourdieu, ❌Citations: 771,000+, ❌ https://scholar.google.com/citations?hl=en&user=5HX--AYAAAAJ (完全幻觉？)

6. ✅ Kaiming He, 🥹 Citations: 757,848, ❌ https://www.adscientificindex.com/citation-ranking/#:~:text=

7. ❌ Eric Lander, ❌ Citations: 737,656, ❌ https://www.adscientificindex.com/citation-ranking/#:~:text= (完全幻觉？)

8. ✅ Ilya Sutskever, Citations: 699,329, ❌ https://www.adscientificindex.com/citation-ranking/#:~:text=

9. ✅ Richard M. Ryan, Citations: 698,909, ❌ https://www.adscientificindex.com/citation-ranking/#:~:text=

10. ✅ Gregory Y. H. Lip, Citations: 666,315, ❌ https://www.adscientificindex.com/citation-ranking/#:~:text=

不完全确定为什么它不显示Google Scholar，即使我给了一个额外的提示要求链接。

总分: ✅ 2.66 / 10

## Gemini 2.5

1.	✅ Michel Foucault, 🥹 Citations: ~1,026,000+, ✅ https://scholar.google.com/citations?user=AKqYlxMAAAAJ
2.	✅ Douglas G. Altman, 🥹 Citations: ~1,000,000+, ✅ https://scholar.google.com/citations?user=_QnLm3kAAAAJ
3.	✅ Yoshua Bengio, ✅ Citations: 1,003,766, ✅ https://scholar.google.com/citations?user=kukA0LcAAAAJ
4.	✅ Geoffrey Hinton, ✅ Citations: 975,672, ✅ https://scholar.google.com/citations?user=JicYPdAAAAAJ
5.	✅ Ahmedin Jemal, ✅ Citations: 953,685, ✅ https://scholar.google.com/citations?user=8o-FYhUAAAAJ
6.	✅ Kaiming He, 🥹 Citations: ~745,000+, ✅ https://scholar.google.com/citations?user=DhtAFkwAAAAJ
7.	✅ Ilya Sutskever, ✅ Citations: 709,155, ✅ https://scholar.google.com/citations?user=x04W_mMAAAAJ
8.	Yann LeCun, Citations: 434,072, https://scholar.google.com/citations?user=WLN3QrAAAAAJ
9.	Ronald C. Kessler, Citations: ~392,000+, https://scholar.google.com/citations?user=EicYvbwAAAAJ
10.	Sigmund Freud, Citations: 381,725, ❌ https://www.google.com/search?q=https://scholar.google.com/citations%3Fuser%3DkENAAfAAAAAJ

总分: ✅ 6 / 10

## Gemini 2.5 Deep Research

1. ✅ Michel Foucault, ✅ Citations: 1,393,602, ✅ https://scholar.google.com/citations?user=AKqYlxMAAAAJ
2. ✅ Douglas G. Altman, ✅ Citations: 1,043,906, ✅ https://scholar.google.com/citations?user=_QnLm3kAAAAJ
3. ✅ Yoshua Bengio, ✅ Citations: 1,003,766, ✅ https://scholar.google.com/citations?user=kukA0LcAAAAJ
4. ✅ Geoffrey Hinton, ✅ Citations: 975,672, ✅ https://scholar.google.com/citations?user=JicYPdAAAAAJ
5. ✅ Ahmedin Jemal, 🥹 Citations: 953,685, ✅ https://scholar.google.com/citations?user=8o-FYhUAAAAJ
6. ✅ Kaiming He, ✅ Citations: 759,096, ✅ https://scholar.google.com/citations?user=DhtAFkwAAAAJ
7. ✅ Ilya Sutskever, ✅ Citations: 709,155, ✅ https://scholar.google.com/citations?user=x04W_mMAAAAJ
8. ✅ Richard M. Ryan, ✅ Citations: 708,904, ✅ https://scholar.google.com/citations?user=fraRBsIAAAAJ
9. ✅ Gregory Y. H. Lip, 🥹 Citations: 667,742, ✅ https://scholar.google.com/citations?user=cqY4wxQAAAAJ
10. ✅ John P. A. Ioannidis, ✅ Citations: 660,135, ✅ https://scholar.google.com/citations?user=JiiMY_wAAAAJ

总分: ✅ 9.33 / 10

## Claude 4.5 Sonnect Research

1. ✅ Michel Foucault, ✅ Citations: 1,393,602, ✅ https://scholar.google.com/citations?user=AKqYlxMAAAAJ
2. ❌ Pierre Bourdieu, Citations: 1,128,000+, https://scholar.google.com/citations?user=d_lp40IAAAAJ
3. ✅ Yoshua Bengio, 🥹 Citations: 1,000,000+, ✅ https://scholar.google.com/citations?user=kukA0LcAAAAJ
4. ✅ Kaiming He, 🥹 Citations: 759,061, ✅ https://scholar.google.com/citations?user=DhtAFkwAAAAJ
5. ✅ Geoffrey Hinton, 🥹 Citations: 733,529, ✅ https://scholar.google.com/citations?user=JicYPdAAAAAJ
6. Eric Lander, Citations: 552,013-600,000+, https://scholar.google.com/citations?user=LXVfPc8AAAAJ
7. Bert Vogelstein, Citations: 530,285, https://scholar.google.com/citations?user=O3FVg9AAAAAJ
8. Noam Chomsky, Citations: 530,056, https://scholar.google.com/citations?user=rbgNVw0AAAAJ
9. Sigmund Freud, Citations: 453,000+, https://scholar.google.com/citations?user=N80kIiYAAAAJ
10. Yann LeCun, Citations: 434,260, https://scholar.google.com/citations?user=WLN3QrAAAAAJ

总分: ✅ 3 / 10

## Manus

服务器宕机

## Perplexity

1. ✅ Michel Foucault, ✅ Citations: 1,393,602, ✅ https://scholar.google.com/citations?user=AKqYlxMAAAAJ
2. ✅ Yoshua Bengio, ✅ Citations: 1,003,766, ✅ https://scholar.google.com/citations?user=kukA0LcAAAAJ
3. ✅ Geoffrey Hinton, ✅ Citations: 975,672, ✅ https://scholar.google.com/citations?user=JicYPdAAAAAJ
4. ✅ Kaiming He, ✅ Citations: 759,096, ✅ https://scholar.google.com/citations?user=DhtAFkwAAAAJ
5. ✅ Ilya Sutskever, 🥹 Citations: 709,155, ✅ https://scholar.google.com/citations?user=x04W_mMAAAAJ
6. Pierre Bourdieu, Citations: 771,039, https://scholar.google.com/citations?user=5HX--AYAAAAJ
7. JoAnn E. Manson, Citations: 497,937, https://scholar.google.com/citations?user=QK07bYEAAAAJ
8. Yann LeCun, Citations: 434,072, https://scholar.google.com/citations?user=WLN3QrAAAAAJ
9. Graham Colditz, Citations: 401,251, https://scholar.google.com/citations?user=M5_mEHQAAAAJ
10. Shizuo Akira, Citations: ~380,000+, https://scholar.google.com/citations?user=0TG2laoAAAAJ

总分: ✅ 4.66 / 10

## SuperGrok Deep Research

1. ✅ Michel Foucault, ✅ Citations: 1,393,602, ✅ https://scholar.google.com/citations?user=AKqYlxMAAAAJ&hl=en
2. ❌ Albert Bandura, 🥹 Citations: 1,016,872, ❌ https://scholar.google.com/citations?user=muejNL8AAAAJ&hl=en
3. ✅ Yoshua Bengio, ✅ Citations: 1,003,766, ✅ https://scholar.google.com/citations?user=kukA0LcAAAAJ&hl=en
4. ✅ Geoffrey Hinton, ✅ Citations: 975,672, ✅ https://scholar.google.com/citations?user=JicYPdAAAAAJ&hl=en
5. ✅ Kaiming He, ✅ Citations: 759,061, ✅ https://scholar.google.com/citations?user=DhtAFkwAAAAJ&hl=en
6. ✅ Ilya Sutskever, ✅ Citations: 709,845, ✅ https://scholar.google.com/citations?user=x04W_mMAAAAJ&hl=en
7. Ronald C. Kessler, Citations: 620,535, https://scholar.google.com/citations?user=EicYvbwAAAAJ&hl=en
8. Jürgen Habermas, Citations: 535,169, https://scholar.google.com/citations?user=Y1oUEw4AAAAJ&hl=en
9. Anthony Giddens, Citations: 533,831, https://scholar.google.com/citations?user=woDR56wAAAAJ&hl=en
10. Noam Chomsky, Citations: 530,056, https://scholar.google.com/citations?user=rbgNVw0AAAAJ&hl=en

总分: ✅ 4.66 / 10

## Qwen 3 Max + Search

达到最大token限制，只得到3个。

Top Cited Researchers (based on available data):

1. ✅ Yoshua Bengio, 🥹 Citations: Over 1,000,000, ✅ https://scholar.google.com/citations?user=kukA0LcAAAAJ
2. ✅ Geoffrey Hinton, ✅ Citations: Approximately 975,672, ✅ https://scholar.google.com/citations?user=JicYPdAAAAJ
3. ✅ He Kaiming (Kaiming He), 🥹 Citations: Reports vary between 460,000+ to over 750,000, ✅ https://scholar.google.com/citations?user=DhtAFkwAAAAJ

总分: ✅ 2.33 / 10

# ✅ 基本事实 (Ground Truth): 基于上述结果合并 + 人工验证的数字
1. Michel Foucault, Citations: 1,393,602, https://scholar.google.com/citations?user=AKqYlxMAAAAJ
2. Douglas G. Altman, Citations: 1,045,914, https://scholar.google.com/citations?user=_QnLm3kAAAAJ
3. Yoshua Bengio, Citations: 1,003,766, https://scholar.google.com/citations?user=kukA0LcAAAAJ
4. Geoffrey Hinton, Citations: 975,672, https://scholar.google.com/citations?user=JicYPdAAAAAJ
5. Ahmedin Jemal, Citations: 955,442, https://scholar.google.com/citations?user=8o-FYhUAAAAJ
6. Kaiming He, Citations: 759,096, https://scholar.google.com/citations?user=DhtAFkwAAAAJ
7. Ilya Sutskever, Citations: 709,845, https://scholar.google.com/citations?user=x04W_mMAAAAJ
8. Richard M. Ryan, Citations: 708,904, https://scholar.google.com/citations?user=fraRBsIAAAAJ
9. Gregory Y. H. Lip, Citations: 668,113, https://scholar.google.com/citations?user=cqY4wxQAAAAJ
10. John P. A. Ioannidis, Citations: 660,135, https://scholar.google.com/citations?user=JiiMY_wAAAAJ

我不敢100%确定没有遗漏的名字，但我已经验证了引用和链接。

# 试试你自己的

如果我有更多时间，我想尝试以下问题：

***Which paper has the most citations?** Please list the top 10 papers and their count. Use Google Scholar as the ground truth. Also give me the link to the paper's page.*
(***哪篇论文拥有最多的引用？** 请列出前10篇论文和它们的计数。使用Google Scholar作为基本事实。还要给我论文页面的链接。*)

***What is the github with the most stars?** Please list the top 10 github repositories and their star count. Use Github as the ground truth. Also give me the link to the github repository.*
(***哪个github拥有最多的star？** 请列出前10个github仓库和它们的star计数。使用Github作为基本事实。还要给我github仓库的链接。*)

***Which model has the most downloads?** Please list the top 10 models and their download count. Use Hugging Face as the ground truth. Also give me the link to the model's page.*
(***哪个模型拥有最多的下载量？** 请列出前10个模型和它们的下载计数。使用Hugging Face作为基本事实。还要给我模型页面的链接。*)

另外，如果我遗漏了任何应该在前10名的名字，请告诉我！
