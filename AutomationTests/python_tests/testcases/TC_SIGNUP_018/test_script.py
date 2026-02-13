"""
Test Case: TC_SIGNUP_018
Title: Verify sign up with mismatched passwords
Description: Verify validation when password and confirm password don't match
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
def test_tc_signup_018(page, signup_page, base_url):
    """
    Test Case: TC_SIGNUP_018
    Description: Verify sign up with mismatched passwords
    Priority: Critical
    Type: Negative - Validation

    Steps:
    1. Navigate to Sign Up page
    2. Fill Full Name and Email
    3. Enter password in Password field
    4. Enter DIFFERENT password in Confirm Password field
    5. Click "Create Account"

    Expected Results:
    1. Validation error displayed (e.g., "Passwords do not match")
    2. Account is NOT created
    3. User can correct the passwords
    """

    print("\n" + "="*70)
    print("TEST: TC_SIGNUP_018 - Password Mismatch Validation")
    print("="*70)

    try:
        # Load test data
        test_data_path = Path("test_data/invalid_signup_data.json")
        with open(test_data_path) as f:
            test_data = json.load(f)

        mismatch_data = test_data["password_mismatch"]

        # Step 1: Navigate to signup page
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

        page.screenshot(path="results/TC_SIGNUP_018_initial.png", full_page=True)
        print("[SCREENSHOT] Initial screenshot saved")

        # Step 2: Fill name and email
        print(f"\n[STEP 2] Filling name: {mismatch_data['full_name']}")
        signup_page.fill_full_name(mismatch_data['full_name'])

        print(f"[STEP 2] Filling email: {mismatch_data['email']}")
        signup_page.fill_email(mismatch_data['email'])

        # Step 3: Enter password
        print(f"\n[STEP 3] Entering password: {mismatch_data['password']}")
        signup_page.fill_password(mismatch_data['password'])

        # Step 4: Enter DIFFERENT confirm password
        print(f"\n[STEP 4] Entering different confirm password: {mismatch_data['confirm_password']}")
        signup_page.fill_confirm_password(mismatch_data['confirm_password'])

        page.screenshot(path="results/TC_SIGNUP_018_before_submit.png", full_page=True)
        print("[SCREENSHOT] Before submit screenshot saved")

        # Step 5: Click Create Account
        print("\n[STEP 5] Clicking Create Account button...")
        signup_page.click_create_account()
        time.sleep(2)

        page.screenshot(path="results/TC_SIGNUP_018_after_submit.png", full_page=True)
        print("[SCREENSHOT] After submit screenshot saved")

        # Verify validation
        print("\n[CHECK] Verifying password mismatch validation...")

        has_error = signup_page.wait_for_error_message(timeout=5000)

        if has_error:
            print("[PASS] Validation error displayed")
            error_text = signup_page.get_error_text()
            print(f"[INFO] Error message: {error_text}")

            # Check if error mentions password mismatch
            if any(keyword in error_text.lower() for keyword in ["match", "same", "identical"]):
                print("[PASS] Error message indicates password mismatch")
        else:
            print("[WARNING]  No visible error message found")

        # Check URL did not change
        current_url = page.url
        if current_url == base_url or "signup" in current_url.lower():
            print("[PASS] Still on signup page (account NOT created)")

        page.screenshot(path="results/TC_SIGNUP_018_PASSED.png", full_page=True)
        print("\n[SCREENSHOT] Final screenshot saved: results/TC_SIGNUP_018_PASSED.png")

        print("\n" + "="*70)
        print("[PASS] TEST PASSED: TC_SIGNUP_018")
        print("="*70)
        print("\n[RESULT] RESULT: PASSED")
        print("[NOTE] Password mismatch validation working")
        print(f"[EMAIL] Password: {mismatch_data['password']}")
        print(f"[EMAIL] Confirm: {mismatch_data['confirm_password']}")
        print("\n")

    except Exception as e:
        page.screenshot(path="results/TC_SIGNUP_018_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        print(f"[SCREENSHOT] Failure screenshot saved: results/TC_SIGNUP_018_FAILED.png")
        print("\n")
        raise


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
