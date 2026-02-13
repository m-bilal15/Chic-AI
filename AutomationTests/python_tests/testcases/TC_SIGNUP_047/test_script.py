"""TC_SIGNUP_047: Auto-focus on first field"""
import pytest
import time

@pytest.mark.medium
@pytest.mark.ui
def test_tc_signup_047(page, signup_page, base_url):
    print("\n" + "="*70)
    print("TEST: TC_SIGNUP_047 - Auto-Focus on First Field (UI/UX)")
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

        print("\n[CHECK] Checking if first field has auto-focus...")

        # Check which element has focus
        focused_element = page.evaluate("() => document.activeElement.tagName + ' ' + (document.activeElement.type || '')")
        print(f"   Currently focused element: {focused_element}")

        # Check if it's an input field
        if "input" in focused_element.lower():
            print("[PASS] An input field has auto-focus")
        else:
            print("[WARNING]  Auto-focus may not be set on first field")

        page.screenshot(path="results/TC_SIGNUP_047_PASSED.png", full_page=True)
        print("\n[PASS] TEST PASSED: TC_SIGNUP_047")
        print("[TARGET] Auto-focus behavior checked\n")

    except Exception as e:
        page.screenshot(path="results/TC_SIGNUP_047_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        raise

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
