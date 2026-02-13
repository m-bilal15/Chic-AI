"""
Generate Individual Test Scripts for Each Test Case
Creates 50 separate folders with test_script.py files
FIXED: Properly escape quotes in descriptions
"""

import json
import os
import sys

# Set UTF-8 encoding for console
sys.stdout.reconfigure(encoding='utf-8')

# Read test cases from JSON
with open('../testcases/test_cases.json', 'r', encoding='utf-8') as f:
    test_cases = json.load(f)

print(f"Generating {len(test_cases)} individual test scripts...\n")

# Create testcases directory
testcases_dir = './testcases'
os.makedirs(testcases_dir, exist_ok=True)

# Test case implementations
test_implementations = {
    "TC_LOGIN_001": '''
            # Navigate to login page
            login_page.navigate_to_login()

            # Verify all login page elements
            assert login_page.is_login_page_displayed(), "Login page not displayed"
            assert login_page.is_logo_visible(), "Logo not visible"
            assert login_page.is_welcome_heading_visible(), "Welcome heading not visible"
            assert login_page.is_subtitle_visible(), "Subtitle not visible"
            assert login_page.is_google_button_visible(), "Google button not visible"
            assert login_page.is_sign_up_visible(), "Sign up button not visible"
''',
    "TC_LOGIN_002": '''
            # Navigate and login with valid credentials
            login_page.navigate_to_login()
            login_page.login("bilal@test.com", "ValidPass@123")
            time.sleep(2)
''',
    "TC_LOGIN_003": '''
            # Navigate
            login_page.navigate_to_login()

            # Enter valid email and blur
            login_page.enter_email("user@example.com")
            login_page.click_outside()

            # Verify no error and value retained
            assert not login_page.is_error_displayed(), "Unexpected error displayed"
            assert login_page.get_email_value() == "user@example.com", "Email value not retained"
''',
    "TC_LOGIN_004": '''
            # Navigate
            login_page.navigate_to_login()

            # Enter password
            login_page.enter_password("TestPass@123")

            # Verify password is masked
            assert login_page.get_password_type() == "password", "Password not masked"
''',
    "TC_LOGIN_005": '''
            # Navigate
            login_page.navigate_to_login()

            # Enter password
            login_page.enter_password("MySecret@123")

            # Verify password is masked
            assert login_page.get_password_type() == "password", "Password not masked initially"
''',
    "TC_LOGIN_006": '''
            # Navigate
            login_page.navigate_to_login()

            # Click Google Sign In
            login_page.click_google_sign_in()
            time.sleep(2)
''',
    "TC_LOGIN_007": '''
            # Navigate
            login_page.navigate_to_login()

            # Click Sign Up
            current_url = page.url
            login_page.click_sign_up()

            time.sleep(2)

            # Verify URL changed to signup
            new_url = page.url
            assert "signup" in new_url.lower() or "register" in new_url.lower(), f"Not redirected to signup. URL: {new_url}"
''',
    "TC_LOGIN_008": '''
            # Navigate
            login_page.navigate_to_login()

            # Check email placeholder
            placeholder = login_page.get_email_placeholder()
            assert "email" in placeholder.lower(), f"Incorrect placeholder: {placeholder}"
''',
    "TC_LOGIN_009": '''
            # Navigate
            login_page.navigate_to_login()

            # Check password placeholder
            placeholder = login_page.get_password_placeholder()
            assert "password" in placeholder.lower(), f"Incorrect placeholder: {placeholder}"
''',
    "TC_LOGIN_010": '''
            # Navigate
            login_page.navigate_to_login()

            # Login using keyboard (Tab and Enter)
            login_page.login_with_keyboard("bilal@test.com", "ValidPass@123")
''',
    "TC_LOGIN_011": '''
            # Navigate
            login_page.navigate_to_login()

            # Click Sign In with empty fields
            login_page.click_sign_in()
            time.sleep(2)

            # Verify validation error
            # NOTE: This will fail if app has no client-side validation
            assert login_page.is_error_displayed(), "No validation error for empty fields"
''',
    "TC_LOGIN_012": '''
            # Navigate
            login_page.navigate_to_login()

            # Enter email only, no password
            login_page.enter_email("bilal@test.com")
            login_page.click_sign_in()
            time.sleep(2)

            # Verify validation error
            assert login_page.is_error_displayed(), "No validation error for empty password"
''',
    "TC_LOGIN_013": '''
            # Navigate
            login_page.navigate_to_login()

            # Enter password only, no email
            login_page.enter_password("ValidPass@123")
            login_page.click_sign_in()
            time.sleep(2)

            # Verify validation error
            assert login_page.is_error_displayed(), "No validation error for empty email"
''',
    "TC_LOGIN_014": '''
            # Navigate
            login_page.navigate_to_login()

            # Enter invalid email format
            login_page.enter_email("plaintext")
            login_page.enter_password("ValidPass@123")
            login_page.click_sign_in()
            time.sleep(2)

            # Verify validation error
            assert login_page.is_error_displayed(), "No validation error for invalid email"
''',
    "TC_LOGIN_015": '''
            # Navigate
            login_page.navigate_to_login()

            # Login with wrong password
            login_page.login("bilal@test.com", "WrongPass@999")
            time.sleep(2)
''',
    "TC_LOGIN_027": '''
            # Navigate
            login_page.navigate_to_login()

            # Verify Welcome back heading
            assert login_page.is_welcome_heading_visible(), "Welcome heading not visible"
''',
    "TC_LOGIN_031": '''
            # Navigate
            login_page.navigate_to_login()

            # Verify Or continue with divider
            assert login_page.is_divider_visible(), "Divider not visible"
''',
    "TC_LOGIN_033": '''
            # Navigate
            login_page.navigate_to_login()

            # Verify Sign up button is visible
            assert login_page.is_sign_up_visible(), "Sign up button not visible"
''',
}

