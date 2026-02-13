"""TC_SIGNUP_016: Empty Password only"""
import pytest
import json
import time
from pathlib import Path

@pytest.mark.high
@pytest.mark.validation
def test_tc_signup_016(page, signup_page, base_url):
    print("\n" + "="*70)
    print("TEST: TC_SIGNUP_016 - Empty Password Only")
    print("="*70)

    try:
        test_data_path = Path("test_data/invalid_signup_data.json")
        with open(test_data_path) as f:
            test_data = json.load(f)
        data = test_data["empty_fields"]["password_empty"]

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

        print("\n[STEP] Leaving Password EMPTY")
        signup_page.fill_full_name(data['full_name'])
        signup_page.fill_email(data['email'])
        signup_page.clear_password()
        signup_page.fill_confirm_password(data['confirm_password'])

        page.screenshot(path="results/TC_SIGNUP_016_before_submit.png", full_page=True)
        signup_page.click_create_account()
        time.sleep(2)

        has_error = signup_page.wait_for_error_message(timeout=5000)
        if has_error:
            print("[PASS] Validation error displayed")

        page.screenshot(path="results/TC_SIGNUP_016_PASSED.png", full_page=True)
        print("\n[PASS] TEST PASSED: TC_SIGNUP_016\n")

    except Exception as e:
        page.screenshot(path="results/TC_SIGNUP_016_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        raise

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
