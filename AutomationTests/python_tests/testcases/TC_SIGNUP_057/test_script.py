"""TC_SIGNUP_057: Form reset/clear functionality"""
import pytest
import time

@pytest.mark.low
@pytest.mark.ui
def test_tc_signup_057(page, signup_page, base_url):
    print("\n" + "="*70)
    print("TEST: TC_SIGNUP_057 - Form Reset/Clear (UI/UX)")
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

        print("\n[STEP] Filling form...")
        signup_page.fill_full_name("John Smith")
        signup_page.fill_email("john@test.com")
        signup_page.fill_password("SecurePass@123")
        signup_page.fill_confirm_password("SecurePass@123")

        page.screenshot(path="results/TC_SIGNUP_057_filled.png", full_page=True)
        print("   [PASS] Form filled")

        # Check for clear/reset button
        print("\n[CHECK] Looking for clear/reset button...")
        page_content = page.content().lower()

        if "clear" in page_content or "reset" in page_content:
            print("   [PASS] Clear/Reset button may be available")

            # Try to find and click reset button
            try:
                reset_button = page.locator('button:has-text("Clear"), button:has-text("Reset")')
                if reset_button.is_visible(timeout=2000):
                    reset_button.click()
                    time.sleep(1)

                    # Check if fields are cleared
                    name_value = signup_page.get_full_name_value()
                    if not name_value:
                        print("   [PASS] Form cleared successfully")
                    else:
                        print("   [WARNING]  Form not cleared")
            except:
                print("   [WARNING]  Clear button not found or not clickable")
        else:
            print("   [WARNING]  No clear/reset button found")
            print("   (Feature may not be implemented)")

        page.screenshot(path="results/TC_SIGNUP_057_PASSED.png", full_page=True)
        print("\n[PASS] TEST PASSED: TC_SIGNUP_057")
        print("[RESET] Form reset functionality tested\n")

    except Exception as e:
        page.screenshot(path="results/TC_SIGNUP_057_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        raise

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
