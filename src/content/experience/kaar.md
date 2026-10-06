---
role: "Machine Learning Intern"
org: "Kaar Technologies"
orgUrl: "https://www.kaartech.com/"
start: "May 2024"
end: "Feb 2025"
current: false
stack: ["LangChain", "FAISS", "TinyLLaMA-1.1B", "FastAPI", "Gemini API", "Word2Vec", "spaCy"]
mark: "k"
segments:
  - label: "Multi-document QA"
    problem: "Document QA over a large corpus was too slow to use interactively, which meant people fell back to searching by hand."
    solution: "Designed a LangChain, FAISS, and TinyLLaMA-1.1B RAG system with retrieval and inference optimizations."
    improvement: "Multi-document QA query latency down 35% against the initial pipeline."
    metrics:
      - value: "35%"
        label: "lower query latency"
        direction: "down"
  - label: "KPI extraction"
    problem: "Business metrics were locked inside unstructured reports, so every number had to be pulled out and classified by a person."
    solution: "Built a lightweight Word2Vec and spaCy system for semantic extraction and classification of performance indicators."
    improvement: "KPI processing time down 40% against manual extraction."
    metrics:
      - value: "40%"
        label: "less KPI processing time"
        direction: "down"
  - label: "Candidate screening"
    problem: "Candidate screening had no automated tooling at all, so first-round interviews consumed recruiter time before any signal existed."
    solution: "Built a GenAI recruitment platform in FastAPI where candidates upload resumes and answer voice-chatbot interview questions, then multiple Gemini API calls consolidate each conversation into a shortlisting report."
    improvement: "Recruiters receive a consolidated shortlisting report per candidate instead of scheduling every first round."
    metrics: []
provenance: "default_bullets"
order: 4
highlights:
  - "Reduced multi-document QA query latency by 35%, measured against the initial pipeline, by designing a LangChain, FAISS, and TinyLLaMA-1.1B RAG system with retrieval and inference optimizations."
  - "Reduced KPI processing time by 40%, measured against manual extraction, by building a lightweight Word2Vec and spaCy system for semantic extraction and classification of performance indicators."
  - "Built a GenAI recruitment platform in FastAPI where candidates upload resumes and answer voice-chatbot interview questions, then multiple Gemini API calls consolidate each conversation into a shortlisting report for recruiters."
---
