"""TC_SIGNUP_055: Accessibility - Color contrast"""
import pytest
import time

@pytest.mark.low
@pytest.mark.accessibility
def test_tc_signup_055(page, signup_page, base_url):
    print("\n" + "="*70)
    print("TEST: TC_SIGNUP_055 - Color Contrast (Accessibility)")
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

        print("\n[CHECK] Capturing page for color contrast analysis...")

        # Take full page screenshot for manual review
        page.screenshot(path="results/TC_SIGNUP_055_full_page.png", full_page=True)

        # Trigger error state for contrast check
        signup_page.clear_all_fields()
        signup_page.click_create_account()
        time.sleep(2)

        page.screenshot(path="results/TC_SIGNUP_055_with_errors.png", full_page=True)

        print("\n   [PASS] Screenshots captured for contrast analysis")
        print("   [WARNING]  Manual review needed:")
        print("      - Check text contrast against background")
        print("      - Verify error messages are clearly visible")
        print("      - Ensure button text is readable")
        print("      - Recommended: Use WCAG contrast checker tool")
        print("      - Minimum ratio: 4.5:1 for normal text")
        print("      - Minimum ratio: 3:1 for large text")

        page.screenshot(path="results/TC_SIGNUP_055_PASSED.png", full_page=True)
        print("\n[PASS] TEST PASSED: TC_SIGNUP_055")
        print("[UI] Color contrast tested (manual review required)\n")

    except Exception as e:
        page.screenshot(path="results/TC_SIGNUP_055_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        raise

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
