"""
Test Runner - Executes All 50 Test Cases One by One
Organizes results into Passed/Failed folders with artifacts
"""

import os
import sys
import shutil
import json
from pathlib import Path
from datetime import datetime
import subprocess

# Paths
TESTCASES_DIR = Path('./testcases')
RESULTS_DIR = Path('./results')
PASSED_DIR = RESULTS_DIR / 'Passed'
FAILED_DIR = RESULTS_DIR / 'Failed'

# Clean and create results directories
if RESULTS_DIR.exists():
    shutil.rmtree(RESULTS_DIR)
RESULTS_DIR.mkdir(exist_ok=True)
PASSED_DIR.mkdir(exist_ok=True)
FAILED_DIR.mkdir(exist_ok=True)

# Get all test case folders
test_folders = sorted([f for f in TESTCASES_DIR.iterdir() if f.is_dir()])

print("=" * 80)
print("CHIC LOGIN PAGE - PYTHON TEST EXECUTION")
print("=" * 80)
print(f"Total Test Cases: {len(test_folders)}")
print(f"Execution Mode: VISIBLE (Browser opens, 2-second delays)")
print("=" * 80)
print()

# Track results
results = {
    'total': len(test_folders),
    'passed': 0,
    'failed': 0,
    'tests': []
}

# Execute each test
for idx, test_folder in enumerate(test_folders, 1):
    tc_id = test_folder.name
    test_script = test_folder / 'test_script.py'

    if not test_script.exists():
        print(f"[{idx}/{len(test_folders)}] SKIP: {tc_id} - No test_script.py found")
        continue

    print(f"\n[{idx}/{len(test_folders)}] Executing: {tc_id}")
    print("-" * 80)

    start_time = datetime.now()

    try:
        # Execute test script from python_tests directory (not from test folder)
        result = subprocess.run(
            [sys.executable, str(test_script.absolute())],
            capture_output=True,
            text=True,
            timeout=120,
            encoding='utf-8',
            errors='replace'
        )

        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()

        # Check if test passed
        if result.returncode == 0 and "PASSED" in result.stdout:
            status = "PASSED"
            results['passed'] += 1
            dest_folder = PASSED_DIR / tc_id
            print(f"PASSED: {tc_id} ({duration:.2f}s)")
        else:
            status = "FAILED"
            results['failed'] += 1
            dest_folder = FAILED_DIR / tc_id
            print(f"FAILED: {tc_id} ({duration:.2f}s)")

        # Create destination folder
        dest_folder.mkdir(exist_ok=True)

        # Save test output
        output_file = dest_folder / 'test_output.txt'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"Test Case: {tc_id}\n")
            f.write(f"Status: {status}\n")
            f.write(f"Duration: {duration:.2f}s\n")
            f.write(f"Executed: {start_time.isoformat()}\n")
            f.write("\n" + "=" * 80 + "\n")
            f.write("STDOUT:\n")
            f.write(result.stdout)
            f.write("\n" + "=" * 80 + "\n")
            if result.stderr:
                f.write("STDERR:\n")
                f.write(result.stderr)

        # Copy video/screenshots from results to dest folder
        video_dir = RESULTS_DIR / tc_id
        if video_dir.exists():
            for artifact in video_dir.iterdir():
                try:
                    shutil.copy2(artifact, dest_folder / artifact.name)
                except:
                    pass

        # Create test report
        report_file = dest_folder / 'TEST_REPORT.md'
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(f"# {tc_id}\n\n")
            f.write(f"## Status: {status}\n\n")
            f.write(f"## Duration: {duration:.2f}s\n\n")
            f.write(f"## Executed: {start_time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"## Test Output:\n```\n{result.stdout}\n```\n")
            if status == "FAILED" and result.stderr:
                f.write(f"\n## Error:\n```\n{result.stderr}\n```\n")

        # Record result
        results['tests'].append({
            'id': tc_id,
            'status': status,
            'duration': f'{duration:.2f}s'
        })

    except subprocess.TimeoutExpired:
        results['failed'] += 1
        results['tests'].append({
            'id': tc_id,
            'status': 'TIMEOUT',
            'duration': '120s'
        })
        print(f"TIMEOUT: {tc_id}")

    except Exception as e:
        results['failed'] += 1
        results['tests'].append({
            'id': tc_id,
            'status': 'ERROR',
            'duration': '0s'
        })
        print(f"ERROR: {tc_id} - {str(e)}")

# Save summary
summary_file = RESULTS_DIR / 'SUMMARY.json'
with open(summary_file, 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2)

# Create summary markdown
pass_rate = (results['passed'] / results['total'] * 100) if results['total'] > 0 else 0
summary_md = f"""# Test Execution Summary

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Results

- **Total Tests:** {results['total']}
- **Passed:** {results['passed']}
- **Failed:** {results['failed']}
- **Pass Rate:** {pass_rate:.1f}%

## Folders

- Passed Tests: `results/Passed/` ({results['passed']} folders)
- Failed Tests: `results/Failed/` ({results['failed']} folders)

## Each Test Folder Contains:

1. test_output.txt - Console output
2. TEST_REPORT.md - Readable report
3. video.webm - Video recording (if test ran)
4. Screenshots - Visual evidence
"""

with open(RESULTS_DIR / 'SUMMARY.md', 'w', encoding='utf-8') as f:
    f.write(summary_md)

# Print final summary
print("\n" + "=" * 80)
print("TEST EXECUTION SUMMARY")
print("=" * 80)
print(f"Total Tests:  {results['total']}")
print(f"PASSED:       {results['passed']} ({pass_rate:.1f}%)")
print(f"FAILED:       {results['failed']} ({100-pass_rate:.1f}%)")
print("=" * 80)
print(f"\nResults Location:")
print(f"  Passed: {PASSED_DIR.absolute()} ({results['passed']} folders)")
print(f"  Failed: {FAILED_DIR.absolute()} ({results['failed']} folders)")
print("\nDone!")
