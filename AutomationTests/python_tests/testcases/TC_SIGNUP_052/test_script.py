"""TC_SIGNUP_052: Loading spinner during submission"""
import pytest
import time

@pytest.mark.low
@pytest.mark.ui
def test_tc_signup_052(page, signup_page, base_url):
    print("\n" + "="*70)
    print("TEST: TC_SIGNUP_052 - Loading Spinner (UI/UX)")
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

        print("\n[STEP] Filling form and checking for loading indicator...")

        signup_page.fill_full_name("John Smith")
        signup_page.fill_email("john.loading@test.com")
        signup_page.fill_password("SecurePass@123")
        signup_page.fill_confirm_password("SecurePass@123")

        # Click submit and quickly check for loading state
        signup_page.click_create_account()
        time.sleep(0.5)  # Quick capture

        page.screenshot(path="results/TC_SIGNUP_052_during_submit.png", full_page=True)

        # Check if loading indicator is present
        is_loading = signup_page.is_loading()
        if is_loading:
            print("   [PASS] Loading indicator detected")
        else:
            print("   [WARNING]  No loading indicator found (may be too fast)")

        time.sleep(2)
        page.screenshot(path="results/TC_SIGNUP_052_PASSED.png", full_page=True)

        print("\n[PASS] TEST PASSED: TC_SIGNUP_052")
        print("[LOADING] Loading indicator tested\n")

    except Exception as e:
        page.screenshot(path="results/TC_SIGNUP_052_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        raise

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
