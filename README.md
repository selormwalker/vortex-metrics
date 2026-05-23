# ðŸ“Š Vortex Metrics

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Performance: Low-Overhead](https://img.shields.io/badge/performance-low--overhead-green.svg)](#)

**Vortex Metrics** is a high-performance, low-overhead telemetry collector designed for mission-critical and low-latency systems (HFT, P2P networks, Real-time APIs). It allows you to capture high-resolution latency and throughput data without blocking your main execution paths.

## ðŸš€ Features
- **Thread-Safe:** Lock-protected collectors for concurrent environments.
- **Low Overhead:** Optimized for microsecond-sensitive applications.
- **Latency Tracking:** Capture high-resolution timing data for engine cycles.
- **Throughput Monitoring:** Simple increment counters for volume tracking.
- **JSON Export:** Standardized output for integration with Grafana, ELK, or custom dashboards.

## ðŸ› ï¸ Quick Start
```python
from vortex_metrics import VortexMetrics
import time

# Initialize metrics for your engine
metrics = VortexMetrics("MatchingEngine-V1")

# Record a latency data point
start_time = time.perf_counter()
# ... critical logic ...
duration = (time.perf_counter() - start_time) * 1000 # convert to ms
metrics.record_latency("order_execution", duration)

# Increment a counter
metrics.increment_counter("orders_processed")

# Export metrics to file
metrics.export_to_json("telemetry.json")
```

## ðŸ¤ Contributing
Help us make system monitoring faster. Issues and pull requests are welcome.

---
Built with âš¡ by [David Selorm Walker](https://github.com/selormwalker)
