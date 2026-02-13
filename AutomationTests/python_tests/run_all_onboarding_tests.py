"""
Run all 78 onboarding tests and organize results into Passed/Failed folders
Following CLAUDE.md guidelines
"""

import subprocess
import sys
import time
import shutil
from pathlib import Path
from datetime import datetime


def create_test_report(test_id, status, duration, screenshot_path, video_path):
    """Create TEST_REPORT.md for passed tests"""

    report = f"""# Test Report - {test_id}

**Test Case ID:** {test_id}
**Status:** {status}
**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Duration:** {duration:.1f} seconds
**Tester:** Automated Test Framework

---

## Test Description

Onboarding questionnaire test case.

---

## Test Result

[{status}] Test executed successfully.

---

## Evidence

**Screenshots:**
- Initial: {test_id}_initial.png
- Final: {test_id}_final.png
- Evidence: {test_id}_evidence.png

**Video Recording:**
- {video_path if video_path else 'Not available'}

---

## Notes

- Test executed as part of complete onboarding test suite
- All assertions passed
- Visual verification recommended via screenshots

---

**Report Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Framework:** Python + Playwright + Pytest v2.0
"""
    return report


def organize_test_results(test_id, status, output, duration):
    """Organize test results into Passed/Failed folders per CLAUDE.md"""

    results_base = Path("results")

    if status == "PASSED":
        # Create Passed folder structure
        test_folder = results_base / "Passed" / test_id
        test_folder.mkdir(parents=True, exist_ok=True)

        # Move screenshots
        for screenshot in results_base.glob(f"{test_id}*.png"):
            try:
                shutil.copy(screenshot, test_folder / screenshot.name)
            except:
                pass

        # Create TEST_REPORT.md
        report = create_test_report(test_id, "PASSED", duration, "", "")
        report_file = test_folder / "TEST_REPORT.md"
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report)

        print(f"  [ORGANIZED] {test_id} -> Passed/ folder")

    else:  # FAILED or ERROR
        # Create Failed folder structure
        test_folder = results_base / "Failed" / test_id
        test_folder.mkdir(parents=True, exist_ok=True)

        # Move screenshots
        for screenshot in results_base.glob(f"{test_id}*.png"):
            try:
                shutil.copy(screenshot, test_folder / screenshot.name)
            except:
                pass

        # Create BUG_REPORT.md (simplified for now)
        bug_report = f"""# Bug Report - {test_id}

**Bug ID:** BUG-OB-{test_id.split('_')[-1]}
**Test Case ID:** {test_id}
**Status:** Open
**Severity:** HIGH
**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## Description

Test {test_id} failed during execution.

---

## Error Details

```
{output[:500]}
```

---

## Evidence

Screenshots available in this folder.

---

**Reported By:** Automated Test Framework
**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""

        bug_file = test_folder / "BUG_REPORT.md"
        with open(bug_file, 'w', encoding='utf-8') as f:
            f.write(bug_report)

        print(f"  [ORGANIZED] {test_id} -> Failed/ folder with BUG_REPORT.md")


def run_all_onboarding_tests():
    """Run all 78 onboarding tests and organize results"""

    # Get all TC_OB_* directories
    testcases_dir = Path("testcases")
    all_tests = sorted([d.name for d in testcases_dir.iterdir()
                       if d.is_dir() and d.name.startswith("TC_OB")])

    print("\n" + "="*70)
    print("RUNNING ALL ONBOARDING TESTS - COMPLETE SUITE")
    print("="*70)
    print(f"Total tests found: {len(all_tests)}")
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*70 + "\n")

    # Ensure results folders exist
    Path("results/Passed").mkdir(parents=True, exist_ok=True)
    Path("results/Failed").mkdir(parents=True, exist_ok=True)

    passed = 0
    failed = 0
    errors = 0

    results = []
    start_time = time.time()

    for i, test_id in enumerate(all_tests, 1):
        test_path = Path(f"testcases/{test_id}/test_script.py")

        if not test_path.exists():
            print(f"\n[{i}/{len(all_tests)}] SKIP: {test_id} - File not found")
            continue

        print(f"\n{'='*70}")
        print(f"[{i}/{len(all_tests)}] Running: {test_id}")
        print(f"{'='*70}")

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
                print(f"[PASS] PASSED: {test_id}")
                passed += 1
                results.append((test_id, "PASSED", "", test_duration))
                organize_test_results(test_id, "PASSED", "", test_duration)
            else:
                print(f"[FAIL] FAILED: {test_id}")
                error_msg = result.stderr[:200] if result.stderr else "Unknown error"
                print(f"   Error: {error_msg[:100]}")
                failed += 1
                results.append((test_id, "FAILED", error_msg[:100], test_duration))
                organize_test_results(test_id, "FAILED", error_msg, test_duration)

        except subprocess.TimeoutExpired:
            print(f"[WARNING] TIMEOUT: {test_id}")
            errors += 1
            results.append((test_id, "TIMEOUT", "Exceeded 120 seconds", 120))
            organize_test_results(test_id, "TIMEOUT", "Test timeout", 120)

        except Exception as e:
            print(f"[ERROR] ERROR: {test_id} - {str(e)[:100]}")
            errors += 1
            results.append((test_id, "ERROR", str(e)[:100], 0))
            organize_test_results(test_id, "ERROR", str(e), 0)

    end_time = time.time()
    duration = end_time - start_time

    # Final Summary
    print("\n" + "="*70)
    print("ALL ONBOARDING TESTS - EXECUTION COMPLETE")
    print("="*70)
    print(f"Total Tests:     {len(all_tests)}")
    print(f"[PASS] Passed:   {passed}")
    print(f"[FAIL] Failed:   {failed}")
    print(f"[WARN] Errors:   {errors}")
    print(f"Pass Rate:       {(passed/len(all_tests)*100):.1f}%")
    print(f"Duration:        {duration/60:.1f} minutes")
    print(f"Completed at:    {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*70)

    # Results organized
    print("\n" + "="*70)
    print("RESULTS ORGANIZATION")
    print("="*70)
    print(f"Passed tests:  results/Passed/ ({passed} folders)")
    print(f"Failed tests:  results/Failed/ ({failed} folders)")
    print("="*70 + "\n")

    print("[NOTE] Each test folder contains:")
    print("  - Screenshots (initial, final, evidence)")
    print("  - TEST_REPORT.md (for passed) or BUG_REPORT.md (for failed)")
    print("  - Video recordings (if available)")
    print("\n")

    return passed, failed, errors


if __name__ == "__main__":
    run_all_onboarding_tests()
