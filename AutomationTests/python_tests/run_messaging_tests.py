"""
Run All Messaging Tests Sequentially
Avoids pytest import conflicts from same-named test_script.py files
Created: February 13, 2026
"""

import subprocess
import time
from pathlib import Path
import json

def run_messaging_tests():
    """Run all messaging tests one by one"""

    print("\n" + "=" * 80)
    print("RUNNING ALL MESSAGING TESTS")
    print("=" * 80)
    print("Total: 15 tests")
    print("Expected time: 30-40 minutes")
    print("=" * 80 + "\n")

    # Find all messaging test directories
    testcases_dir = Path("testcases")
    messaging_tests = sorted([d for d in testcases_dir.glob("TC_CHAT_MSG_*") if d.is_dir()])

    print(f"Found {len(messaging_tests)} messaging tests\n")

    results = {
        "total": len(messaging_tests),
        "passed": 0,
        "failed": 0,
        "errors": 0,
        "test_results": []
    }

    # Run each test
    for i, test_dir in enumerate(messaging_tests, 1):
        test_id = test_dir.name
        test_file = test_dir / "test_script.py"

        print("\n" + "=" * 80)
        print(f"TEST {i}/{len(messaging_tests)}: {test_id}")
        print("=" * 80)

        start_time = time.time()

        # Run test
        cmd = f'python -m pytest "{test_file}" -v -s --tb=short'

        try:
            result = subprocess.run(
                cmd,
                shell=True,
                capture_output=True,
                text=True,
                timeout=300  # 5 minutes per test
            )

            duration = time.time() - start_time

            # Check result
            if result.returncode == 0:
                print(f"\n[PASSED] {test_id} - Duration: {duration:.1f}s")
                results["passed"] += 1
                results["test_results"].append({
                    "test_id": test_id,
                    "status": "PASSED",
                    "duration": duration
                })
            else:
                print(f"\n[FAILED] {test_id} - Duration: {duration:.1f}s")
                results["failed"] += 1
                results["test_results"].append({
                    "test_id": test_id,
                    "status": "FAILED",
                    "duration": duration
                })

                # Print failure info
                if "FAILED" in result.stdout:
                    print("\nFailure details:")
                    lines = result.stdout.split('\n')
                    for line in lines:
                        if "FAILED" in line or "ERROR" in line or "AssertionError" in line:
                            print(f"  {line}")

        except subprocess.TimeoutExpired:
            print(f"\n[TIMEOUT] {test_id} - Exceeded 5 minutes")
            results["errors"] += 1
            results["test_results"].append({
                "test_id": test_id,
                "status": "TIMEOUT",
                "duration": 300
            })

        except Exception as e:
            print(f"\n[ERROR] {test_id} - {e}")
            results["errors"] += 1
            results["test_results"].append({
                "test_id": test_id,
                "status": "ERROR",
                "duration": 0
            })

        # Small delay between tests
        time.sleep(2)

    # Final summary
    print("\n\n" + "=" * 80)
    print("MESSAGING TESTS COMPLETE")
    print("=" * 80)
    print(f"Total:   {results['total']}")
    print(f"Passed:  {results['passed']}")
    print(f"Failed:  {results['failed']}")
    print(f"Errors:  {results['errors']}")
    print(f"Pass Rate: {results['passed']/results['total']*100:.1f}%")
    print("=" * 80)

    # Print individual results
    print("\nIndividual Test Results:")
    print("-" * 80)
    for test in results["test_results"]:
        status_symbol = "✅" if test["status"] == "PASSED" else "❌"
        print(f"{status_symbol} {test['test_id']:20s} - {test['status']:8s} ({test['duration']:.1f}s)")

    # Save results
    with open("results/messaging_tests_summary.json", "w") as f:
        json.dump(results, f, indent=2)

    print("\n" + "=" * 80)
    print("Results saved to: results/messaging_tests_summary.json")
    print("=" * 80 + "\n")

    return results


if __name__ == "__main__":
    run_messaging_tests()
