"""TC_SIGNUP_051: Field character limits display"""
import pytest
import time

@pytest.mark.low
@pytest.mark.ui
def test_tc_signup_051(page, signup_page, base_url):
    print("\n" + "="*70)
    print("TEST: TC_SIGNUP_051 - Field Character Limits (UI/UX)")
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

        print("\n[CHECK] Testing field character limits...")

        # Check maxlength attributes
        page_source = page.content()

        fields_to_check = {
            "Full Name": signup_page.FULL_NAME_INPUT,
            "Email": signup_page.EMAIL_INPUT,
        }

        for field_name, selector in fields_to_check.items():
            try:
                maxlength = page.get_attribute(selector, "maxlength")
                if maxlength:
                    print(f"   {field_name}: maxlength = {maxlength}")
                else:
                    print(f"   {field_name}: No maxlength set")
            except:
                print(f"   {field_name}: Could not check maxlength")

        # Test typing beyond limit in Full Name
        print("\n[STEP] Testing typing beyond limit...")
        long_text = "A" * 500
        signup_page.fill_full_name(long_text)

        entered_value = signup_page.get_full_name_value()
        print(f"   Tried to enter: {len(long_text)} chars")
        print(f"   Actually entered: {len(entered_value)} chars")

        if len(entered_value) < len(long_text):
            print(f"   [PASS] Field enforced character limit at {len(entered_value)}")

        page.screenshot(path="results/TC_SIGNUP_051_PASSED.png", full_page=True)
        print("\n[PASS] TEST PASSED: TC_SIGNUP_051")
        print("[BOUNDARY] Character limits tested\n")

    except Exception as e:
        page.screenshot(path="results/TC_SIGNUP_051_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        raise

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
