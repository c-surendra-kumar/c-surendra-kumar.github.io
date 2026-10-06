---
title: "AgriNav"
tagline: "NDVI-Guided Irrigation Drone Navigation"
start: "Feb 2024"
end: "Apr 2024"
stack: ["Arduino C++", "GPS", "ARIMA", "NDVI"]
segments:
  - label: "Choosing which zones to water"
    problem: "Irrigating a whole plot uniformly wastes water, so the first question is which zones actually need it, and that is a forecasting problem rather than a sensing one."
    solution: "Selected those zones with an ARIMA model over per-zone NDVI time series."
    metrics: []
  - label: "Flying the route"
    problem: "Visiting the selected zones efficiently is a routing problem, and it has to run on an Arduino with a flight battery as the real constraint."
    solution: "Built the GPS waypoint-navigation stack in Arduino C++, routing the drone through the zones needing water along the shortest flight path."
    improvement: "Field-tested on a farm plot, and took 1st prize at a college tech fest."
    metrics:
      - value: "1st"
        label: "prize at a college tech fest"
        direction: "flat"
provenance: "default_bullets"
featured: false
order: 7
highlights:
  - "Built the GPS waypoint-navigation stack for an autonomous irrigation drone in Arduino C++, routing it through the zones needing water along the shortest flight path."
  - "Selected those zones with an ARIMA model over per-zone NDVI time series, and field-tested the drone on a farm plot, taking 1st prize at a college tech fest."
---
