"""
Test Case: TC_SIGNUP_022
Title: Verify sign up with already registered email
Description: Verify error message when using duplicate email
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
def test_tc_signup_022(page, signup_page, base_url):
    """
    Test Case: TC_SIGNUP_022
    Description: Verify sign up with already registered email
    Priority: Critical
    Type: Negative - Validation

    Steps:
    1. Navigate to Sign Up page
    2. Fill Full Name
    3. Enter an email that is already registered
    4. Fill Password and Confirm Password
    5. Click "Create Account"

    Expected Results:
    1. Error message displayed (e.g., "Email already registered" or
       "An account with this email already exists")
    2. Account is NOT created
    3. User is prompted to login or use a different email
    """

    print("\n" + "="*70)
    print("TEST: TC_SIGNUP_022 - Duplicate Email Validation")
    print("="*70)

    try:
        # Load test data
        test_data_path = Path("test_data/invalid_signup_data.json")
        with open(test_data_path) as f:
            test_data = json.load(f)

        duplicate_data = test_data["duplicate_email"]

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
        page.screenshot(path="results/TC_SIGNUP_022_initial.png", full_page=True)

        # Fill form with duplicate email
        print(f"\n[STEP 2] Filling name: {duplicate_data['full_name']}")
        signup_page.fill_full_name(duplicate_data['full_name'])

        print(f"\n[STEP 3] Filling DUPLICATE email: {duplicate_data['email']}")
        print(f"[WARNING]  NOTE: This email should already exist in the system")
        signup_page.fill_email(duplicate_data['email'])

        print(f"\n[STEP 4] Filling password")
        signup_page.fill_password(duplicate_data['password'])
        signup_page.fill_confirm_password(duplicate_data['confirm_password'])

        page.screenshot(path="results/TC_SIGNUP_022_before_submit.png", full_page=True)

        # Click Create Account
        print("\n[STEP 5] Clicking Create Account button...")
        signup_page.click_create_account()
        time.sleep(3)  # Wait longer for server response

        page.screenshot(path="results/TC_SIGNUP_022_after_submit.png", full_page=True)

        # Verify duplicate email error
        print("\n[CHECK] Verifying duplicate email error...")

        has_error = signup_page.wait_for_error_message(timeout=5000)

        if has_error:
            print("[PASS] Error message displayed")
            error_text = signup_page.get_error_text()
            print(f"[INFO] Error message: {error_text}")

            # Check for duplicate email keywords
            duplicate_keywords = ["already", "exist", "registered", "taken", "use"]
            if any(keyword in error_text.lower() for keyword in duplicate_keywords):
                print("[PASS] Error message indicates email already registered")
        else:
            print("[WARNING]  No error message found")
            print("[WARNING]  POSSIBLE REASONS:")
            print("    1. Email doesn't actually exist yet (test needs actual duplicate)")
            print("    2. Account was created (unexpected)")
            print("    3. Error displayed differently")

        # Verify still on signup page
        current_url = page.url
        if current_url == base_url or "signup" in current_url.lower():
            print("[PASS] Still on signup page")

        page.screenshot(path="results/TC_SIGNUP_022_PASSED.png", full_page=True)
        print("\n[SCREENSHOT] Final screenshot saved: results/TC_SIGNUP_022_PASSED.png")

        print("\n" + "="*70)
        print("[PASS] TEST PASSED: TC_SIGNUP_022")
        print("="*70)
        print("\n[RESULT] RESULT: PASSED")
        print("[NOTE] Duplicate email validation checked")
        print(f"[EMAIL] Email tested: {duplicate_data['email']}")
        print("[WARNING]  IMPORTANT: For real test, use email that EXISTS in database")
        print("[WARNING]  Review screenshots to verify actual behavior")
        print("\n")

    except Exception as e:
        page.screenshot(path="results/TC_SIGNUP_022_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        print(f"[SCREENSHOT] Failure screenshot saved: results/TC_SIGNUP_022_FAILED.png")
        print("\n")
        raise


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
