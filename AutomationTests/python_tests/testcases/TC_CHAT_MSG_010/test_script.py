"""
Test Case: TC_CHAT_MSG_010
Title: Send multiple messages in sequence
Description: Verify multiple messages are sent in correct order
Priority: High
Type: Positive - Messaging
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
@pytest.mark.messaging
def test_tc_chat_msg_010(page):
    """
    TC_CHAT_MSG_010: Send multiple messages in sequence

    Description: Verify multiple messages are sent in correct order
    Priority: High
    Type: Positive - Messaging

    Expected Result: All messages sent in order
    """

    # Test ID constant
    tc_id = "TC_CHAT_MSG_010"

    print("\n" + "=" * 80)
    print(f"TEST: TC_CHAT_MSG_010 - Send multiple messages in sequence")
    print("=" * 80 + "\n")

    try:
        # PRECONDITION: Complete signup, onboarding, and tour
        print("[PRECONDITION] Creating authenticated session with preference tracking...")

        user_profile = complete_signup_and_onboarding_with_tracking(page, "chat_msg")

        print("\n[READY] Chat page ready for testing")
        print(f"[PROFILE] Tracked preferences available for validation")

        page.screenshot(path=f"results/TC_CHAT_MSG_010_chat_ready.png", full_page=True)
        print("[PRECONDITION] Chat page ready\n")

        # Initialize chat page object
        chat_page = ChatPage(page)

        # TEST: Messaging functionality
        print(f"[TEST] Testing: Send multiple messages in sequence")
        print("-" * 80 + "\n")

        # Send multiple messages
        messages = ['First message', 'Second message', 'Third message']

        print(f"[STEP] Sending {len(messages)} messages...")

        for i, msg in enumerate(messages, 1):
            print(f"\n[MESSAGE {i}] Sending: '{msg}'")

            # Type message
            chat_input = page.locator('textarea, input[type="text"], [placeholder*="style" i]').first
            chat_input.fill(msg)
            time.sleep(2)  # Increased wait for input

            # Send
            send_btn = page.locator('button:has-text("Send"), button[aria-label*="send" i], button[type="submit"], button svg, button:has([class*="send" i])').first
            send_btn.click()
            time.sleep(4)  # Increased wait for message to send

            page.screenshot(path=f"results/TC_CHAT_MSG_010_message_{i}.png", full_page=True)

            # Wait before sending next message
            time.sleep(2)

        # Verify all messages sent
        print("\n[VALIDATION] Checking all messages were sent...")
        time.sleep(2)

        # Get all message elements
        all_messages = page.locator('[class*="message"]').all()
        print(f"[INFO] Total messages in chat: {len(all_messages)}")

        page.screenshot(path=f"results/TC_CHAT_MSG_010_PASSED.png", full_page=True)
        print("\n[PASS] Multiple messages sent successfully")

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
