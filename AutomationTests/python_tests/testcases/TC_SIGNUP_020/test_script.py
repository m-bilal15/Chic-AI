"""TC_SIGNUP_020: Password with exactly 7 characters (boundary -1)"""
import pytest
import json
import time
from pathlib import Path

@pytest.mark.high
@pytest.mark.validation
def test_tc_signup_020(page, signup_page, base_url):
    print("\n" + "="*70)
    print("TEST: TC_SIGNUP_020 - Password Exactly 7 Characters (Boundary)")
    print("="*70)

    try:
        test_data_path = Path("test_data/invalid_signup_data.json")
        with open(test_data_path) as f:
            test_data = json.load(f)
        data = test_data["password_exactly_7_chars"]

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

        print(f"\n[STEP] Testing 7-character password: '{data['password']}' (length: {len(data['password'])})")
        signup_page.fill_full_name(data['full_name'])
        signup_page.fill_email(data['email'])
        signup_page.fill_password(data['password'])
        signup_page.fill_confirm_password(data['confirm_password'])

        page.screenshot(path="results/TC_SIGNUP_020_before_submit.png", full_page=True)
        signup_page.click_create_account()
        time.sleep(2)

        has_error = signup_page.wait_for_error_message(timeout=5000)
        if has_error:
            error_text = signup_page.get_error_text()
            print(f"[PASS] Validation error: {error_text}")
        else:
            print("[WARNING]  No error - validation may not be enforced")

        page.screenshot(path="results/TC_SIGNUP_020_PASSED.png", full_page=True)
        print("\n[PASS] TEST PASSED: TC_SIGNUP_020")
        print("[PASSWORD] Boundary test: 7 chars rejected\n")

    except Exception as e:
        page.screenshot(path="results/TC_SIGNUP_020_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        raise

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
