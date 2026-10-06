---
title: "CompressIQ"
tagline: "Bandwidth-Aware Gradient Compression for Heterogeneous Clusters"
start: "Jan 2026"
end: "May 2026"
stack: ["Python", "PyTorch", "Convex Optimization", "Discrete-Event Simulation", "Multi-GPU HPC"]
segments:
  - problem: "Data-parallel training on a heterogeneous cluster is bounded by its slowest link. Compressing every worker's gradients at the same ratio ignores that: fast workers get degraded for nothing, and the slow ones still gate the all-reduce."
    solution: "Formulated per-worker gradient-compression ratios as a convex min-max program over a ring all-reduce cost model, treating the ratio as a decision variable rather than a constant. Added error-feedback-aware bounds so convergence holds and per-layer ratios so the choice tracks each layer's sensitivity, validated with a discrete-event simulator and a real multi-GPU CNN training run on an HPC cluster."
    improvement: "A simulated 3.26x speedup over uniform compression at matched accuracy on a 12-worker, 3-tier cluster. That figure is a simulator result; the multi-GPU training run confirmed the implementation, not the speedup."
    metrics:
      - value: "3.26x"
        label: "simulated speedup over uniform compression"
        direction: "up"
      - value: "12"
        label: "workers across a 3-tier cluster"
        direction: "flat"
provenance: "default_bullets"
featured: true
order: 4
highlights:
  - "Formulated per-worker gradient-compression ratios as a convex min-max program over a ring all-reduce cost model, validated via a discrete-event simulator and a real multi-GPU CNN training run on an HPC cluster."
  - "Achieved a simulated 3.26x speedup over uniform compression at matched accuracy (12-worker, 3-tier cluster) by adding error-feedback-aware bounds and per-layer compression ratios."
---
