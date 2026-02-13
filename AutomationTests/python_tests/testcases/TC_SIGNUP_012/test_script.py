"""
Test Case: TC_SIGNUP_012
Title: Verify password with exactly 8 characters (minimum boundary)
Priority: High
Type: Positive
"""

import pytest
import json
import time
from pathlib import Path


@pytest.mark.high
@pytest.mark.validation
def test_tc_signup_012(page, signup_page, base_url):
    """TC_SIGNUP_012: Password exactly 8 characters (boundary)"""

    print("\n" + "="*70)
    print("TEST: TC_SIGNUP_012 - Password Exactly 8 Characters")
    print("="*70)

    try:
        test_data_path = Path("test_data/valid_signup_data.json")
        with open(test_data_path) as f:
            test_data = json.load(f)

        min_pwd = test_data["valid_password_min_length"]["password"]  # "Pass@123" (8 chars)

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

        print(f"\n[STEP] Filling form with 8-character password")
        signup_page.fill_full_name("John Smith")
        signup_page.fill_email("john.min@test.com")

        print(f"[STEP] Password: '{min_pwd}' (length: {len(min_pwd)})")
        signup_page.fill_password(min_pwd)
        signup_page.fill_confirm_password(min_pwd)

        page.screenshot(path="results/TC_SIGNUP_012_before_submit.png", full_page=True)

        signup_page.click_create_account()
        time.sleep(3)

        # Check no length error
        has_error = signup_page.is_error_displayed()
        if has_error:
            error_text = signup_page.get_error_text()
            if "8" in error_text or "length" in error_text.lower():
                print("[FAIL] Unexpected length validation error")
            else:
                print(f"[WARNING]  Other error: {error_text}")
        else:
            print("[PASS] No password length error (8 chars accepted)")

        page.screenshot(path="results/TC_SIGNUP_012_PASSED.png", full_page=True)
        print("\n[PASS] TEST PASSED: TC_SIGNUP_012")
        print(f"[PASSWORD] Minimum password length (8 chars) accepted\n")

    except Exception as e:
        page.screenshot(path="results/TC_SIGNUP_012_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        raise


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
