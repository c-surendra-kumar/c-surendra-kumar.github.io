---
role: "Graduate Research Assistant"
org: "University of Maryland, CLIP Lab"
orgUrl: "https://wiki.umiacs.umd.edu/clip/"
start: "Sep 2025"
end: "Present"
current: true
stack: ["PyTorch", "HuggingFace", "FAISS", "RAG", "SBERT", "BERT", "T5", "Llama", "Gemma"]
mark: "umd"
segments:
  - label: "Dog whistle detection in podcasts"
    problem: "A dog whistle says one thing to a general audience and something else to an in-group, which lets it move opinion while staying deniable. They had been studied in congressional speech and on Reddit, X and Gab, but never in podcasts, even though podcasts are now mainstream news: around a third of US adults sometimes get news from them, and most listeners expect that news to be accurate. Long-form transcripts also make hand annotation impractical at the scale the question needs."
    solution: "Built a human-AI collaborative annotation framework that scales human labelling to long-form podcast transcripts, applied it across 100+ podcasts, and fine-tuned an LLM-based detector on the resulting dataset."
    improvement: "Produced the largest human-labelled dog whistle dataset to date, then used the detector to measure how prevalent dog whistles are across the sampled podcasts. Code, models, model outputs and datasets released for future work."
    metrics:
      - value: "10+"
        label: "podcasts annotated for dog whistles"
        direction: "flat"
      - value: "1st"
        label: "study of dog whistles in podcasts"
        direction: "flat"
  - label: "Harmful-speech classification"
    problem: "Coded harmful speech splits into distinct mechanisms, and the available taxonomies supply positive examples only, so there is nothing to measure precision against."
    solution: "Fine-tuned SBERT, BERT, and T5 classifiers for seven harmful-speech mechanisms in social-media posts and benchmarked them against zero-shot Llama and Gemma baselines."
    improvement: "Per-mechanism precision and recall measured against zero-shot baselines."
    metrics:
      - value: "7"
        label: "harmful-speech mechanisms classified"
        direction: "flat"
  - label: "Cross-modal evaluation"
    problem: "Coded language does not stay in the text: the same signal can sit in the imagery alongside it, which a text-only pipeline cannot see."
    solution: "Developed scalable multimodal evaluation pipelines combining text and computer vision models to analyze coded language patterns and detect cross-modal signals."
    metrics: []
provenance: "default_bullets"
figuresFrom: "Author's own AAAI 2026 submission on dog whistles in podcasts"
order: 2
highlights:
  - "Selected the best-performing LLM for political-discourse QA, measured by a 5-model eval on faithfulness and relevance, by building a FAISS RAG pipeline over podcast transcripts and scoring each configuration."
  - "Fine-tuned SBERT, BERT, and T5 classifiers for seven harmful-speech mechanisms in social-media posts, benchmarking them against zero-shot Llama and Gemma baselines on per-mechanism precision and recall."
  - "Developed scalable multimodal evaluation pipelines combining text and computer vision models to analyze coded language patterns and detect cross-modal signals."
---
