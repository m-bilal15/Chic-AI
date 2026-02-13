"""
Re-run the 16 fixed test scripts and update organization
"""

import subprocess
import sys
import time
import shutil
from pathlib import Path
from datetime import datetime


def organize_test_result(test_id, status, output, duration):
    """Organize test result - move from Failed to Passed if now passing"""

    results_base = Path("results")
    failed_folder = results_base / "Failed" / test_id
    passed_folder = results_base / "Passed" / test_id

    if status == "PASSED":
        # Remove from Failed folder if it exists
        if failed_folder.exists():
            shutil.rmtree(failed_folder)
            print(f"  [MOVED] {test_id}: Failed -> Passed")

        # Create/update Passed folder
        passed_folder.mkdir(parents=True, exist_ok=True)

        # Copy screenshots
        for screenshot in results_base.glob(f"{test_id}*.png"):
            shutil.copy(screenshot, passed_folder / screenshot.name)

        # Create TEST_REPORT.md
        report = f"""# Test Report - {test_id}

**Test Case ID:** {test_id}
**Status:** PASSED
**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Duration:** {duration:.1f} seconds

## Test Result

[PASS] Test executed successfully after fix.

## Evidence

Screenshots available in this folder.

---

**Report Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        with open(passed_folder / "TEST_REPORT.md", 'w') as f:
            f.write(report)


def rerun_fixed_tests():
    """Re-run the 16 fixed tests"""

    fixed_tests = [
        "TC_OB_004", "TC_OB_005", "TC_OB_010",
        "TC_OB_S2_008", "TC_OB_S3_009",
        "TC_OB_S4_007", "TC_OB_S4_008", "TC_OB_S4_013",
        "TC_OB_S5_007", "TC_OB_S5_008", "TC_OB_S5_009",
        "TC_OB_S5_010", "TC_OB_S5_011", "TC_OB_S5_012",
        "TC_OB_S5_016", "TC_OB_S5_017"
    ]

    print("="*70)
    print("RE-RUNNING 16 FIXED TESTS")
    print("="*70)
    print(f"Total tests: {len(fixed_tests)}\\n")

    passed = 0
    failed = 0

    for i, test_id in enumerate(fixed_tests, 1):
        test_path = Path(f"testcases/{test_id}/test_script.py")

        print(f"[{i}/16] Running: {test_id}...", end=" ")

        test_start = time.time()

        try:
            result = subprocess.run(
                [sys.executable, str(test_path)],
                capture_output=True,
                text=True,
                timeout=120,
                encoding='utf-8',
                errors='replace'
            )

            test_duration = time.time() - test_start

            if result.returncode == 0:
                print("[PASS]")
                passed += 1
                organize_test_result(test_id, "PASSED", "", test_duration)
            else:
                print("[FAIL]")
                print(f"    Error: {result.stderr[:100]}")
                failed += 1

        except Exception as e:
            print(f"[ERROR] {str(e)[:50]}")
            failed += 1

    print("\\n" + "="*70)
    print("RE-RUN COMPLETE")
    print("="*70)
    print(f"[PASS] Now Passing: {passed}/16")
    print(f"[FAIL] Still Failing: {failed}/16")
    print(f"Fix Rate: {(passed/16*100):.1f}%")
    print("="*70 + "\\n")

    return passed, failed


if __name__ == "__main__":
    rerun_fixed_tests()
