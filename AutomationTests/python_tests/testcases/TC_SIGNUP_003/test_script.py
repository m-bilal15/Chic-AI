"""
Test Case: TC_SIGNUP_003
Title: Verify Full Name field accepts valid names
Priority: High
Type: Positive
"""

import pytest
import json
import time
from pathlib import Path


@pytest.mark.high
@pytest.mark.validation
def test_tc_signup_003(page, signup_page, base_url):
    """TC_SIGNUP_003: Full Name field accepts valid names"""

    print("\n" + "="*70)
    print("TEST: TC_SIGNUP_003 - Full Name Accepts Valid Names")
    print("="*70)

    try:
        test_data_path = Path("test_data/valid_signup_data.json")
        with open(test_data_path) as f:
            test_data = json.load(f)

        valid_name = test_data["valid_names"][0]  # "John Smith"

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

        page.screenshot(path="results/TC_SIGNUP_003_initial.png", full_page=True)

        print(f"\n[STEP] Entering valid name: {valid_name}")
        signup_page.fill_full_name(valid_name)

        print("[STEP] Clicking outside to trigger blur/validation")
        signup_page.click_outside()
        time.sleep(1)

        # Verify name is retained
        entered_name = signup_page.get_full_name_value()
        print(f"[CHECK] Name in field: {entered_name}")

        assert entered_name == valid_name, f"Name not retained: {entered_name}"
        print("[PASS] Name accepted and retained")

        # Check no error displayed
        has_error = signup_page.is_error_displayed()
        if has_error:
            print("[WARNING]  Unexpected error displayed")
        else:
            print("[PASS] No error message displayed")

        page.screenshot(path="results/TC_SIGNUP_003_PASSED.png", full_page=True)

        print("\n[PASS] TEST PASSED: TC_SIGNUP_003")
        print(f"[NOTE] Valid name accepted: {valid_name}\n")

    except Exception as e:
        page.screenshot(path="results/TC_SIGNUP_003_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        raise


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
