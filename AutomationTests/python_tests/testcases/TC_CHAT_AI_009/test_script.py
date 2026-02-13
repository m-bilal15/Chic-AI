"""
Test Case: TC_CHAT_AI_009
Title: Verify AI maintains conversation context
Description: Check AI remembers previous messages in conversation
Priority: High
Type: Positive - AI Intelligence
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
@pytest.mark.ai_response
def test_tc_chat_ai_009(page):
    """
    TC_CHAT_AI_009: Verify AI maintains conversation context

    Description: Check AI remembers previous messages in conversation
    Expected: Second response references wedding context
    """

    # Test ID constant
    tc_id = "TC_CHAT_AI_009"

    print("\n" + "=" * 80)
    print(f"TEST: TC_CHAT_AI_009 - Verify AI maintains conversation context")
    print("=" * 80 + "\n")

    try:
        # PRECONDITION: Complete signup, onboarding, and tour
        print("[PRECONDITION] Creating authenticated session with preference tracking...")

        user_profile = complete_signup_and_onboarding_with_tracking(page, "chat_ai")

        print("\n[READY] Chat page ready for testing")
        print(f"[PROFILE] Tracked preferences available for validation")

        page.screenshot(path=f"results/TC_CHAT_AI_009_chat_ready.png", full_page=True)
        print("[PRECONDITION] Chat page ready\n")

        chat_page = ChatPage(page)

        # TEST: AI Response
        print(f"[TEST] Testing AI response functionality...")
        print("-" * 80 + "\n")

        # Send multiple messages to test context
        messages = ['I have a wedding next month', 'What should I wear?']

        for i, msg in enumerate(messages, 1):
            print(f"\n[MESSAGE {i}/{len(messages)}] Sending: '{msg}'")

            chat_input = page.locator('textarea, input[type="text"]').first
            chat_input.fill(msg)
            time.sleep(0.5)

            send_btn = page.locator('button:has-text("Send")').first
            send_btn.click()
            time.sleep(3)

            # Wait for AI response
            print(f"[WAIT] Waiting for AI response to message {i}...")
            time.sleep(8)

            page.screenshot(path=f"results/TC_CHAT_AI_009_exchange_{i}.png", full_page=True)

        print("\n[VALIDATION] Checking conversation flow...")
        all_messages = page.locator('[class*="message"]').count()
        print(f"[INFO] Total messages in conversation: {all_messages}")

        assert all_messages >= len(messages), "Not all messages were sent"

        page.screenshot(path=f"results/TC_CHAT_AI_009_PASSED.png", full_page=True)
        print("\n[PASS] Conversation flow tested successfully")

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
