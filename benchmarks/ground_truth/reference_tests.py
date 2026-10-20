"""Reference ground-truth test definitions for baseline verification."""

def verify_output_marker(stdout: str) -> bool:
    return "ALL_TESTS_PASSED" in stdout
