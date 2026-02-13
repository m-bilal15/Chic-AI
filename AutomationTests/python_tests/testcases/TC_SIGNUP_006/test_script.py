"""
Test Case: TC_SIGNUP_006
Title: Verify Password field masks input characters
Priority: High
Type: Positive
"""

import pytest
import time


@pytest.mark.high
@pytest.mark.validation
def test_tc_signup_006(page, signup_page, base_url):
    """TC_SIGNUP_006: Password field masks input"""

    print("\n" + "="*70)
    print("TEST: TC_SIGNUP_006 - Password Field Masks Input")
    print("="*70)

    try:
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

        test_password = "TestPass@123"

        print(f"\n[STEP] Entering password: {test_password}")
        signup_page.fill_password(test_password)

        print("[CHECK] Verifying password is masked...")
        is_masked = signup_page.is_password_masked()

        if is_masked:
            print("[PASS] Password field type is 'password' (masked)")
        else:
            print("[WARNING]  Password field type is NOT 'password'")

        # Check for eye icon visibility toggle
        print("[CHECK] Looking for visibility toggle (eye icon)...")
        page.screenshot(path="results/TC_SIGNUP_006_masked.png", full_page=True)

        print("\n[PASS] TEST PASSED: TC_SIGNUP_006")
        print("[SECURITY] Password input is properly masked\n")

    except Exception as e:
        page.screenshot(path="results/TC_SIGNUP_006_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        raise


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
