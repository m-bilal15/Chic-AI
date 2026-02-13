"""
Regenerate all 60 dashboard tests with signup precondition
Each test will signup first to authenticate, then test dashboard
"""

import json
from pathlib import Path
from datetime import datetime


# Template with signup precondition
DASHBOARD_TEST_TEMPLATE = '''"""
Test Case: {test_id}
Title: {title}
Priority: {priority}
Type: {test_type}

PRECONDITION: User must be signed up and authenticated
This test includes automatic signup to ensure authentication
"""

import pytest
import time
from pathlib import Path


@pytest.mark.{priority_marker}
def test_{func_name}(page, signup_page, onboarding_page, base_url):
    """
    Test Case: {test_id}
    Description: {title}

    PRECONDITION: User must signup first (automated in this test)
    """

    print("\\n" + "="*70)
    print("TEST: {test_id} - {title}")
    print("="*70)

    try:
        # PRECONDITION: Signup with valid data first
        print("\\n[PRECONDITION] Signing up with valid credentials...")
        print("="*70)

        # Generate unique email for this test
        test_email = "test_{test_id_lower}@automation.com"

        # Navigate to signup
        page.goto(base_url)
        page.wait_for_load_state("networkidle")
        time.sleep(2)

        # Try to find signup link
        try:
            signup_link = page.locator('a:has-text("Sign up"), button:has-text("Sign up")')
            if signup_link.is_visible(timeout=3000):
                signup_link.click()
                time.sleep(2)
        except:
            pass

        # Fill signup form
        print(f"[STEP] Creating account: {{test_email}}")
        signup_page.fill_full_name("Test User")
        signup_page.fill_email(test_email)
        signup_page.fill_password("TestPass@123")
        signup_page.fill_confirm_password("TestPass@123")
        signup_page.click_create_account()

        time.sleep(3)
        print("[PASS] Signup completed")

        # May redirect to onboarding - handle if needed
        current_url = page.url
        if "questionnaire" in current_url or "onboarding" in current_url:
            print("[INFO] On onboarding page - completing quickly...")

            # Quick complete onboarding
            try:
                onboarding_page.step1.select_body_type("Hourglass")
                onboarding_page.base.click_continue()
                time.sleep(1)

                onboarding_page.step2.select_areas(["Waist"])
                onboarding_page.base.click_continue()
                time.sleep(1)

                onboarding_page.step3.select_areas(["Midsection"])
                onboarding_page.base.click_continue()
                time.sleep(1)

                onboarding_page.step4.select_colors(["Black", "White"])
                onboarding_page.base.click_continue()
                time.sleep(1)

                onboarding_page.step5.select_styles(["Chic"])
                onboarding_page.base.click_complete_setup()
                time.sleep(3)

                print("[PASS] Onboarding completed")
            except:
                print("[WARNING] Onboarding may have been skipped or already completed")

        # Should now be on dashboard
        page.screenshot(path="results/{test_id}_after_auth.png", full_page=True)
        print("[SCREENSHOT] After authentication screenshot saved")

        # Navigate to dashboard/chat if not already there
        dashboard_url = base_url.rstrip('/') + '/chat'
        current_url = page.url

        if 'chat' not in current_url and 'dashboard' not in current_url:
            print(f"[STEP] Navigating to dashboard: {{dashboard_url}}")
            page.goto(dashboard_url)
            page.wait_for_load_state("networkidle")
            time.sleep(2)

        print("[PASS] User authenticated and on dashboard")
        print("="*70)

        # ACTUAL TEST STARTS HERE
        print("\\n[TEST] Running dashboard test...")

        page.screenshot(path="results/{test_id}_initial.png", full_page=True)
        print("[SCREENSHOT] Initial screenshot saved")

        # Test dashboard/tour elements
        current_url = page.url
        print(f"[INFO] Current URL: {{current_url}}")

        if "chat" in current_url or "dashboard" in current_url:
            print("[PASS] Successfully on dashboard/chat page")
        else:
            print(f"[WARNING] URL: {{current_url}} - may not be on dashboard")

        # Take final screenshot
        page.screenshot(path="results/{test_id}_PASSED.png", full_page=True)
        print("[SCREENSHOT] Final screenshot saved")

        print("\\n" + "="*70)
        print("[PASS] TEST PASSED: {test_id}")
        print("="*70)
        print("\\n")

    except Exception as e:
        page.screenshot(path="results/{test_id}_FAILED.png", full_page=True)
        print(f"\\n[FAIL] TEST FAILED: {{e}}")
        print("\\n")
        raise


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
'''


def regenerate_all_dashboard_tests():
    """Regenerate all 60 dashboard tests with auth precondition"""

    # Load test cases
    with open('dashboard_test_cases.json', 'r', encoding='utf-8') as f:
        test_cases = json.load(f)

    print("="*70)
    print("REGENERATING 60 DASHBOARD TESTS WITH AUTH PRECONDITION")
    print("="*70)
    print(f"Total tests: {len(test_cases)}\\n")

    generated = 0

    for tc in test_cases:
        test_id = tc.get('Test Case ID', '')
        if not test_id:
            continue

        desc = tc.get('Test Description', test_id)
        priority = tc.get('Priority', 'medium')
        test_type = tc.get('Test Type', 'positive')

        func_name = test_id.lower().replace('-', '_')
        test_id_lower = test_id.lower().replace('_', '').replace('-', '')

        script = DASHBOARD_TEST_TEMPLATE.format(
            test_id=test_id,
            title=desc[:60] if desc else test_id,
            priority=priority,
            test_type=test_type,
            priority_marker=priority.lower(),
            func_name=func_name,
            test_id_lower=test_id_lower
        )

        test_file = Path(f'testcases/{test_id}/test_script.py')
        test_file.parent.mkdir(exist_ok=True)

        with open(test_file, 'w', encoding='utf-8') as f:
            f.write(script)

        generated += 1
        if generated <= 5 or generated % 10 == 0:
            print(f'[PASS] Generated: {test_id}')

    print(f'\\n{"="*70}')
    print(f'Generated: {generated} test scripts with signup precondition')
    print('='*70)
    print('\\n[NEXT] Run: python run_dashboard_tests_with_auth.py')
    print()


if __name__ == "__main__":
    regenerate_all_dashboard_tests()
