"""
Test Case: TC_SIGNUP_005
Title: Verify Email field accepts valid email formats
Priority: High
Type: Positive
"""

import pytest
import json
import time
from pathlib import Path


@pytest.mark.high
@pytest.mark.validation
def test_tc_signup_005(page, signup_page, base_url):
    """TC_SIGNUP_005: Email field accepts valid formats"""

    print("\n" + "="*70)
    print("TEST: TC_SIGNUP_005 - Email Accepts Valid Formats")
    print("="*70)

    try:
        test_data_path = Path("test_data/valid_signup_data.json")
        with open(test_data_path) as f:
            test_data = json.load(f)

        valid_email = test_data["valid_emails"][0]

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

        print(f"\n[STEP] Entering valid email: {valid_email}")
        signup_page.fill_email(valid_email)
        signup_page.click_outside()
        time.sleep(1)

        entered_email = signup_page.get_email_value()
        assert entered_email == valid_email, "Email not retained"
        print("[PASS] Email accepted and retained")

        has_error = signup_page.is_error_displayed()
        assert not has_error, "Unexpected error for valid email"
        print("[PASS] No error message displayed")

        page.screenshot(path="results/TC_SIGNUP_005_PASSED.png", full_page=True)

        print("\n[PASS] TEST PASSED: TC_SIGNUP_005")
        print(f"[EMAIL] Valid email accepted: {valid_email}\n")

    except Exception as e:
        page.screenshot(path="results/TC_SIGNUP_005_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        raise


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
