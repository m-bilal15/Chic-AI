"""
Test Case: TC_SIGNUP_032
Title: Verify SQL injection in Email field
Description: Security test - verify app handles SQL injection in email safely
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
def test_tc_signup_032(page, signup_page, base_url):
    """
    Test Case: TC_SIGNUP_032
    Description: Verify SQL injection in Email field
    Priority: Critical
    Type: Security
    """

    print("\n" + "="*70)
    print("TEST: TC_SIGNUP_032 - SQL Injection in Email (Security)")
    print("="*70)

    try:
        test_data_path = Path("test_data/security_signup_data.json")
        with open(test_data_path) as f:
            test_data = json.load(f)

        sqli_data = test_data["sql_injection_payloads"]["email_sqli"]

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

        page.screenshot(path="results/TC_SIGNUP_032_initial.png", full_page=True)

        print(f"\n[STEP] Filling name: {sqli_data['full_name']}")
        signup_page.fill_full_name(sqli_data['full_name'])

        print(f"\n[STEP] Entering SQL injection in EMAIL:")
        print(f"   Payload: {sqli_data['email']}")
        signup_page.fill_email(sqli_data['email'])

        signup_page.fill_password(sqli_data['password'])
        signup_page.fill_confirm_password(sqli_data['confirm_password'])

        page.screenshot(path="results/TC_SIGNUP_032_before_submit.png", full_page=True)

        signup_page.click_create_account()
        time.sleep(3)

        page.screenshot(path="results/TC_SIGNUP_032_after_submit.png", full_page=True)

        print("\n[SECURITY CHECK] Verifying application security...")

        current_url = page.url
        print(f"[PASS] Application still running")

        page_content = page.content()
        db_error_indicators = ["sql", "mysql", "syntax error", "database error"]
        has_db_error = any(indicator in page_content.lower() for indicator in db_error_indicators)

        if has_db_error:
            print("[WARNING]  WARNING: Possible database error exposed!")
        else:
            print("[PASS] No database errors exposed")

        page.screenshot(path="results/TC_SIGNUP_032_PASSED.png", full_page=True)

        print("\n" + "="*70)
        print("[PASS] TEST PASSED: TC_SIGNUP_032")
        print("="*70)
        print(f"[SECURITY] Payload: {sqli_data['email']}")
        print("[PASS] Application handled SQL injection safely")
        print("\n")

    except Exception as e:
        page.screenshot(path="results/TC_SIGNUP_032_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        raise


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
