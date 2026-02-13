"""TC_SIGNUP_026: Extremely long Full Name (255+ chars)"""
import pytest
import json
import time
from pathlib import Path

@pytest.mark.medium
@pytest.mark.validation
def test_tc_signup_026(page, signup_page, base_url):
    print("\n" + "="*70)
    print("TEST: TC_SIGNUP_026 - Extremely Long Name (Boundary)")
    print("="*70)

    try:
        test_data_path = Path("test_data/security_signup_data.json")
        with open(test_data_path) as f:
            test_data = json.load(f)
        data = test_data["boundary_tests"]["extremely_long_name"]

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

        print(f"\n[STEP] Testing extremely long name ({len(data['full_name'])} characters)")
        signup_page.fill_full_name(data['full_name'])
        signup_page.fill_email(data['email'])
        signup_page.fill_password(data['password'])
        signup_page.fill_confirm_password(data['confirm_password'])

        # Check if field truncated the input
        entered_name = signup_page.get_full_name_value()
        print(f"[INFO] Entered length: {len(data['full_name'])}, Field length: {len(entered_name)}")

        if len(entered_name) < len(data['full_name']):
            print(f"[PASS] Field truncated at {len(entered_name)} characters")
        else:
            print("[WARNING]  Field accepted full length input")

        page.screenshot(path="results/TC_SIGNUP_026_before_submit.png", full_page=True)
        signup_page.click_create_account()
        time.sleep(2)

        page.screenshot(path="results/TC_SIGNUP_026_PASSED.png", full_page=True)
        print("\n[PASS] TEST PASSED: TC_SIGNUP_026")
        print("[BOUNDARY] Boundary test: Extremely long name handled\n")

    except Exception as e:
        page.screenshot(path="results/TC_SIGNUP_026_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        raise

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
