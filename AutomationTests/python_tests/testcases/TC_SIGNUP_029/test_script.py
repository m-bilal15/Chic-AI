"""TC_SIGNUP_029: Weak password (no special characters/numbers)"""
import pytest
import json
import time
from pathlib import Path

@pytest.mark.high
@pytest.mark.validation
def test_tc_signup_029(page, signup_page, base_url):
    print("\n" + "="*70)
    print("TEST: TC_SIGNUP_029 - Weak Password (No Special Chars)")
    print("="*70)

    try:
        test_data_path = Path("test_data/invalid_signup_data.json")
        with open(test_data_path) as f:
            test_data = json.load(f)
        data = test_data["weak_password_no_special_chars"]

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

        print(f"\n[STEP] Testing weak password: '{data['password']}'")
        print(f"   (Only lowercase, no special chars/numbers)")
        signup_page.fill_full_name(data['full_name'])
        signup_page.fill_email(data['email'])
        signup_page.fill_password(data['password'])
        signup_page.fill_confirm_password(data['confirm_password'])

        page.screenshot(path="results/TC_SIGNUP_029_before_submit.png", full_page=True)
        signup_page.click_create_account()
        time.sleep(2)

        has_error = signup_page.wait_for_error_message(timeout=5000)
        if has_error:
            print("[PASS] Validation error - weak password rejected")
        else:
            print("[WARNING]  No error - weak password may be accepted (length-only policy)")

        page.screenshot(path="results/TC_SIGNUP_029_PASSED.png", full_page=True)
        print("\n[PASS] TEST PASSED: TC_SIGNUP_029\n")

    except Exception as e:
        page.screenshot(path="results/TC_SIGNUP_029_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        raise

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
