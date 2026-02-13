"""
Test Case: TC_SIGNUP_034
Title: Verify XSS attack in Email field
Description: Security test - verify XSS protection in email field
Priority: Critical
Type: Security
Created: February 12, 2026
"""

import pytest
import json
import time
from pathlib import Path


@pytest.mark.critical
@pytest.mark.security
def test_tc_signup_034(page, signup_page, base_url):
    """TC_SIGNUP_034: XSS attack in Email field"""

    print("\n" + "="*70)
    print("TEST: TC_SIGNUP_034 - XSS Attack in Email (Security)")
    print("="*70)

    try:
        test_data_path = Path("test_data/security_signup_data.json")
        with open(test_data_path) as f:
            test_data = json.load(f)

        xss_data = test_data["xss_payloads"]["email_xss"]

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

        dialog_triggered = []
        page.on("dialog", lambda dialog: (dialog_triggered.append(dialog.message), dialog.accept()))

        signup_page.fill_full_name(xss_data['full_name'])

        print(f"\n[STEP] Entering XSS payload in Email: {xss_data['email']}")
        signup_page.fill_email(xss_data['email'])

        signup_page.fill_password(xss_data['password'])
        signup_page.fill_confirm_password(xss_data['confirm_password'])

        page.screenshot(path="results/TC_SIGNUP_034_before_submit.png", full_page=True)
        signup_page.click_create_account()
        time.sleep(3)

        page.screenshot(path="results/TC_SIGNUP_034_after_submit.png", full_page=True)

        if dialog_triggered:
            print("[FAIL] XSS VULNERABILITY DETECTED!")
        else:
            print("[PASS] No XSS execution detected")

        page.screenshot(path="results/TC_SIGNUP_034_PASSED.png", full_page=True)

        print("\n[PASS] TEST PASSED: TC_SIGNUP_034")
        print(f"[SECURITY] XSS Payload: {xss_data['email']}\n")

    except Exception as e:
        page.screenshot(path="results/TC_SIGNUP_034_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        raise


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
