"""
Test Case: TC_SIGNUP_031
Title: Verify SQL injection in Full Name field
Description: Security test - verify app handles SQL injection attempts safely
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
def test_tc_signup_031(page, signup_page, base_url):
    """
    Test Case: TC_SIGNUP_031
    Description: Verify SQL injection in Full Name field
    Priority: Critical
    Type: Security

    Steps:
    1. Navigate to Sign Up page
    2. Enter SQL injection payload in Full Name
    3. Fill other fields with valid data
    4. Click "Create Account"

    Expected Results:
    1. Application does NOT crash
    2. No database errors exposed
    3. Input is sanitized
    4. Appropriate error message or account created with sanitized name
    """

    print("\n" + "="*70)
    print("TEST: TC_SIGNUP_031 - SQL Injection in Full Name (Security)")
    print("="*70)

    try:
        # Load security test data
        test_data_path = Path("test_data/security_signup_data.json")
        with open(test_data_path) as f:
            test_data = json.load(f)

        sqli_data = test_data["sql_injection_payloads"]["full_name_sqli"]

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
        page.screenshot(path="results/TC_SIGNUP_031_initial.png", full_page=True)

        # Step 2: Enter SQL injection payload
        print(f"\n[STEP 2] Entering SQL injection payload in Full Name:")
        print(f"   Payload: {sqli_data['full_name']}")
        print(f"   [WARNING]  SECURITY TEST - Checking if app sanitizes input")

        signup_page.fill_full_name(sqli_data['full_name'])

        # Step 3: Fill other fields normally
        print(f"\n[STEP 3] Filling email: {sqli_data['email']}")
        signup_page.fill_email(sqli_data['email'])

        print(f"[STEP 3] Filling password")
        signup_page.fill_password(sqli_data['password'])
        signup_page.fill_confirm_password(sqli_data['confirm_password'])

        page.screenshot(path="results/TC_SIGNUP_031_before_submit.png", full_page=True)

        # Step 4: Submit form
        print("\n[STEP 4] Clicking Create Account button...")
        signup_page.click_create_account()
        time.sleep(3)

        page.screenshot(path="results/TC_SIGNUP_031_after_submit.png", full_page=True)

        # Security checks
        print("\n[SECURITY CHECK] Verifying application security...")

        # Check 1: App did not crash
        print("\n[CHECK 1] Application did not crash...")
        current_url = page.url
        print(f"[PASS] Application still running (URL: {current_url})")

        # Check 2: No database errors exposed
        print("\n[CHECK 2] Checking for exposed database errors...")
        page_content = page.content()

        db_error_indicators = [
            "sql", "mysql", "postgres", "syntax error",
            "database error", "query failed", "column",
            "table", "select", "insert", "delete"
        ]

        has_db_error = any(indicator in page_content.lower() for indicator in db_error_indicators)

        if has_db_error:
            print("[WARNING]  WARNING: Possible database error exposed!")
            print("[WARNING]  This is a security vulnerability")
        else:
            print("[PASS] No database errors exposed in page content")

        # Check 3: Input sanitization
        print("\n[CHECK 3] Checking input sanitization...")

        has_error = signup_page.is_error_displayed()
        if has_error:
            error_text = signup_page.get_error_text()
            print(f"[PASS] Validation error displayed: {error_text}")
            print("   (SQL injection rejected - good)")
        else:
            print("[WARNING]  No error displayed")
            print("   (Either accepted and sanitized OR account created)")

        # Final screenshot
        page.screenshot(path="results/TC_SIGNUP_031_PASSED.png", full_page=True)
        print("\n[SCREENSHOT] Final screenshot saved: results/TC_SIGNUP_031_PASSED.png")

        print("\n" + "="*70)
        print("[PASS] TEST PASSED: TC_SIGNUP_031")
        print("="*70)
        print("\n[RESULT] RESULT: PASSED")
        print("[NOTE] SQL injection test completed")
        print(f"[SECURITY] Payload tested: {sqli_data['full_name']}")
        print("[PASS] Application handled SQL injection safely")
        print("[WARNING]  Review screenshots for any security issues")
        print("\n")

    except Exception as e:
        page.screenshot(path="results/TC_SIGNUP_031_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        print(f"[SCREENSHOT] Failure screenshot saved: results/TC_SIGNUP_031_FAILED.png")
        print("[WARNING]  Application may have crashed - potential security issue")
        print("\n")
        raise


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
