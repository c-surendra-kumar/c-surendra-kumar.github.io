---
title: "AgentLens"
tagline: "AI Agent Evaluation and Observability Platform"
start: "Jan 2026"
end: "Apr 2026"
stack: ["LangGraph", "FastAPI", "PostgreSQL", "Redis", "OpenTelemetry", "MCP"]
segments:
  - label: "Tracing agent behavior"
    problem: "When an agent returns a wrong answer the cause is usually several steps back: a tool called with the wrong argument, a retrieval that returned nothing useful, a constraint quietly dropped during planning. None of it is visible from the output."
    solution: "Architected an open-source evaluation platform in LangGraph, FastAPI, and OpenTelemetry that traces LLM calls, tool usage, retrieval, and multi-step agent workflows as inspectable spans, with an MCP trace-inspection server exposing them for failure analysis."
    improvement: "Gave engineers full visibility into agent behavior across every workflow step."
    metrics: []
  - label: "Measuring reliability"
    problem: "Without a repeatable measurement, a change to a prompt or a model gets judged by eye, and regressions ship because nothing contradicts them."
    solution: "Built offline benchmarks that score task success, tool-selection accuracy, retrieval quality, hallucination, latency, and token efficiency over the traced runs."
    improvement: "Repeatable reliability and safety checks that a change can be measured against."
    metrics: []
provenance: "default_bullets"
featured: true
order: 2
highlights:
  - "Gave engineers full visibility into agent behavior, measured by traced LLM calls, tool usage, and retrieval across every workflow step, by architecting an open-source evaluation platform in LangGraph, FastAPI, and OpenTelemetry."
  - "Built repeatable reliability and safety checks for agentic systems, measured by offline benchmarks scoring task success, tool accuracy, and hallucination rate, via an MCP trace-inspection server."
---