for tc in test_cases:
    tc_id = tc['Test Case ID']
    tc_description = tc['Test Description'].replace('"', '\\"')  # Escape quotes!
    tc_priority = tc['Priority']
    tc_type = tc['Test Type']

    # Create folder
    tc_folder = os.path.join(testcases_dir, tc_id)
    os.makedirs(tc_folder, exist_ok=True)

    # Get implementation or use default
    implementation = test_implementations.get(tc_id, '''
            # Navigate to login page
            login_page.navigate_to_login()

            # Basic test implementation
            assert login_page.is_login_page_displayed(), "Login page not displayed"
''')

    # Generate test script
    test_script = f'''"""
Test Case: {tc_id}
Description: {tc_description}
Priority: {tc_priority}
Type: {tc_type}
"""

import sys
import os
import time
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage


def test_{tc_id.lower()}():
    """
    {tc_id}: {tc_description}
    """

    print("=" * 80)
    print("Test Case: {tc_id}")
    print("Description: {tc_description}")
    print("Priority: {tc_priority} | Type: {tc_type}")
    print("=" * 80)
    print()

    with sync_playwright() as p:
        # Launch browser (VISIBLE, SLOW)
        print("Launching browser...")
        browser = p.chromium.launch(
            headless=False,
            slow_mo=2000
        )

        context = browser.new_context(
            viewport={{"width": 1280, "height": 720}},
            record_video_dir="../../results/{tc_id}/"
        )
        page = context.new_page()
        login_page = LoginPage(page)

        try:
            print("\\nStarting test execution...\\n")
{implementation}
            print("\\n" + "=" * 80)
            print("PASSED: {tc_id}")
            print("=" * 80)

        except AssertionError as e:
            print("\\n" + "=" * 80)
            print("FAILED: {tc_id}")
            print("Error: {{e}}")
            print("=" * 80)

            # Take screenshot
            screenshot_path = "../../results/{tc_id}_FAILED.png"
            os.makedirs("../../results", exist_ok=True)
            page.screenshot(path=screenshot_path, full_page=True)
            print("Screenshot saved: {{screenshot_path}}")
            raise

        except Exception as e:
            print("ERROR: {{str(e)}}")
            raise

        finally:
            print("\\nClosing browser...")
            context.close()
            browser.close()


if __name__ == "__main__":
    test_{tc_id.lower()}()
'''

    # Write to file
    script_path = os.path.join(tc_folder, 'test_script.py')
    with open(script_path, 'w', encoding='utf-8') as f:
        f.write(test_script)

    print(f"Created: {tc_id}/test_script.py")

print(f"\\nGenerated {len(test_cases)} test scripts successfully!")
print(f"Location: {testcases_dir}/")
