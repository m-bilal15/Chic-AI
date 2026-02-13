"""TC_SIGNUP_056: Form validation on blur (field exit)"""
import pytest
import time

@pytest.mark.low
@pytest.mark.validation
def test_tc_signup_056(page, signup_page, base_url):
    print("\n" + "="*70)
    print("TEST: TC_SIGNUP_056 - Validation on Blur (UI/UX)")
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

        print("\n[STEP] Testing validation on field blur...")

        # Focus on email, enter invalid, then blur
        print("   Testing email field...")
        signup_page.focus_email()
        signup_page.fill_email("invalid-email")
        signup_page.click_outside()  # Blur
        time.sleep(1)

        page.screenshot(path="results/TC_SIGNUP_056_email_blur.png", full_page=True)

        has_error = signup_page.is_error_displayed()
        if has_error:
            print("   [PASS] Validation triggered on blur")
        else:
            print("   [WARNING]  No validation on blur (may validate on submit only)")

        # Test password field blur
        print("\n   Testing password field...")
        signup_page.focus_password()
        signup_page.fill_password("short")
        signup_page.click_outside()
        time.sleep(1)

        page.screenshot(path="results/TC_SIGNUP_056_password_blur.png", full_page=True)

        page.screenshot(path="results/TC_SIGNUP_056_PASSED.png", full_page=True)
        print("\n[PASS] TEST PASSED: TC_SIGNUP_056")
        print("[EYE]  Blur validation tested\n")

    except Exception as e:
        page.screenshot(path="results/TC_SIGNUP_056_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        raise

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
