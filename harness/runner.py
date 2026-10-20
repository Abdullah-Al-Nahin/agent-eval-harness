import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Dict, Any

def execute_task(task: Dict[str, Any]) -> Dict[str, Any]:
    """Executes synthesized code alongside its unit test in an isolated subprocess."""
    task_id = task.get("task_id", "unknown")
    code = task.get("candidate_solution", "")
    unit_test = task.get("unit_test", "")
    timeout = task.get("timeout_sec", 5)

    full_script = f"{code}\n\n# --- Unit Tests ---\n{unit_test}\n"

    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False, encoding="utf-8") as tmp_file:
        tmp_file.write(full_script)
        tmp_path = Path(tmp_file.name)

    start_time = time.perf_counter()
    passed = False
    status = "failed"
    stderr_out = ""

    try:
        proc = subprocess.run(
            [sys.executable, str(tmp_path)],
            capture_output=True,
            text=True,
            timeout=timeout
        )
        latency_ms = round((time.perf_counter() - start_time) * 1000, 2)

        if proc.returncode == 0 and "ALL_TESTS_PASSED" in proc.stdout:
            passed = True
            status = "passed"
        else:
            stderr_out = proc.stderr.strip()
            status = "syntax_error" if "SyntaxError" in stderr_out else "assertion_or_runtime_error"

    except subprocess.TimeoutExpired:
        latency_ms = round(timeout * 1000, 2)
        status = "timeout"
        stderr_out = f"Execution exceeded {timeout}s timeout."
    finally:
        if tmp_path.exists():
            tmp_path.unlink()

    return {
        "task_id": task_id,
        "language": task.get("language", "python"),
        "passed": passed,
        "status": status,
        "latency_ms": latency_ms,
        "error": stderr_out
    }
