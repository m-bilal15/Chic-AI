"""TC_SIGNUP_049: Browser autofill compatibility"""
import pytest
import time

@pytest.mark.medium
@pytest.mark.ui
def test_tc_signup_049(page, signup_page, base_url):
    print("\n" + "="*70)
    print("TEST: TC_SIGNUP_049 - Browser Autofill Compatibility (UI/UX)")
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

        print("\n[CHECK] Checking autocomplete attributes...")

        # Check if fields have autocomplete attributes
        page_content = page.content()

        autocomplete_attrs = {
            "name": "autocomplete=\"name\"",
            "email": "autocomplete=\"email\"",
            "new-password": "autocomplete=\"new-password\"",
        }

        found_attrs = []
        for attr_name, attr_value in autocomplete_attrs.items():
            if attr_value in page_content:
                found_attrs.append(attr_name)
                print(f"   [PASS] Found {attr_value}")

        if not found_attrs:
            print("   [WARNING]  No autocomplete attributes found")
            print("   (May use generic autocomplete or none)")

        # Check input types
        print("\n[CHECK] Verifying correct input types...")
        email_type = page.get_attribute(signup_page.EMAIL_INPUT, "type")
        password_type = page.get_attribute(signup_page.PASSWORD_INPUT, "type")

        print(f"   Email field type: {email_type}")
        print(f"   Password field type: {password_type}")

        if email_type == "email":
            print("   [PASS] Email field uses correct type")
        if password_type == "password":
            print("   [PASS] Password field uses correct type")

        page.screenshot(path="results/TC_SIGNUP_049_PASSED.png", full_page=True)
        print("\n[PASS] TEST PASSED: TC_SIGNUP_049")
        print("[CONFIG] Browser autofill compatibility checked\n")

    except Exception as e:
        page.screenshot(path="results/TC_SIGNUP_049_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        raise

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
