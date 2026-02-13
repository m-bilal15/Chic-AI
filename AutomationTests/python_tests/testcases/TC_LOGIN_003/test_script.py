"""
Test Case: TC_LOGIN_003
Description: Verify Email field accepts valid email format
Priority: High
Type: Positive
"""

import sys
import os
import time
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage


def test_tc_login_003():
    """
    TC_LOGIN_003: Verify Email field accepts valid email format
    """

    print("=" * 80)
    print("Test Case: TC_LOGIN_003")
    print("Description: Verify Email field accepts valid email format")
    print("Priority: High | Type: Positive")
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
            viewport={"width": 1280, "height": 720},
            record_video_dir="../../results/TC_LOGIN_003/"
        )
        page = context.new_page()
        login_page = LoginPage(page)

        try:
            print("\nStarting test execution...\n")

            # Navigate
            login_page.navigate_to_login()

            # Enter valid email and blur
            login_page.enter_email("user@example.com")
            login_page.click_outside()

            # Verify no error and value retained
            assert not login_page.is_error_displayed(), "Unexpected error displayed"
            assert login_page.get_email_value() == "user@example.com", "Email value not retained"

            print("\n" + "=" * 80)
            print("PASSED: TC_LOGIN_003")
            print("=" * 80)

        except AssertionError as e:
            print("\n" + "=" * 80)
            print("FAILED: TC_LOGIN_003")
            print("Error: {e}")
            print("=" * 80)

            # Take screenshot
            screenshot_path = "../../results/TC_LOGIN_003_FAILED.png"
            os.makedirs("../../results", exist_ok=True)
            page.screenshot(path=screenshot_path, full_page=True)
            print("Screenshot saved: {screenshot_path}")
            raise

        except Exception as e:
            print("ERROR: {str(e)}")
            raise

        finally:
            print("\nClosing browser...")
            context.close()
            browser.close()


if __name__ == "__main__":
    test_tc_login_003()
