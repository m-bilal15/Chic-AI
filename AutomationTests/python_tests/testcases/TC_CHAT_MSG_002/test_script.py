"""
Test Case: TC_CHAT_MSG_002
Title: Send message using Enter key
Description: Verify Enter key sends message (keyboard shortcut)
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
def test_tc_chat_msg_002(page):
    """
    TC_CHAT_MSG_002: Send message using Enter key

    Description: Verify Enter key sends message (keyboard shortcut)
    Priority: High
    Type: Positive - Messaging

    Expected Result: Message sent via keyboard
    """

    # Test ID constant
    tc_id = "TC_CHAT_MSG_002"

    print("\n" + "=" * 80)
    print(f"TEST: TC_CHAT_MSG_002 - Send message using Enter key")
    print("=" * 80 + "\n")

    try:
        # PRECONDITION: Complete signup, onboarding, and tour
        print("[PRECONDITION] Creating authenticated session with preference tracking...")

        user_profile = complete_signup_and_onboarding_with_tracking(page, "chat_msg")

        print("\n[READY] Chat page ready for testing")
        print(f"[PROFILE] Tracked preferences available for validation")

        page.screenshot(path=f"results/TC_CHAT_MSG_002_chat_ready.png", full_page=True)
        print("[PRECONDITION] Chat page ready\n")

        # Initialize chat page object
        chat_page = ChatPage(page)

        # TEST: Messaging functionality
        print(f"[TEST] Testing: Send message using Enter key")
        print("-" * 80 + "\n")

        # Type message and press Enter
        message_text = "Quick test message"

        print(f"[STEP] Typing message: '{message_text}'")
        chat_input = page.locator('textarea, input[type="text"], [placeholder*="style" i]').first
        chat_input.fill(message_text)
        time.sleep(1)

        page.screenshot(path=f"results/TC_CHAT_MSG_002_typed.png", full_page=True)

        # Press Enter
        print("[STEP] Pressing Enter to send...")
        chat_input.press("Enter")
        time.sleep(3)

        # Verify message sent
        print("\n[VALIDATION] Verifying message sent...")
        messages = page.locator('[class*="message"]').all()

        message_found = False
        for msg in messages:
            try:
                msg_text = msg.text_content() or ""
                if message_text in msg_text:
                    message_found = True
                    print(f"[OK] Message found in chat")
                    break
            except:
                continue

        assert message_found, "Message not found after pressing Enter"

        page.screenshot(path=f"results/TC_CHAT_MSG_002_PASSED.png", full_page=True)
        print("\n[PASS] Message sent successfully via Enter key")

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
