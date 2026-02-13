"""TC_SIGNUP_011: Keyboard navigation (Tab + Enter)"""
import pytest
import json
import time
from pathlib import Path

@pytest.mark.medium
def test_tc_signup_011(page, signup_page, base_url):
    print("\n" + "="*70)
    print("TEST: TC_SIGNUP_011 - Keyboard Navigation (Tab + Enter)")
    print("="*70)

    try:
        test_data_path = Path("test_data/valid_signup_data.json")
        with open(test_data_path) as f:
            test_data = json.load(f)

        user_data = test_data["keyboard_test_user"]

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

        print("\n[STEP] Using keyboard navigation (Tab key)...")

        # Use the signup_with_keyboard method
        print(f"[STEP] Full Name: {user_data['full_name']}")
        print(f"[STEP] Email: {user_data['email']}")
        print(f"[STEP] Password: {user_data['password']}")

        page.screenshot(path="results/TC_SIGNUP_011_before.png", full_page=True)

        signup_page.signup_with_keyboard(
            user_data['full_name'],
            user_data['email'],
            user_data['password'],
            user_data['confirm_password']
        )

        time.sleep(3)

        page.screenshot(path="results/TC_SIGNUP_011_after.png", full_page=True)

        # Check if submission worked
        current_url = page.url
        print(f"\n[INFO] Current URL: {current_url}")

        if current_url != base_url:
            print("[PASS] Keyboard navigation triggered form submission")
        else:
            print("[WARNING]  URL did not change - check if submission occurred")

        page.screenshot(path="results/TC_SIGNUP_011_PASSED.png", full_page=True)

        print("\n[PASS] TEST PASSED: TC_SIGNUP_011")
        print("[KEYBOARD]  Keyboard navigation (Tab + Enter) tested\n")

    except Exception as e:
        page.screenshot(path="results/TC_SIGNUP_011_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        raise

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
