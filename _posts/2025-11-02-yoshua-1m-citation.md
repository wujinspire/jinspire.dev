---
layout: post
title: "AI still can't read Google Scholar's numbers"
date: 2025-11-02
lang: en
---

- Congratulations to **Yoshua Bengio** for hitting **1 million citations**!
- I'm always wondering who has **the most citations**, also the **top 10**.
- **Surprisingly, search and even deep research are not finding the correct results**, and hallucinate a lot - althrough it's fairly **simple** to verify.
- Scores:
  - GPT 5 + Web Search: **3.66** / 10
  - GPT 5 Deep Research: **2.66** / 10
  - **Gemini 2.5**: 🥈 **6** / 10
  - **Gemini 2.5 Deep Research**: 🥇 **9.33** / 10
  - Claude 4.5 Sonnect Research: **3** / 10
  - Manus: server down
  - **Perplexity**: 🥉 **4.66** / 10
- I believe in AI for research and general browser use, but it seems the claims around AI development are not as impressive as I expected. Seems AGI is still far away?


# The Story

Congradulations to Yoshua Bengio for hitting 1 million citations!

I always have this idea to test AI's ability by 4 simple questions:
- Who has the most citations?
- Which paper has the most citations?
- What is the github with the most stars?
- Which model has the most downloads?

The good thing of the above questions is that they are very easy to verify. Can AI ace this job?

**Surprisingly, AI is not doing as good as I expected, even for the first question about citations, which clearly is the simplest one.**

Now, let's give AI a try and see how it performs.


# Prompt

I use the below prompt for both naive browser use and deep research.

***Who has the most citations?** Please list the top 10 names and their count. Use Google Scholar as the ground truth. Also give me the link to the Google Scholar page for each person.*

Grading criteria:
- Name, Citations, Link each worth 0.33 points.
- If name is shown in top 10, it counts.
- If name is incorrect, the rest always counts 0.
- ✅ for correct
- Blank for not relevant
- 🥹 for citations very close to the truth
- ❌ for incorrect


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

Total score: ✅ 3.66 / 10


## GPT 5 Deep Research

1. ✅ Michel Foucault, ✅ Citations: ~1,360,000, ❌ https://www.astralcodexten.com/p/your-book-review-how-language-began

2. ✅ Yoshua Bengio, 🥹 Citations: over 1,000,000, ❌ https://eu.36kr.com/en/p/3525357754522499#:~:text=Yoshua%20Bengio%20has%20become%20the,the%20academic%20influence%20of%20AI

3. ✅ Geoffrey Hinton, 🥹 Citations: ≈970,000, ❌ https://eu.36kr.com/en/p/3525357754522499#:~:text=Yoshua%20Bengio%20has%20become%20the,the%20academic%20influence%20of%20AI

4. Ahmedin Jemal, Citations: 948,985, ❌ https://www.adscientificindex.com/citation-ranking/#:~:text=

5. ❌ Pierre Bourdieu, ❌Citations: 771,000+, ❌ https://scholar.google.com/citations?hl=en&user=5HX--AYAAAAJ (Complete Hallucination?)

6. ✅ Kaiming He, 🥹 Citations: 757,848, ❌ https://www.adscientificindex.com/citation-ranking/#:~:text=

7. ❌ Eric Lander, ❌ Citations: 737,656, ❌ https://www.adscientificindex.com/citation-ranking/#:~:text= (Complete Hallucination?)

8. ✅ Ilya Sutskever, Citations: 699,329, ❌ https://www.adscientificindex.com/citation-ranking/#:~:text=

9. ✅ Richard M. Ryan, Citations: 698,909, ❌ https://www.adscientificindex.com/citation-ranking/#:~:text=

10. ✅ Gregory Y. H. Lip, Citations: 666,315, ❌ https://www.adscientificindex.com/citation-ranking/#:~:text=

Not exactly sure why it's not showing Google Scholar, even after I gave an addition prompt asking for the link.

Total score: ✅ 2.66 / 10


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

Total score: ✅ 6 / 10


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

Total score: ✅ 9.33 / 10


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

Total score: ✅ 3 / 10


## Manus

Server down


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

Total score: ✅ 4.66 / 10

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

Total score: ✅ 4.66 / 10


## Qwen 3 Max + Search

Hit max token limit and only got 3.

Top Cited Researchers (based on available data):

1. ✅ Yoshua Bengio, 🥹 Citations: Over 1,000,000, ✅ https://scholar.google.com/citations?user=kukA0LcAAAAJ
2. ✅ Geoffrey Hinton, ✅ Citations: Approximately 975,672, ✅ https://scholar.google.com/citations?user=JicYPdAAAAJ
3. ✅ He Kaiming (Kaiming He), 🥹 Citations: Reports vary between 460,000+ to over 750,000, ✅ https://scholar.google.com/citations?user=DhtAFkwAAAAJ

Total score: ✅ 2.33 / 10


# ✅ Ground Truth: Numbers based on the merge of above results + Manual verification
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


I'm not 100% sure about the NOT missing names, but I've verified the citations and links.


# Try your own

If I have more time, I would like to experiment the following questions:

***Which paper has the most citations?** Please list the top 10 papers and their count. Use Google Scholar as the ground truth. Also give me the link to the paper's page.*

***What is the github with the most stars?** Please list the top 10 github repositories and their star count. Use Github as the ground truth. Also give me the link to the github repository.*

***Which model has the most downloads?** Please list the top 10 models and their download count. Use Hugging Face as the ground truth. Also give me the link to the model's page.*

Also please let me know if I missed any names that should be in the top 10!