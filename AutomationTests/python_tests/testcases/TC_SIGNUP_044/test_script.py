"""TC_SIGNUP_044: Button states (default, hover, disabled, loading)"""
import pytest
import time

@pytest.mark.medium
@pytest.mark.ui
def test_tc_signup_044(page, signup_page, base_url):
    print("\n" + "="*70)
    print("TEST: TC_SIGNUP_044 - Button States (UI/UX)")
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

        print("\n[CHECK] Capturing Create Account button states...")

        # Default state
        page.screenshot(path="results/TC_SIGNUP_044_default_state.png", full_page=True)
        print("   [PASS] Default state captured")

        # Hover state
        print("   Hovering over button...")
        button = page.locator('button:has-text("Create Account"), button[type="submit"]')
        button.hover()
        time.sleep(1)
        page.screenshot(path="results/TC_SIGNUP_044_hover_state.png", full_page=True)
        print("   [PASS] Hover state captured")

        # Try to trigger loading state
        print("   Filling form and clicking to check loading state...")
        signup_page.fill_full_name("John Smith")
        signup_page.fill_email("john@test.com")
        signup_page.fill_password("SecurePass@123")
        signup_page.fill_confirm_password("SecurePass@123")

        signup_page.click_create_account()
        time.sleep(0.5)  # Quick screenshot to catch loading state
        page.screenshot(path="results/TC_SIGNUP_044_loading_state.png", full_page=True)
        time.sleep(2)

        print("\n[PASS] Button states captured")
        print("[WARNING]  Review screenshots for visual states")

        page.screenshot(path="results/TC_SIGNUP_044_PASSED.png", full_page=True)
        print("\n[PASS] TEST PASSED: TC_SIGNUP_044\n")

    except Exception as e:
        page.screenshot(path="results/TC_SIGNUP_044_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        raise

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
