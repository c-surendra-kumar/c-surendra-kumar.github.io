---
title: "Why Dogwhistle Detection is Harder Than It Sounds"
description: "Coded political phrases are designed to be deniable, which makes them a hard retrieval and classification problem rather than a keyword-matching one."
pubDate: 2026-03-10
tags: ["NLP", "Research"]
draft: false
---


A dogwhistle is a phrase that carries a hidden meaning: a general audience hears
something innocuous, an in-group hears a signal. Political dogwhistles are
everywhere in modern discourse and they are deliberately built to be deniable.

## The core challenge

Most text classification tasks have a clear signal. The text either says the
thing or it does not. Dogwhistles do not work that way. The same phrase is
neutral in one context and loaded in another, so a model trained on surface form
learns the wrong thing.

Keyword matching fails immediately. Naive fine-tuning also struggles, because
the training signal is sparse and almost entirely context-dependent.

## The approach

The pipeline has three stages:

1. **Transcription at scale.** Bulk audio acquisition, then transcription with
   Whisper large-v3 on an A100.
2. **Dense retrieval.** Each transcript segment is embedded and indexed in FAISS
   using inner product over normalized vectors, so a query against a curated
   lexicon surfaces candidate segments.
3. **Contrastive classification.** The candidate segment is presented alongside
   a neutral paraphrase and a known coded example, and the model decides whether
   this particular usage is coded.

## What is actually hard

Evaluation, more than modeling. Taxonomies in this area tend to contain positive
examples only, which means a precision number is meaningless until you have
constructed your own negatives, and constructing good negatives is most of the
work. This is the same lesson as every other retrieval project: the benchmark is
the deliverable.

## What I would do differently

Contrastive prompting works but is slow and expensive per segment. A lighter
first-pass classifier to filter segments before the expensive call should cut
cost substantially at minimal recall loss.
