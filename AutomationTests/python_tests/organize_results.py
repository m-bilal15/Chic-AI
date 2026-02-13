"""
Organize scattered PNG files into proper test case folders
Moves files from results/ to results/Passed/TC_XXX/ or results/Failed/TC_XXX/
Created: February 12, 2026
"""

import os
import shutil
import re
from pathlib import Path

def extract_test_id(filename):
    """
    Extract test case ID from filename
    Examples:
        TC_SIGNUP_001_PASSED.png -> TC_SIGNUP_001
        TC_DASH_001_initial.png -> TC_DASH_001
        TC_OB_S1_001_FAILED.png -> TC_OB_S1_001
    """
    # Match pattern: TC_XXX_XXX or TC_XXX
    match = re.match(r'(TC_[A-Z]+_[A-Z0-9]+)_', filename)
    if match:
        return match.group(1)

    match = re.match(r'(TC_[A-Z]+_\d+)_', filename)
    if match:
        return match.group(1)

    return None

def is_failed_test(filename):
    """Check if this is a failed test based on filename"""
    return '_FAILED' in filename

def organize_screenshots():
    """Organize all scattered PNG files into proper folders"""

    results_dir = Path("results")
    passed_dir = results_dir / "Passed"
    failed_dir = results_dir / "Failed"

    # Ensure base directories exist
    passed_dir.mkdir(exist_ok=True)
    failed_dir.mkdir(exist_ok=True)

    # Get all PNG files in results directory
    png_files = list(results_dir.glob("*.png"))

    if not png_files:
        print("No PNG files found in results directory")
        return

    print(f"\nFound {len(png_files)} PNG files to organize")
    print("=" * 70)

    # Statistics
    stats = {
        'moved': 0,
        'failed': 0,
        'skipped': 0,
        'passed': 0,
        'failed_tests': 0
    }

    # Process each PNG file
    for png_file in sorted(png_files):
        filename = png_file.name

        # Extract test case ID
        test_id = extract_test_id(filename)

        if not test_id:
            print(f"[SKIP] Could not extract test ID from: {filename}")
            stats['skipped'] += 1
            continue

        # Determine if passed or failed
        is_failed = is_failed_test(filename)

        # Determine target directory
        if is_failed:
            target_dir = failed_dir / test_id
            status = "FAILED"
            stats['failed_tests'] += 1
        else:
            target_dir = passed_dir / test_id
            status = "PASSED"
            stats['passed'] += 1

        # Create target directory if it doesn't exist
        target_dir.mkdir(parents=True, exist_ok=True)

        # Target file path
        target_file = target_dir / filename

        # Move file
        try:
            shutil.move(str(png_file), str(target_file))
            print(f"[MOVED] {filename:50s} -> {status}/{test_id}/")
            stats['moved'] += 1
        except Exception as e:
            print(f"[ERROR] Failed to move {filename}: {e}")
            stats['failed'] += 1

    # Print summary
    print("\n" + "=" * 70)
    print("ORGANIZATION COMPLETE")
    print("=" * 70)
    print(f"Total PNG files found:        {len(png_files)}")
    print(f"Successfully moved:           {stats['moved']}")
    print(f"  - To Passed/:               {stats['passed']}")
    print(f"  - To Failed/:               {stats['failed_tests']}")
    print(f"Failed to move:               {stats['failed']}")
    print(f"Skipped (no test ID):         {stats['skipped']}")
    print("=" * 70)

    # List organized folders
    print("\nOrganized test case folders:")
    print("-" * 70)

    passed_folders = sorted([d.name for d in passed_dir.iterdir() if d.is_dir()])
    failed_folders = sorted([d.name for d in failed_dir.iterdir() if d.is_dir()])

    if passed_folders:
        print(f"\nPassed/ ({len(passed_folders)} folders):")
        for folder in passed_folders[:10]:
            file_count = len(list((passed_dir / folder).glob("*.png")))
            print(f"  {folder}: {file_count} files")
        if len(passed_folders) > 10:
            print(f"  ... and {len(passed_folders) - 10} more folders")

    if failed_folders:
        print(f"\nFailed/ ({len(failed_folders)} folders):")
        for folder in failed_folders:
            file_count = len(list((failed_dir / folder).glob("*.png")))
            print(f"  {folder}: {file_count} files")

    print("\n" + "=" * 70)
    print("All screenshots are now organized in their respective folders!")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("RESULTS FOLDER ORGANIZATION TOOL")
    print("=" * 70)
    print("This script will organize scattered PNG files into proper folders")
    print("Following CLAUDE.md guidelines:")
    print("  - PASSED screenshots -> results/Passed/TC_XXX/")
    print("  - FAILED screenshots -> results/Failed/TC_XXX/")
    print("=" * 70 + "\n")

    # Change to python_tests directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)

    # Run organization
    organize_screenshots()
