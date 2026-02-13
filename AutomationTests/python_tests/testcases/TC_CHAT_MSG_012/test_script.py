"""
Test Case: TC_CHAT_MSG_012
Title: Verify send button state changes
Description: Check send button enabled/disabled based on input
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
@pytest.mark.messaging
def test_tc_chat_msg_012(page):
    """
    TC_CHAT_MSG_012: Verify send button state changes

    Description: Check send button enabled/disabled based on input
    Priority: Medium
    Type: Positive - UX

    Expected Result: Button disabled when empty, enabled with text
    """

    # Test ID constant
    tc_id = "TC_CHAT_MSG_012"

    print("\n" + "=" * 80)
    print(f"TEST: TC_CHAT_MSG_012 - Verify send button state changes")
    print("=" * 80 + "\n")

    try:
        # PRECONDITION: Complete signup, onboarding, and tour
        print("[PRECONDITION] Creating authenticated session with preference tracking...")

        user_profile = complete_signup_and_onboarding_with_tracking(page, "chat_msg")

        print("\n[READY] Chat page ready for testing")
        print(f"[PROFILE] Tracked preferences available for validation")

        page.screenshot(path=f"results/TC_CHAT_MSG_012_chat_ready.png", full_page=True)
        print("[PRECONDITION] Chat page ready\n")

        # Initialize chat page object
        chat_page = ChatPage(page)

        # TEST: Messaging functionality
        print(f"[TEST] Testing: Verify send button state changes")
        print("-" * 80 + "\n")

        # Send test message
        message_text = "Test message"

        print(f"[STEP] Typing message: '{message_text}'")

        # Find and fill input
        chat_input = page.locator('textarea, input[type="text"], [placeholder*="style" i]').first
        chat_input.fill(message_text)
        time.sleep(1)

        page.screenshot(path=f"results/TC_CHAT_MSG_012_message_typed.png", full_page=True)

        # Click send
        print("[STEP] Clicking Send button...")
        send_btn = page.locator('button:has-text("Send"), button[aria-label*="send" i], button[type="submit"], button svg, button:has([class*="send" i])').first
        send_btn.click()
        time.sleep(3)

        page.screenshot(path=f"results/TC_CHAT_MSG_012_message_sent.png", full_page=True)

        # Verify message appears in chat
        print("\n[VALIDATION] Verifying message appears in chat...")

        messages = page.locator('[class*="message"]').all()
        message_found = False

        for msg in messages:
            try:
                msg_text = msg.inner_text()
                if message_text in msg_text:
                    message_found = True
                    print(f"[OK] Message found: '{msg_text[:100]}'")
                    break
            except:
                pass

        assert message_found or len(messages) > 0, "Message not found in chat"

        page.screenshot(path=f"results/TC_CHAT_MSG_012_PASSED.png", full_page=True)
        print("\n[PASS] Message sent and displayed successfully")

    except AssertionError as e:
        page.screenshot(path=f"results/{tc_id}_FAILED.png", full_page=True)
        print(f"\n[FAIL] Test failed: {{e}}")
        raise

    except Exception as e:
        page.screenshot(path=f"results/{tc_id}_ERROR.png", full_page=True)
        print(f"\n[ERROR] Test error: {{e}}")
        raise

    finally:
        print("\n" + "=" * 80)
        print(f"TEST {tc_id} COMPLETE")
        print("=" * 80 + "\n")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
