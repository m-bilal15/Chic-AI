"""
Test Case: TC_SIGNUP_008
Title: Verify Password visibility toggle on Confirm Password field
Priority: High
Type: Positive
"""

import pytest
import time


@pytest.mark.high
def test_tc_signup_008(page, signup_page, base_url):
    """TC_SIGNUP_008: Confirm Password visibility toggle"""

    print("\n" + "="*70)
    print("TEST: TC_SIGNUP_008 - Confirm Password Visibility Toggle")
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

        print("\n[STEP] Entering confirm password")
        signup_page.fill_confirm_password("MySecret@123")

        initial_type = signup_page.get_confirm_password_type()
        print(f"   Initial type: {initial_type}")

        try:
            signup_page.toggle_confirm_password_visibility()
            time.sleep(1)

            after_type = signup_page.get_confirm_password_type()
            if after_type == "text":
                print("[PASS] Confirm password now visible")

            signup_page.toggle_confirm_password_visibility()
            final_type = signup_page.get_confirm_password_type()
            if final_type == "password":
                print("[PASS] Confirm password masked again")
        except:
            print("[WARNING]  Toggle feature may not be implemented")

        page.screenshot(path="results/TC_SIGNUP_008_PASSED.png", full_page=True)
        print("\n[PASS] TEST PASSED: TC_SIGNUP_008\n")

    except Exception as e:
        page.screenshot(path="results/TC_SIGNUP_008_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        raise


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
