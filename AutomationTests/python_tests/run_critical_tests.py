"""
Run all critical signup tests one by one
Workaround for import file mismatch issue
"""

import subprocess
import sys
from pathlib import Path


def run_critical_tests():
    """Run all 13 critical signup tests"""

    critical_tests = [
        "TC_SIGNUP_001",  # Page load
        "TC_SIGNUP_002",  # Valid signup
        "TC_SIGNUP_009",  # Google OAuth
        "TC_SIGNUP_013",  # All fields empty
        "TC_SIGNUP_018",  # Password mismatch
        "TC_SIGNUP_019",  # Password too short
        "TC_SIGNUP_022",  # Duplicate email
        "TC_SIGNUP_031",  # SQL injection (Name)
        "TC_SIGNUP_032",  # SQL injection (Email)
        "TC_SIGNUP_033",  # XSS (Name)
        "TC_SIGNUP_034",  # XSS (Email)
        "TC_SIGNUP_035",  # XSS (Password)
        "TC_SIGNUP_036",  # HTTPS security
    ]

    print("\n" + "="*70)
    print("RUNNING 13 CRITICAL SIGNUP TESTS")
    print("="*70)
    print(f"Total tests to run: {len(critical_tests)}")
    print("="*70 + "\n")

    passed = 0
    failed = 0
    errors = 0

    results = []

    for i, test_id in enumerate(critical_tests, 1):
        test_path = Path(f"testcases/{test_id}/test_script.py")

        if not test_path.exists():
            print(f"\n[{i}/{len(critical_tests)}] SKIP: {test_id} - File not found")
            errors += 1
            results.append((test_id, "SKIP", "File not found"))
            continue

        print(f"\n{'='*70}")
        print(f"[{i}/{len(critical_tests)}] Running: {test_id}")
        print(f"{'='*70}")

        try:
            # Run test using Python directly
            result = subprocess.run(
                [sys.executable, str(test_path)],
                capture_output=True,
                text=True,
                timeout=120
            )

            if result.returncode == 0:
                print(f"[PASS] PASSED: {test_id}")
                passed += 1
                results.append((test_id, "PASSED", ""))
            else:
                print(f"[FAIL] FAILED: {test_id}")
                print(f"   Error output: {result.stderr[:200]}")
                failed += 1
                results.append((test_id, "FAILED", result.stderr[:100]))

        except subprocess.TimeoutExpired:
            print(f"[WARNING] TIMEOUT: {test_id}")
            errors += 1
            results.append((test_id, "TIMEOUT", "Test exceeded 120 seconds"))
        except Exception as e:
            print(f"[ERROR] ERROR: {test_id} - {e}")
            errors += 1
            results.append((test_id, "ERROR", str(e)))

    # Summary
    print("\n" + "="*70)
    print("TEST EXECUTION SUMMARY")
    print("="*70)
    print(f"Total Tests:  {len(critical_tests)}")
    print(f"[PASS] Passed:    {passed}")
    print(f"[FAIL] Failed:    {failed}")
    print(f"[WARNING] Errors:    {errors}")
    print(f"Pass Rate:    {(passed/len(critical_tests)*100):.1f}%")
    print("="*70)

    print("\n" + "="*70)
    print("DETAILED RESULTS")
    print("="*70)

    for test_id, status, message in results:
        status_symbol = "[PASS]" if status == "PASSED" else "[FAIL]" if status == "FAILED" else "[WARN]"
        print(f"{status_symbol} {test_id}: {status}")
        if message:
            print(f"   {message[:80]}")

    print("="*70 + "\n")

    # Save results
    with open("results/critical_tests_summary.txt", "w", encoding="utf-8") as f:
        f.write(f"Critical Tests Execution Summary\n")
        f.write(f"Date: {Path.ctime(Path(__file__))}\n")
        f.write(f"Total: {len(critical_tests)}, Passed: {passed}, Failed: {failed}, Errors: {errors}\n\n")

        for test_id, status, message in results:
            f.write(f"{test_id}: {status}\n")
            if message:
                f.write(f"  {message}\n")

    print(f"📄 Results saved to: results/critical_tests_summary.txt\n")

    return passed, failed, errors


if __name__ == "__main__":
    run_critical_tests()
