import time
import json
import collections
import threading

class VortexMetrics:
    """
    A low-overhead telemetry collector for high-performance systems.
    Designed to capture latency, throughput, and custom metrics without
    stalling the main execution thread.
    """
    def __init__(self, system_name):
        self.system_name = system_name
        self.metrics = collections.defaultdict(list)
        self.lock = threading.Lock()
        self._start_time = time.time()

    def record_latency(self, label, duration_ms):
        """Records a latency data point (e.g., matching engine cycle time)."""
        with self.lock:
            self.metrics[f"{label}_latency_ms"].append({
                "t": time.time() - self._start_time,
                "v": duration_ms
            })

    def increment_counter(self, label, amount=1):
        """Increments a counter (e.g., total orders processed)."""
        with self.lock:
            current = self.metrics[f"{label}_count"]
            last_val = current[-1]["v"] if current else 0
            self.metrics[f"{label}_count"].append({
                "t": time.time() - self._start_time,
                "v": last_val + amount
            })

    def get_snapshot(self):
        """Returns a snapshot of current metrics and clears the buffer."""
        with self.lock:
            snapshot = dict(self.metrics)
            self.metrics.clear()
            return snapshot

    def export_to_json(self, filename):
        """Saves current metrics to a JSON file for analysis."""
        snapshot = self.get_snapshot()
        with open(filename, "w") as f:
            json.dump({
                "system": self.system_name,
                "timestamp": time.time(),
                "data": snapshot
            }, f, indent=4)

# Example: Profiling an HFT Engine Cycle
# metrics = VortexMetrics("Vortex-HFT")
# start = time.perf_counter()
# ... perform matching ...
# metrics.record_latency("matching_engine", (time.perf_counter() - start) * 1000)
