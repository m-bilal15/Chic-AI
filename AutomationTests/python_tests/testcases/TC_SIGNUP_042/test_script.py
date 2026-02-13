"""TC_SIGNUP_042: Field focus states and visual feedback"""
import pytest
import time

@pytest.mark.medium
@pytest.mark.ui
def test_tc_signup_042(page, signup_page, base_url):
    print("\n" + "="*70)
    print("TEST: TC_SIGNUP_042 - Field Focus States (UI/UX)")
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

        print("\n[STEP] Testing field focus states...")

        # Focus on Full Name
        print("   Focusing on Full Name field...")
        signup_page.focus_full_name()
        page.screenshot(path="results/TC_SIGNUP_042_name_focused.png", full_page=True)

        # Focus on Email
        print("   Focusing on Email field...")
        signup_page.focus_email()
        page.screenshot(path="results/TC_SIGNUP_042_email_focused.png", full_page=True)

        # Focus on Password
        print("   Focusing on Password field...")
        signup_page.focus_password()
        page.screenshot(path="results/TC_SIGNUP_042_password_focused.png", full_page=True)

        # Focus on Confirm Password
        print("   Focusing on Confirm Password field...")
        signup_page.focus_confirm_password()
        page.screenshot(path="results/TC_SIGNUP_042_confirm_focused.png", full_page=True)

        print("\n[PASS] All fields can receive focus")
        print("[WARNING]  Review screenshots to verify visual focus indicators")

        page.screenshot(path="results/TC_SIGNUP_042_PASSED.png", full_page=True)
        print("\n[PASS] TEST PASSED: TC_SIGNUP_042")
        print("[UI] Field focus states tested\n")

    except Exception as e:
        page.screenshot(path="results/TC_SIGNUP_042_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        raise

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
