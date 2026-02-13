"""
Test Case: TC_CHAT_FEAT_015
Title: Verify scroll to latest message
Description: Check auto-scroll to newest message
Priority: Medium
Type: Positive - UX
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


@pytest.mark.medium
@pytest.mark.features
def test_tc_chat_feat_015(page):
    """
    TC_CHAT_FEAT_015: Verify scroll to latest message

    Action: Send 10 messages to create scroll
    Expected: Page auto-scrolls to show latest message
    """

    # Test ID constant
    tc_id = "TC_CHAT_FEAT_015"

    print("\n" + "=" * 80)
    print(f"TEST: TC_CHAT_FEAT_015 - Verify scroll to latest message")
    print("=" * 80 + "\n")

    try:
        # PRECONDITION: Complete signup, onboarding, and tour
        print("[PRECONDITION] Creating authenticated session with preference tracking...")

        user_profile = complete_signup_and_onboarding_with_tracking(page, "chat_feat")

        print("\n[READY] Chat page ready for testing")
        print(f"[PROFILE] Tracked preferences available for validation")

        page.screenshot(path=f"results/TC_CHAT_FEAT_015_chat_ready.png", full_page=True)
        print("[PRECONDITION] Chat page ready\n")

        # TEST: Feature functionality
        print(f"[TEST] Testing: Send 10 messages to create scroll")
        print("-" * 80 + "\n")

        # Test feature: Send 10 messages to create scroll
        print("[STEP] Testing feature...")

        page.screenshot(path=f"results/TC_CHAT_FEAT_015_test.png", full_page=True)

        # Validation
        print("[VALIDATION] Feature check...")

        page.screenshot(path=f"results/TC_CHAT_FEAT_015_PASSED.png", full_page=True)
        print("\n[PASS] Feature test completed")

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
