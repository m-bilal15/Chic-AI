"""
Test Case: TC_CHAT_FEAT_005
Title: Navigate to My Wardrobe from sidebar
Description: Verify My Wardrobe menu navigation
Priority: High
Type: Positive - Navigation
Created: February 12, 2026
"""

import pytest
import time
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from auth_helper import complete_signup_and_onboarding_with_tracking
from pages.chat_page import ChatPage


@pytest.mark.high
@pytest.mark.features
def test_tc_chat_feat_005(page):
    """
    TC_CHAT_FEAT_005: Navigate to My Wardrobe from sidebar

    Action: Click 'My Wardrobe'
    Expected: Navigates to wardrobe page
    """

    # Test ID constant
    tc_id = "TC_CHAT_FEAT_005"

    print("\n" + "=" * 80)
    print(f"TEST: TC_CHAT_FEAT_005 - Navigate to My Wardrobe from sidebar")
    print("=" * 80 + "\n")

    try:
        # PRECONDITION: Complete signup, onboarding, and tour
        print("[PRECONDITION] Creating authenticated session with preference tracking...")

        user_profile = complete_signup_and_onboarding_with_tracking(page, "chat_feat")

        print("\n[READY] Chat page ready for testing")
        print(f"[PROFILE] Tracked preferences available for validation")

        page.screenshot(path=f"results/TC_CHAT_FEAT_005_chat_ready.png", full_page=True)
        print("[PRECONDITION] Chat page ready\n")

        # TEST: Feature functionality
        print(f"[TEST] Testing: Click 'My Wardrobe'")
        print("-" * 80 + "\n")

        # Navigate to Wardrobe
        print(f"[STEP] Clicking '{menu_item}' in sidebar...")

        menu_link = page.locator('a:has-text("Wardrobe"), button:has-text("Wardrobe")')
        assert menu_link.count() > 0, "Wardrobe menu not found"

        initial_url = page.url
        menu_link.first.click()
        time.sleep(3)

        final_url = page.url
        print(f"[INFO] Initial URL: {initial_url}")
        print(f"[INFO] Final URL: {final_url}")

        page.screenshot(path=f"results/{tc_id}_navigation.png", full_page=True)

        # Verify navigation occurred or modal opened
        navigation_occurred = (final_url != initial_url) or page.locator('[role="dialog"], [class*="modal"]').count() > 0
        assert navigation_occurred, "Navigation did not occur"

        page.screenshot(path=f"results/{tc_id}_PASSED.png", full_page=True)
        print("\n[PASS] Navigation to Wardrobe successful")

    except AssertionError as e:
        page.screenshot(path=f"results/{tc_id}_FAILED.png", full_page=True)
        print(f"\n[FAIL] {{e}}")
        raise

    except Exception as e:
        page.screenshot(path=f"results/{tc_id}_ERROR.png", full_page=True)
        print(f"\n[ERROR] {{e}}")
        raise

    finally:
        print("\n" + "=" * 80)
        print(f"TEST {tc_id} COMPLETE")
        print("=" * 80 + "\n")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
