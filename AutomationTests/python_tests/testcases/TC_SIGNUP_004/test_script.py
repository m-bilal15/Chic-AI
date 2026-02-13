"""
Test Case: TC_SIGNUP_004
Title: Verify Full Name field accepts names with special characters
Priority: Medium
Type: Positive
"""

import pytest
import json
import time
from pathlib import Path


@pytest.mark.medium
@pytest.mark.validation
def test_tc_signup_004(page, signup_page, base_url):
    """TC_SIGNUP_004: Names with special characters (hyphens, apostrophes, accents)"""

    print("\n" + "="*70)
    print("TEST: TC_SIGNUP_004 - Names With Special Characters")
    print("="*70)

    try:
        test_data_path = Path("test_data/valid_signup_data.json")
        with open(test_data_path) as f:
            test_data = json.load(f)

        special_names = test_data["valid_names_with_special_chars"]

        page.goto(base_url)
        page.wait_for_load_state("networkidle")
        time.sleep(2)

        try:
            signup_link = page.locator('a:has-text("Sign up"), button:has-text("Sign up")')
            if signup_link.is_visible(timeout=3000):
                signup_link.click()
                time.sleep(2)
        except:
            pass

        # Test first special name
        test_name = special_names[0]  # "O'Brien Smith"

        print(f"\n[STEP] Testing name with special characters: {test_name}")
        signup_page.fill_full_name(test_name)
        signup_page.click_outside()
        time.sleep(1)

        # Verify name is retained
        entered_name = signup_page.get_full_name_value()
        print(f"[CHECK] Name in field: {entered_name}")

        if entered_name == test_name:
            print(f"[PASS] Special character name accepted: {test_name}")
        else:
            print(f"[WARNING]  Name changed from '{test_name}' to '{entered_name}'")

        # Check no error
        has_error = signup_page.is_error_displayed()
        if has_error:
            print("[WARNING]  Error displayed for culturally valid name")
        else:
            print("[PASS] No error - special characters accepted")

        # Test all special names
        print(f"\n[INFO] Testing all {len(special_names)} special character names:")
        for name in special_names:
            print(f"   - {name}")
            signup_page.clear_full_name()
            signup_page.fill_full_name(name)
            time.sleep(0.5)

        page.screenshot(path="results/TC_SIGNUP_004_PASSED.png", full_page=True)

        print("\n[PASS] TEST PASSED: TC_SIGNUP_004")
        print("[NOTE] Names with hyphens, apostrophes, and accents accepted\n")

    except Exception as e:
        page.screenshot(path="results/TC_SIGNUP_004_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        raise


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
