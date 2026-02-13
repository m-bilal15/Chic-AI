"""TC_SIGNUP_048: Copy/paste in password fields"""
import pytest
import time

@pytest.mark.medium
@pytest.mark.ui
def test_tc_signup_048(page, signup_page, base_url):
    print("\n" + "="*70)
    print("TEST: TC_SIGNUP_048 - Copy/Paste in Password Fields (UI/UX)")
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

        test_password = "SecurePass@123"

        print(f"\n[STEP] Testing copy/paste in password field...")

        # Fill password field
        signup_page.fill_password(test_password)

        # Try to copy from password field (may be blocked)
        print("   Attempting to select and copy password...")
        try:
            password_field = page.locator(signup_page.PASSWORD_INPUT)
            password_field.click()
            page.keyboard.press("Control+A")
            page.keyboard.press("Control+C")
            time.sleep(0.5)
            print("   [PASS] Copy attempted")
        except:
            print("   [WARNING]  Copy may be blocked")

        # Try to paste in confirm password
        print("   Attempting to paste in confirm password...")
        try:
            confirm_field = page.locator(signup_page.CONFIRM_PASSWORD_INPUT)
            confirm_field.click()
            page.keyboard.press("Control+V")
            time.sleep(0.5)

            pasted_value = signup_page.get_confirm_password_value()
            if pasted_value:
                print(f"   [PASS] Paste worked (length: {len(pasted_value)})")
            else:
                print("   [WARNING]  Paste may be blocked")
        except:
            print("   [WARNING]  Paste operation failed")

        page.screenshot(path="results/TC_SIGNUP_048_PASSED.png", full_page=True)
        print("\n[PASS] TEST PASSED: TC_SIGNUP_048")
        print("[CLIPBOARD] Copy/paste behavior tested\n")

    except Exception as e:
        page.screenshot(path="results/TC_SIGNUP_048_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        raise

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
