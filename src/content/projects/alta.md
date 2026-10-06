---
title: "ALTA"
tagline: "Adaptive Logistics and Tracking Agent"
start: "Apr 2026"
end: "May 2026"
stack: ["LangGraph", "FastAPI", "React", "SQLite", "LLM Risk Scoring"]
segments:
  - problem: "Cold-chain shipments fail quietly. A temperature excursion or a customs hold is only expensive if nobody notices for a day, and a sequential polling loop finds out in the order it happens to check, not in the order that matters."
    solution: "Orchestrated a real-time agentic system in LangGraph, FastAPI, and React where each shipment moves through a multi-agent conditional-DAG workflow rather than a fixed sequence of checks, so agents run only when a shipment's state calls for them. An LLM scores risk from the combined signals, with SQLite persistence and human-in-the-loop approval gates before any intervention."
    improvement: "Cut shipment-monitoring latency ~50% versus a sequential polling baseline, and ran automated risk assessment across 20+ concurrent cold-chain shipments in load tests."
    metrics:
      - value: "~50%"
        label: "lower monitoring latency"
        direction: "down"
      - value: "20+"
        label: "concurrent shipments in load tests"
        direction: "flat"
links:
  - label: "Live demo"
    url: "https://alta-logistics-agent.netlify.app/"
provenance: "default_bullets"
featured: true
order: 1
highlights:
  - "Cut shipment-monitoring latency ~50% versus a sequential polling baseline by orchestrating a real-time agentic system in LangGraph, FastAPI, and React with multi-agent conditional-DAG workflows and LLM-based risk scoring."
  - "Ran automated risk assessment across 20+ concurrent cold-chain shipments in load tests, with SQLite persistence and human-in-the-loop approval gates before any intervention."
---
