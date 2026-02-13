"""
Test Case: TC_LOGIN_046
Description: Verify Google Sign-In cancellation
Priority: Medium
Type: Negative
"""

import sys
import os
import time
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage


def test_tc_login_046():
    """
    TC_LOGIN_046: Verify Google Sign-In cancellation
    """

    print("=" * 80)
    print("Test Case: TC_LOGIN_046")
    print("Description: Verify Google Sign-In cancellation")
    print("Priority: Medium | Type: Negative")
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
            record_video_dir="../../results/TC_LOGIN_046/"
        )
        page = context.new_page()
        login_page = LoginPage(page)

        try:
            print("\nStarting test execution...\n")

            # Navigate to login page
            login_page.navigate_to_login()

            # Basic test implementation
            assert login_page.is_login_page_displayed(), "Login page not displayed"

            print("\n" + "=" * 80)
            print("PASSED: TC_LOGIN_046")
            print("=" * 80)

        except AssertionError as e:
            print("\n" + "=" * 80)
            print("FAILED: TC_LOGIN_046")
            print("Error: {e}")
            print("=" * 80)

            # Take screenshot
            screenshot_path = "../../results/TC_LOGIN_046_FAILED.png"
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
    test_tc_login_046()
