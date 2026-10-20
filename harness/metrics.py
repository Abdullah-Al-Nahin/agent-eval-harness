from typing import List, Dict, Any

def compute_summary_metrics(results: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Computes Pass@1, average execution latency, and error breakdown."""
    total = len(results)
    if total == 0:
        return {"total_tasks": 0, "pass_at_1": 0.0, "avg_latency_ms": 0.0, "status_breakdown": {}}

    passed_count = sum(1 for r in results if r["passed"])
    avg_latency = sum(r["latency_ms"] for r in results) / total

    breakdown: Dict[str, int] = {}
    for r in results:
        st = r["status"]
        breakdown[st] = breakdown.get(st, 0) + 1

    return {
        "total_tasks": total,
        "passed_tasks": passed_count,
        "pass_at_1": round(passed_count / total, 4),
        "avg_latency_ms": round(avg_latency, 2),
        "status_breakdown": breakdown
    }
