"""
Run all 60 signup tests one by one
Complete test suite execution
"""

import subprocess
import sys
import time
from pathlib import Path
from datetime import datetime


def run_all_signup_tests():
    """Run all 60 signup tests"""

    # All 60 test cases in order
    all_tests = [
        "TC_SIGNUP_001", "TC_SIGNUP_002", "TC_SIGNUP_003", "TC_SIGNUP_004", "TC_SIGNUP_005",
        "TC_SIGNUP_006", "TC_SIGNUP_007", "TC_SIGNUP_008", "TC_SIGNUP_009", "TC_SIGNUP_010",
        "TC_SIGNUP_011", "TC_SIGNUP_012", "TC_SIGNUP_013", "TC_SIGNUP_014", "TC_SIGNUP_015",
        "TC_SIGNUP_016", "TC_SIGNUP_017", "TC_SIGNUP_018", "TC_SIGNUP_019", "TC_SIGNUP_020",
        "TC_SIGNUP_021", "TC_SIGNUP_022", "TC_SIGNUP_023", "TC_SIGNUP_024", "TC_SIGNUP_025",
        "TC_SIGNUP_026", "TC_SIGNUP_027", "TC_SIGNUP_028", "TC_SIGNUP_029", "TC_SIGNUP_030",
        "TC_SIGNUP_031", "TC_SIGNUP_032", "TC_SIGNUP_033", "TC_SIGNUP_034", "TC_SIGNUP_035",
        "TC_SIGNUP_036", "TC_SIGNUP_037", "TC_SIGNUP_038", "TC_SIGNUP_039", "TC_SIGNUP_040",
        "TC_SIGNUP_041", "TC_SIGNUP_042", "TC_SIGNUP_043", "TC_SIGNUP_044", "TC_SIGNUP_045",
        "TC_SIGNUP_046", "TC_SIGNUP_047", "TC_SIGNUP_048", "TC_SIGNUP_049", "TC_SIGNUP_050",
        "TC_SIGNUP_051", "TC_SIGNUP_052", "TC_SIGNUP_053", "TC_SIGNUP_054", "TC_SIGNUP_055",
        "TC_SIGNUP_056", "TC_SIGNUP_057", "TC_SIGNUP_058", "TC_SIGNUP_060"
    ]

    print("\n" + "="*70)
    print("RUNNING ALL 60 SIGNUP TESTS - COMPLETE SUITE")
    print("="*70)
    print(f"Total tests to run: {len(all_tests)}")
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*70 + "\n")

    passed = 0
    failed = 0
    errors = 0
    skipped = 0

    results = []
    start_time = time.time()

    for i, test_id in enumerate(all_tests, 1):
        test_path = Path(f"testcases/{test_id}/test_script.py")

        if not test_path.exists():
            print(f"\n[{i}/{len(all_tests)}] SKIP: {test_id} - File not found")
            skipped += 1
            results.append((test_id, "SKIP", "File not found"))
            continue

        print(f"\n{'='*70}")
        print(f"[{i}/{len(all_tests)}] Running: {test_id}")
        print(f"{'='*70}")

        try:
            # Run test using Python directly
            result = subprocess.run(
                [sys.executable, str(test_path)],
                capture_output=True,
                text=True,
                timeout=120,
                encoding='utf-8',
                errors='replace'
            )

            if result.returncode == 0:
                print(f"[PASS] PASSED: {test_id}")
                passed += 1
                results.append((test_id, "PASSED", ""))
            else:
                print(f"[FAIL] FAILED: {test_id}")
                error_msg = result.stderr[:200] if result.stderr else "Unknown error"
                print(f"   Error: {error_msg}")
                failed += 1
                results.append((test_id, "FAILED", error_msg[:100]))

        except subprocess.TimeoutExpired:
            print(f"[WARNING] TIMEOUT: {test_id}")
            errors += 1
            results.append((test_id, "TIMEOUT", "Test exceeded 120 seconds"))
        except Exception as e:
            print(f"[ERROR] ERROR: {test_id} - {str(e)[:100]}")
            errors += 1
            results.append((test_id, "ERROR", str(e)[:100]))

    end_time = time.time()
    duration = end_time - start_time

    # Summary
    print("\n" + "="*70)
    print("COMPLETE TEST SUITE EXECUTION SUMMARY")
    print("="*70)
    print(f"Total Tests:    {len(all_tests)}")
    print(f"[PASS] Passed:  {passed}")
    print(f"[FAIL] Failed:  {failed}")
    print(f"[WARN] Errors:  {errors}")
    print(f"[SKIP] Skipped: {skipped}")
    print(f"Pass Rate:      {(passed/(len(all_tests)-skipped)*100):.1f}%")
    print(f"Duration:       {duration/60:.1f} minutes ({duration:.0f} seconds)")
    print(f"Completed at:   {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*70)

    # Breakdown by phase
    print("\n" + "="*70)
    print("RESULTS BY PHASE")
    print("="*70)

    phases = {
        "Phase 1 - Critical": ["TC_SIGNUP_001", "TC_SIGNUP_002", "TC_SIGNUP_009", "TC_SIGNUP_013",
                               "TC_SIGNUP_018", "TC_SIGNUP_019", "TC_SIGNUP_022", "TC_SIGNUP_031",
                               "TC_SIGNUP_032", "TC_SIGNUP_033", "TC_SIGNUP_034", "TC_SIGNUP_035", "TC_SIGNUP_036"],
        "Phase 2 - High": ["TC_SIGNUP_003", "TC_SIGNUP_005", "TC_SIGNUP_006", "TC_SIGNUP_007",
                          "TC_SIGNUP_008", "TC_SIGNUP_010", "TC_SIGNUP_012", "TC_SIGNUP_014",
                          "TC_SIGNUP_015", "TC_SIGNUP_016", "TC_SIGNUP_017", "TC_SIGNUP_020",
                          "TC_SIGNUP_021", "TC_SIGNUP_028", "TC_SIGNUP_029", "TC_SIGNUP_030",
                          "TC_SIGNUP_037", "TC_SIGNUP_038", "TC_SIGNUP_039", "TC_SIGNUP_040"],
        "Phase 3 - Medium": ["TC_SIGNUP_004", "TC_SIGNUP_011", "TC_SIGNUP_023", "TC_SIGNUP_024",
                            "TC_SIGNUP_025", "TC_SIGNUP_026", "TC_SIGNUP_027", "TC_SIGNUP_041",
                            "TC_SIGNUP_042", "TC_SIGNUP_043", "TC_SIGNUP_044", "TC_SIGNUP_045",
                            "TC_SIGNUP_046", "TC_SIGNUP_047", "TC_SIGNUP_048", "TC_SIGNUP_049"],
        "Phase 4 - Low": ["TC_SIGNUP_050", "TC_SIGNUP_051", "TC_SIGNUP_052", "TC_SIGNUP_053",
                         "TC_SIGNUP_054", "TC_SIGNUP_055", "TC_SIGNUP_056", "TC_SIGNUP_057",
                         "TC_SIGNUP_058", "TC_SIGNUP_060"]
    }

    for phase_name, phase_tests in phases.items():
        phase_passed = sum(1 for t, s, _ in results if t in phase_tests and s == "PASSED")
        phase_total = len(phase_tests)
        print(f"{phase_name}: {phase_passed}/{phase_total} passed")

    # Detailed results
    print("\n" + "="*70)
    print("DETAILED RESULTS - ALL 60 TESTS")
    print("="*70)

    for test_id, status, message in results:
        status_symbol = "[PASS]" if status == "PASSED" else "[FAIL]" if status == "FAILED" else "[WARN]" if status == "TIMEOUT" else "[SKIP]"
        print(f"{status_symbol} {test_id}: {status}")
        if message and status != "PASSED":
            print(f"   {message[:80]}")

    print("="*70 + "\n")

    # Save results
    results_file = Path("results/all_tests_summary.txt")
    try:
        with open(results_file, "w", encoding="utf-8") as f:
            f.write(f"All Signup Tests Execution Summary\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total: {len(all_tests)}, Passed: {passed}, Failed: {failed}, Errors: {errors}, Skipped: {skipped}\n")
            f.write(f"Pass Rate: {(passed/(len(all_tests)-skipped)*100):.1f}%\n")
            f.write(f"Duration: {duration:.0f} seconds\n\n")

            for test_id, status, message in results:
                f.write(f"{test_id}: {status}\n")
                if message:
                    f.write(f"  {message}\n")

        print(f"[SAVED] Results saved to: {results_file}\n")
    except Exception as e:
        print(f"[WARNING] Could not save results file: {e}\n")

    return passed, failed, errors


if __name__ == "__main__":
    run_all_signup_tests()
