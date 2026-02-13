"""
Test Case: TC_LOGIN_001
Description: Verify Login page loads successfully
Priority: Critical
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


def test_tc_login_001():
    """
    TC_LOGIN_001: Verify Login page loads successfully
    """

    print("=" * 80)
    print("Test Case: TC_LOGIN_001")
    print("Description: Verify Login page loads successfully")
    print("Priority: Critical | Type: Positive")
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
            record_video_dir="../../results/TC_LOGIN_001/"
        )
        page = context.new_page()
        login_page = LoginPage(page)

        try:
            print("\nStarting test execution...\n")

            # Navigate to login page
            login_page.navigate_to_login()

            # Verify all login page elements
            assert login_page.is_login_page_displayed(), "Login page not displayed"
            assert login_page.is_logo_visible(), "Logo not visible"
            assert login_page.is_welcome_heading_visible(), "Welcome heading not visible"
            assert login_page.is_subtitle_visible(), "Subtitle not visible"
            assert login_page.is_google_button_visible(), "Google button not visible"
            assert login_page.is_sign_up_visible(), "Sign up button not visible"

            print("\n" + "=" * 80)
            print("PASSED: TC_LOGIN_001")
            print("=" * 80)

        except AssertionError as e:
            print("\n" + "=" * 80)
            print("FAILED: TC_LOGIN_001")
            print("Error: {e}")
            print("=" * 80)

            # Take screenshot
            screenshot_path = "../../results/TC_LOGIN_001_FAILED.png"
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
    test_tc_login_001()
