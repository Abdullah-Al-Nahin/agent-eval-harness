import argparse
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from harness import execute_task, compute_summary_metrics

def main():
    parser = argparse.ArgumentParser(description="Run Agent-Eval-Harness benchmark suite.")
    parser.add_argument("--tasks", default="benchmarks/tasks.json", help="Path to tasks JSON file")
    parser.add_argument("--output", default="results/run_01.json", help="Path to output report JSON")
    args = parser.parse_args()

    tasks_path = PROJECT_ROOT / args.tasks
    output_path = PROJECT_ROOT / args.output
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(tasks_path, "r", encoding="utf-8-sig") as f:
        tasks = json.load(f)

    print(f"[*] Running {len(tasks)} benchmark tasks from {args.tasks}...")
    results = []
    for task in tasks:
        res = execute_task(task)
        results.append(res)
        badge = "PASS" if res["passed"] else "FAIL"
        print(f"    [{badge}] {res['task_id']} ({res['latency_ms']} ms) -> {res['status']}")

    summary = compute_summary_metrics(results)
    payload = {"summary": summary, "task_results": results}

    with open(output_path, "w", encoding="utf-8-sig") as f:
        json.dump(payload, f, indent=2)

    print("\n=== Evaluation Summary ===")
    print(f"Pass@1 Score   : {summary['pass_at_1'] * 100:.1f}% ({summary['passed_tasks']}/{summary['total_tasks']})")
    print(f"Mean Latency   : {summary['avg_latency_ms']} ms")
    print(f"Report Saved   : {args.output}")

if __name__ == "__main__":
    main()
