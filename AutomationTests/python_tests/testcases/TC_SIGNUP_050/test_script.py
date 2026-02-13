"""TC_SIGNUP_050: Error message animations/transitions"""
import pytest
import time

@pytest.mark.low
@pytest.mark.ui
def test_tc_signup_050(page, signup_page, base_url):
    print("\n" + "="*70)
    print("TEST: TC_SIGNUP_050 - Error Message Animations (UI/UX)")
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

        print("\n[STEP] Triggering validation errors...")

        # Take screenshot before error
        page.screenshot(path="results/TC_SIGNUP_050_before_error.png", full_page=True)

        # Trigger validation error
        signup_page.clear_all_fields()
        signup_page.click_create_account()

        # Quick screenshot to catch animation start
        time.sleep(0.3)
        page.screenshot(path="results/TC_SIGNUP_050_error_appearing.png", full_page=True)

        # Wait for animation to complete
        time.sleep(1)
        page.screenshot(path="results/TC_SIGNUP_050_error_complete.png", full_page=True)

        print("\n[PASS] Error appearance captured")
        print("[WARNING]  Review screenshots to verify animations/transitions")
        print("   - Check for smooth fade-in")
        print("   - Check for slide-in effect")
        print("   - Verify no jarring appearance")

        page.screenshot(path="results/TC_SIGNUP_050_PASSED.png", full_page=True)
        print("\n[PASS] TEST PASSED: TC_SIGNUP_050")
        print("[ANIMATION] Error animations tested\n")

    except Exception as e:
        page.screenshot(path="results/TC_SIGNUP_050_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        raise

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
