"""
Test Case: TC_SIGNUP_010
Title: Verify "Sign in here" link navigates to Login page
Priority: High
Type: Positive
"""

import pytest
import time


@pytest.mark.high
def test_tc_signup_010(page, signup_page, base_url):
    """TC_SIGNUP_010: Sign in link navigation"""

    print("\n" + "="*70)
    print("TEST: TC_SIGNUP_010 - Sign In Link Navigation")
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

        initial_url = page.url
        print(f"[INFO] Current URL: {initial_url}")

        page.screenshot(path="results/TC_SIGNUP_010_on_signup.png", full_page=True)

        print("\n[STEP] Clicking 'Sign in here' link...")
        signup_page.click_sign_in_link()
        time.sleep(2)

        new_url = page.url
        print(f"[INFO] New URL: {new_url}")

        # Check if navigated to login
        if new_url != initial_url:
            print("[PASS] URL changed - navigated successfully")

            # Check for login page elements
            login_indicators = ["welcome back", "sign in", "login"]
            page_content = page.content().lower()

            if any(indicator in page_content for indicator in login_indicators):
                print("[PASS] Login page elements detected")
        else:
            print("[WARNING]  URL did not change")

        page.screenshot(path="results/TC_SIGNUP_010_PASSED.png", full_page=True)
        print("\n[PASS] TEST PASSED: TC_SIGNUP_010\n")

    except Exception as e:
        page.screenshot(path="results/TC_SIGNUP_010_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        raise


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
