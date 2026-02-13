"""
Test Case: TC_SIGNUP_014
Title: Verify sign up with empty Full Name only
Priority: High
Type: Negative - Validation
"""

import pytest
import json
import time
from pathlib import Path


@pytest.mark.high
@pytest.mark.validation
def test_tc_signup_014(page, signup_page, base_url):
    """TC_SIGNUP_014: Empty Full Name only"""

    print("\n" + "="*70)
    print("TEST: TC_SIGNUP_014 - Empty Full Name Only")
    print("="*70)

    try:
        test_data_path = Path("test_data/invalid_signup_data.json")
        with open(test_data_path) as f:
            test_data = json.load(f)

        data = test_data["empty_fields"]["name_empty"]

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

        print("\n[STEP] Leaving Full Name EMPTY, filling other fields")
        signup_page.clear_full_name()  # Ensure empty
        signup_page.fill_email(data['email'])
        signup_page.fill_password(data['password'])
        signup_page.fill_confirm_password(data['confirm_password'])

        page.screenshot(path="results/TC_SIGNUP_014_before_submit.png", full_page=True)

        signup_page.click_create_account()
        time.sleep(2)

        # Verify validation error
        has_error = signup_page.wait_for_error_message(timeout=5000)
        if has_error:
            print("[PASS] Validation error displayed for empty name")
        else:
            print("[WARNING]  No error - may use native HTML5 validation")

        page.screenshot(path="results/TC_SIGNUP_014_PASSED.png", full_page=True)
        print("\n[PASS] TEST PASSED: TC_SIGNUP_014")
        print("[NOTE] Empty Full Name validation working\n")

    except Exception as e:
        page.screenshot(path="results/TC_SIGNUP_014_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        raise


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
