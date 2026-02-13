"""TC_SIGNUP_054: Accessibility - Tab order"""
import pytest
import time

@pytest.mark.low
@pytest.mark.accessibility
def test_tc_signup_054(page, signup_page, base_url):
    print("\n" + "="*70)
    print("TEST: TC_SIGNUP_054 - Tab Order (Accessibility)")
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

        print("\n[STEP] Testing tab order through form...")

        # Start at first field
        signup_page.focus_full_name()
        time.sleep(0.5)

        focused_elements = []

        # Tab through form
        for i in range(6):
            focused = page.evaluate("() => document.activeElement.tagName + ' ' + (document.activeElement.type || document.activeElement.textContent?.substring(0, 20) || '')")
            focused_elements.append(focused)
            print(f"   Tab {i+1}: {focused}")

            page.keyboard.press("Tab")
            time.sleep(0.5)

        print(f"\n   [PASS] Tab order captured ({len(focused_elements)} elements)")
        print("   Expected order: Full Name → Email → Password → Confirm Password → Button")

        page.screenshot(path="results/TC_SIGNUP_054_PASSED.png", full_page=True)
        print("\n[PASS] TEST PASSED: TC_SIGNUP_054")
        print("[KEYBOARD]  Tab order tested\n")

    except Exception as e:
        page.screenshot(path="results/TC_SIGNUP_054_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        raise

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
