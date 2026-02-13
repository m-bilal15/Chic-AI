"""
Fix syntax errors in failed onboarding test scripts
Replace unescaped quotes with escaped quotes
"""

import json
from pathlib import Path


def fix_test_script(test_id):
    """Fix syntax errors in a test script"""

    test_file = Path(f"testcases/{test_id}/test_script.py")

    if not test_file.exists():
        return False

    try:
        with open(test_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Fix the common syntax error - quotes in print statements
        # Replace pattern: print("TEST: TC_XXX - Description with "quotes"...")
        # With: print("TEST: TC_XXX - Description with \\"quotes\\"...")

        import re

        # Fix print statements with embedded quotes
        # Pattern: print("... "word" ...")
        # This is a complex fix, so let's replace problematic descriptions

        # Simpler approach: Use single quotes for outer string
        content = content.replace('print("TEST:', "print('TEST:")
        content = content.replace('print("[PASS]', "print('[PASS]")
        content = content.replace('print("[FAIL]', "print('[FAIL]")
        content = content.replace('print("[WARNING]', "print('[WARNING]")

        # Or escape internal quotes
        lines = content.split('\n')
        fixed_lines = []

        for line in lines:
            # If line has print("TEST: and contains quotes in description
            if 'print("TEST:' in line and line.count('"') > 2:
                # Use triple quotes or escape
                line = line.replace('print("TEST:', 'print("""TEST:')
                if not line.endswith('")'):
                    line = line.rstrip() + '""")'
                else:
                    line = line.replace('")', '""")')

            fixed_lines.append(line)

        content = '\n'.join(fixed_lines)

        # Write back
        with open(test_file, 'w', encoding='utf-8') as f:
            f.write(content)

        return True

    except Exception as e:
        print(f"[ERROR] Could not fix {test_id}: {e}")
        return False


def fix_all_failed_tests():
    """Fix all 16 failed test scripts"""

    failed_tests = [
        "TC_OB_004", "TC_OB_005", "TC_OB_010",
        "TC_OB_S2_008", "TC_OB_S3_009",
        "TC_OB_S4_007", "TC_OB_S4_008", "TC_OB_S4_013",
        "TC_OB_S5_007", "TC_OB_S5_008", "TC_OB_S5_009",
        "TC_OB_S5_010", "TC_OB_S5_011", "TC_OB_S5_012",
        "TC_OB_S5_016", "TC_OB_S5_017"
    ]

    print("="*70)
    print("FIXING FAILED TEST SCRIPTS")
    print("="*70)
    print(f"Tests to fix: {len(failed_tests)}\n")

    fixed = 0

    for test_id in failed_tests:
        print(f"Fixing {test_id}...", end=" ")
        if fix_test_script(test_id):
            print("[FIXED]")
            fixed += 1
        else:
            print("[FAILED]")

    print("\n" + "="*70)
    print(f"Fixed: {fixed}/{len(failed_tests)}")
    print("="*70 + "\n")


if __name__ == "__main__":
    fix_all_failed_tests()
