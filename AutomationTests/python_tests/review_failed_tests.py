"""
Review Failed Tests - Generate Summary Report
Helps identify which failed tests need manual review
Created: February 12, 2026
"""

import os
from pathlib import Path

def review_failed_tests():
    """Generate summary of all failed tests for review"""

    failed_dir = Path("results/Failed")

    # Get all test case folders (exclude markdown files)
    failed_folders = sorted([
        d for d in failed_dir.iterdir()
        if d.is_dir()
    ])

    if not failed_folders:
        print("\nNo failed test folders found!")
        print("All tests passed! ✅\n")
        return

    print("\n" + "=" * 70)
    print("FAILED TESTS REVIEW REPORT")
    print("=" * 70)
    print(f"Total failed tests: {len(failed_folders)}")
    print("=" * 70 + "\n")

    print("According to CLAUDE.md guidelines, you should:")
    print("1. Review screenshots in each folder")
    print("2. Check if the feature actually works (visual evidence)")
    print("3. If feature works, move to Passed/ and update TEST_REPORT.md")
    print("4. If feature is broken, create BUG_REPORT.md\n")
    print("=" * 70 + "\n")

    # Categorize by test type
    categories = {
        'Signup': [],
        'Dashboard': [],
        'Tour': [],
        'Onboarding': []
    }

    for folder in failed_folders:
        test_id = folder.name
        if 'SIGNUP' in test_id:
            categories['Signup'].append(test_id)
        elif 'DASH' in test_id:
            categories['Dashboard'].append(test_id)
        elif 'TOUR' in test_id:
            categories['Tour'].append(test_id)
        elif 'OB' in test_id:
            categories['Onboarding'].append(test_id)

    # Print by category
    for category, tests in categories.items():
        if tests:
            print(f"\n{category} Tests ({len(tests)}):")
            print("-" * 70)
            for test_id in tests:
                folder = failed_dir / test_id
                files = list(folder.glob("*.png"))
                print(f"  [FOLDER] {test_id}")
                print(f"     Location: results/Failed/{test_id}/")
                print(f"     Screenshots: {len(files)}")
                for file in files:
                    size_kb = file.stat().st_size / 1024
                    print(f"       - {file.name} ({size_kb:.1f} KB)")
                print()

    # Generate review checklist
    print("\n" + "=" * 70)
    print("REVIEW CHECKLIST")
    print("=" * 70 + "\n")

    for i, folder in enumerate(failed_folders, 1):
        test_id = folder.name
        print(f"{i:2d}. [ ] {test_id}")
        print(f"       Review: results/Failed/{test_id}/*_FAILED.png")
        print(f"       Decision: PASS ☐  |  FAIL ☐")
        print()

    # Print commands to move to Passed if needed
    print("\n" + "=" * 70)
    print("QUICK COMMANDS - If test should be PASSED:")
    print("=" * 70 + "\n")

    print("# Move individual test to Passed folder:")
    for folder in failed_folders[:3]:
        test_id = folder.name
        print(f'python -c "import shutil; shutil.move(\'results/Failed/{test_id}\', \'results/Passed/{test_id}\')"')

    if len(failed_folders) > 3:
        print(f"# ... and {len(failed_folders) - 3} more")

    print("\n" + "=" * 70)
    print("IMPORTANT: Review evidence BEFORE moving!")
    print("=" * 70 + "\n")

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Total failed tests to review: {len(failed_folders)}")
    print(f"  - Signup tests:     {len(categories['Signup'])}")
    print(f"  - Dashboard tests:  {len(categories['Dashboard'])}")
    print(f"  - Tour tests:       {len(categories['Tour'])}")
    print(f"  - Onboarding tests: {len(categories['Onboarding'])}")
    print("\nNext steps:")
    print("1. Open each screenshot and review the visual evidence")
    print("2. Determine if the failure is real or a false negative")
    print("3. Move to Passed/ or create BUG_REPORT.md accordingly")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    # Change to python_tests directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)

    # Run review
    review_failed_tests()
