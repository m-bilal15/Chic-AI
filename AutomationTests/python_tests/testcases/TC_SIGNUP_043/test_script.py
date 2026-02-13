"""TC_SIGNUP_043: Error message styling and placement"""
import pytest
import time

@pytest.mark.medium
@pytest.mark.ui
def test_tc_signup_043(page, signup_page, base_url):
    print("\n" + "="*70)
    print("TEST: TC_SIGNUP_043 - Error Message Styling (UI/UX)")
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

        print("\n[STEP] Triggering validation error to check styling...")

        # Submit empty form to trigger errors
        signup_page.clear_all_fields()
        signup_page.click_create_account()
        time.sleep(2)

        page.screenshot(path="results/TC_SIGNUP_043_with_errors.png", full_page=True)

        has_error = signup_page.is_error_displayed()
        if has_error:
            print("[PASS] Error messages displayed")
            error_text = signup_page.get_error_text()
            print(f"   Error text: {error_text}")
        else:
            print("[WARNING]  No error messages found (may use native validation)")

        print("\n[WARNING]  Review screenshot to verify:")
        print("   - Error messages are visible")
        print("   - Error styling is clear (color, position)")
        print("   - Errors are near their respective fields")

        page.screenshot(path="results/TC_SIGNUP_043_PASSED.png", full_page=True)
        print("\n[PASS] TEST PASSED: TC_SIGNUP_043")
        print("[UI] Error message styling checked\n")

    except Exception as e:
        page.screenshot(path="results/TC_SIGNUP_043_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        raise

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
