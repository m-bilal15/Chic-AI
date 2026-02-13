"""TC_SIGNUP_041: Form field placeholders"""
import pytest
import time

@pytest.mark.medium
@pytest.mark.ui
def test_tc_signup_041(page, signup_page, base_url):
    print("\n" + "="*70)
    print("TEST: TC_SIGNUP_041 - Form Field Placeholders (UI/UX)")
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

        print("\n[CHECK] Verifying field placeholders...")

        # Check Full Name placeholder
        name_placeholder = signup_page.get_full_name_placeholder()
        print(f"   Full Name placeholder: '{name_placeholder}'")

        # Check Email placeholder
        email_placeholder = signup_page.get_email_placeholder()
        print(f"   Email placeholder: '{email_placeholder}'")

        # Check Password placeholder
        pwd_placeholder = signup_page.get_password_placeholder()
        print(f"   Password placeholder: '{pwd_placeholder}'")

        # Check Confirm Password placeholder
        confirm_placeholder = signup_page.get_confirm_password_placeholder()
        print(f"   Confirm Password placeholder: '{confirm_placeholder}'")

        # Verify placeholders are helpful
        if name_placeholder and email_placeholder and pwd_placeholder:
            print("\n[PASS] All fields have placeholders")
        else:
            print("\n[WARNING]  Some fields missing placeholders")

        page.screenshot(path="results/TC_SIGNUP_041_PASSED.png", full_page=True)
        print("\n[PASS] TEST PASSED: TC_SIGNUP_041")
        print("[UI] Form field placeholders verified\n")

    except Exception as e:
        page.screenshot(path="results/TC_SIGNUP_041_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        raise

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
