"""
Rename all test_script.py files to unique names for pytest compatibility
This fixes the 'import file mismatch' error
"""

import os
import shutil
from pathlib import Path


def rename_test_files():
    """Rename test_script.py to test_signup_XXX.py"""

    testcases_dir = Path("testcases")

    if not testcases_dir.exists():
        print("ERROR: testcases directory not found!")
        return

    renamed_count = 0
    errors = []

    # Find all test_script.py files
    for test_dir in sorted(testcases_dir.iterdir()):
        if test_dir.is_dir() and test_dir.name.startswith("TC_SIGNUP"):
            test_file = test_dir / "test_script.py"

            if test_file.exists():
                # Extract test case number (e.g., TC_SIGNUP_001 -> 001)
                test_id = test_dir.name  # e.g., TC_SIGNUP_001

                # New filename
                new_name = f"test_{test_id.lower()}.py"  # e.g., test_tc_signup_001.py
                new_file = test_dir / new_name

                try:
                    # Rename file
                    shutil.move(str(test_file), str(new_file))
                    print(f"✅ Renamed: {test_dir.name}/test_script.py -> {new_name}")
                    renamed_count += 1
                except Exception as e:
                    errors.append(f"❌ Error renaming {test_file}: {e}")

    print(f"\n{'='*70}")
    print(f"Renaming Complete!")
    print(f"{'='*70}")
    print(f"✅ Successfully renamed: {renamed_count} files")

    if errors:
        print(f"❌ Errors encountered: {len(errors)}")
        for error in errors:
            print(f"   {error}")
    else:
        print("✅ No errors!")

    print(f"\n{'='*70}")
    print("Next Steps:")
    print("='*70}")
    print("1. Run: pytest -m critical -v -s")
    print("2. Or:  pytest testcases/TC_SIGNUP_*/test_tc_signup_*.py -v")
    print(f"{'='*70}\n")


if __name__ == "__main__":
    rename_test_files()
