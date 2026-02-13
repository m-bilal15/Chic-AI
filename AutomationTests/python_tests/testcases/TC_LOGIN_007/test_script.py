"""
Test Case: TC_LOGIN_007
Description: Verify \"Sign up here\" link navigation
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


def test_tc_login_007():
    """
    TC_LOGIN_007: Verify \"Sign up here\" link navigation
    """

    print("=" * 80)
    print("Test Case: TC_LOGIN_007")
    print("Description: Verify \"Sign up here\" link navigation")
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
            record_video_dir="../../results/TC_LOGIN_007/"
        )
        page = context.new_page()
        login_page = LoginPage(page)

        try:
            print("\nStarting test execution...\n")

            # Navigate
            login_page.navigate_to_login()

            # Click Sign Up
            current_url = page.url
            login_page.click_sign_up()

            time.sleep(2)

            # Verify URL changed to signup
            new_url = page.url
            assert "signup" in new_url.lower() or "register" in new_url.lower(), f"Not redirected to signup. URL: {new_url}"

            print("\n" + "=" * 80)
            print("PASSED: TC_LOGIN_007")
            print("=" * 80)

        except AssertionError as e:
            print("\n" + "=" * 80)
            print("FAILED: TC_LOGIN_007")
            print("Error: {e}")
            print("=" * 80)

            # Take screenshot
            screenshot_path = "../../results/TC_LOGIN_007_FAILED.png"
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
    test_tc_login_007()
