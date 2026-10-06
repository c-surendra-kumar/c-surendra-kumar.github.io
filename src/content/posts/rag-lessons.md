---
title: "RAG is Not Magic: Lessons from Building Three RAG Systems"
description: "Retrieval-augmented generation sounds simple in blog posts. Every component has failure modes you do not anticipate until production. Notes from building RAG over legal documents, enterprise QA, and political speech."
pubDate: 2026-01-18
tags: ["RAG", "Engineering"]
draft: false
---

Retrieval-augmented generation is the most overhyped and underspecified pattern
in applied ML right now. Everyone says "just use RAG." Almost nobody talks about
why it fails.

I have now built three of these: one over Indian court judgments (CaseSage), one
for multi-document enterprise QA at Kaar Technologies, and one over political
podcast transcripts at the CLIP Lab. The failure modes repeated.

## Failure mode 1: bad chunking

How you split documents determines what can be retrieved at all. Fixed-size
chunking loses context exactly at the boundaries, which in a legal judgment is
often where the holding lives.

For CaseSage we moved to semantic chunking, splitting on paragraph and section
boundaries instead of token counts. That single change improved retrieval
quality more than any model swap we tried. The surrounding system ended up at
roughly 85% entity-extraction F1 on structured extraction from those judgments,
and cut case-analysis lookup time about 40% against manual precedent search.

## Failure mode 2: the wrong similarity metric

FAISS defaults to L2 distance. For most embedding models you want cosine
similarity. Switching from `IndexFlatL2` to `IndexFlatIP` over normalized
vectors is a one-line change that is very easy to overlook and quietly costs you
recall:

```python
# Wrong (L2 distance)
index = faiss.IndexFlatL2(dim)

# Right (cosine similarity via inner product on normalized vectors)
faiss.normalize_L2(embeddings)
index = faiss.IndexFlatIP(dim)
```

## Failure mode 3: no evaluation

Most RAG systems ship without any retrieval evaluation. If you are not measuring
recall@k on a held-out query set, you cannot tell whether a change helped or
hurt, and you will keep making changes anyway.

RAGAS is a reasonable starting point for end-to-end evaluation. On CaseSage it
caught two regressions that would otherwise have shipped.

The same principle applies upward: when I needed to pick a model for
political-discourse QA at the lab, the answer came from running a five-model
evaluation on faithfulness and relevance, not from a preference. Retrieval
tuning without measurement is just rearranging.

## The honest summary

RAG works well when retrieval is good, chunks are meaningful, and you evaluate
it. None of those three are free, and none of them are what the tutorials spend
their time on.
