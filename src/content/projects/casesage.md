---
title: "CaseSage"
tagline: "Analysis of Indian Legal Documents"
start: "Nov 2024"
end: "May 2025"
stack: ["Longformer", "NER", "Neo4j", "FAISS", "RAG"]
segments:
  - label: "Long-document extraction"
    problem: "Indian court judgments run long enough that a standard summarizer truncates them, and the precedents, statutes, and holdings a practitioner actually needs are exactly what truncation drops."
    solution: "Devised a Legal NLP system pairing Longformer-based summarization, which attends over the whole judgment rather than a truncated prefix, with named-entity recognition so precedent citations survive into the output."
    improvement: "~85% entity-extraction F1 on structured extraction from lengthy judgments. The work became a paper at MIDAS 2025 (Springer)."
    metrics:
      - value: "~85%"
        label: "entity-extraction F1"
        direction: "up"
  - label: "Precedent retrieval"
    problem: "Keyword search cannot follow a citation that does not use the case's exact title, and a judge citing a decades-old decision rarely does."
    solution: "Built knowledge-graph precedent retrieval over the case relationships, making lookup a graph traversal instead of a keyword match, with RAG-based QA over the judgment corpus on top."
    improvement: "Case-analysis lookup time cut ~40% versus manual precedent search."
    metrics:
      - value: "~40%"
        label: "less case-analysis lookup time"
        direction: "down"
provenance: "default_bullets"
featured: true
order: 3
highlights:
  - "Automated structured extraction from lengthy Indian court judgments, measured by ~85% entity-extraction F1, by devising a Legal NLP system with Longformer-based summarization and named-entity recognition."
  - "Cut case-analysis lookup time ~40% versus manual precedent search by implementing knowledge-graph precedent retrieval and RAG-based QA over the judgment corpus."
---
