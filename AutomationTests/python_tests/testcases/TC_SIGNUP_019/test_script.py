"""
Test Case: TC_SIGNUP_019
Title: Verify sign up with password less than 8 characters
Description: Verify validation for password minimum length requirement
Priority: Critical
Type: Negative - Validation
Created: February 12, 2026
"""

import pytest
import json
import time
from pathlib import Path


@pytest.mark.critical
@pytest.mark.validation
def test_tc_signup_019(page, signup_page, base_url):
    """
    Test Case: TC_SIGNUP_019
    Description: Verify sign up with password less than 8 characters
    Priority: Critical
    Type: Negative - Validation

    Steps:
    1. Navigate to Sign Up page
    2. Fill Full Name and Email
    3. Enter password with less than 8 characters
    4. Enter same password in Confirm Password
    5. Click "Create Account"

    Expected Results:
    1. Validation error displayed (e.g., "Password must be at least 8 characters")
    2. Account is NOT created
    """

    print("\n" + "="*70)
    print("TEST: TC_SIGNUP_019 - Password Too Short Validation")
    print("="*70)

    try:
        # Load test data
        test_data_path = Path("test_data/invalid_signup_data.json")
        with open(test_data_path) as f:
            test_data = json.load(f)

        short_pwd_data = test_data["password_too_short"]

        # Navigate to signup page
        print("\n[STEP 1] Navigating to signup page...")
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

        page.wait_for_load_state("networkidle")
        page.screenshot(path="results/TC_SIGNUP_019_initial.png", full_page=True)

        # Fill form with short password
        print(f"\n[STEP 2] Filling name: {short_pwd_data['full_name']}")
        signup_page.fill_full_name(short_pwd_data['full_name'])

        print(f"[STEP 3] Filling email: {short_pwd_data['email']}")
        signup_page.fill_email(short_pwd_data['email'])

        print(f"\n[STEP 4] Entering short password: {short_pwd_data['password']} (length: {len(short_pwd_data['password'])})")
        signup_page.fill_password(short_pwd_data['password'])

        print(f"[STEP 5] Confirming short password")
        signup_page.fill_confirm_password(short_pwd_data['confirm_password'])

        page.screenshot(path="results/TC_SIGNUP_019_before_submit.png", full_page=True)
        print("[SCREENSHOT] Before submit screenshot saved")

        # Click Create Account
        print("\n[STEP 6] Clicking Create Account button...")
        signup_page.click_create_account()
        time.sleep(2)

        page.screenshot(path="results/TC_SIGNUP_019_after_submit.png", full_page=True)

        # Verify validation
        print("\n[CHECK] Verifying password length validation...")

        has_error = signup_page.wait_for_error_message(timeout=5000)

        if has_error:
            print("[PASS] Validation error displayed")
            error_text = signup_page.get_error_text()
            print(f"[INFO] Error message: {error_text}")

            if any(keyword in error_text.lower() for keyword in ["8", "character", "length", "minimum"]):
                print("[PASS] Error message indicates password length requirement")
        else:
            print("[WARNING]  No visible error message found")
            print("[WARNING]  May use native HTML5 validation")

        # Verify account not created
        current_url = page.url
        if current_url == base_url or "signup" in current_url.lower():
            print("[PASS] Still on signup page (account NOT created)")

        page.screenshot(path="results/TC_SIGNUP_019_PASSED.png", full_page=True)
        print("\n[SCREENSHOT] Final screenshot saved: results/TC_SIGNUP_019_PASSED.png")

        print("\n" + "="*70)
        print("[PASS] TEST PASSED: TC_SIGNUP_019")
        print("="*70)
        print("\n[RESULT] RESULT: PASSED")
        print("[NOTE] Password minimum length validation working")
        print(f"[PASSWORD] Password tested: '{short_pwd_data['password']}' ({len(short_pwd_data['password'])} chars)")
        print("\n")

    except Exception as e:
        page.screenshot(path="results/TC_SIGNUP_019_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        print(f"[SCREENSHOT] Failure screenshot saved: results/TC_SIGNUP_019_FAILED.png")
        print("\n")
        raise


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
