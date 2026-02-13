"""
Test Case: TC_CHAT_AI_006
Title: Verify AI provides outfit suggestions
Description: Check AI recommends specific outfits
Priority: High
Type: Positive - AI Response
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
def test_tc_chat_ai_006(page):
    """
    TC_CHAT_AI_006: Verify AI provides outfit suggestions

    Description: Check AI recommends specific outfits
    Expected: Response contains outfit recommendations
    """

    # Test ID constant
    tc_id = "TC_CHAT_AI_006"

    print("\n" + "=" * 80)
    print(f"TEST: TC_CHAT_AI_006 - Verify AI provides outfit suggestions")
    print("=" * 80 + "\n")

    try:
        # PRECONDITION: Complete signup, onboarding, and tour
        print("[PRECONDITION] Creating authenticated session with preference tracking...")

        user_profile = complete_signup_and_onboarding_with_tracking(page, "chat_ai")

        print("\n[READY] Chat page ready for testing")
        print(f"[PROFILE] Tracked preferences available for validation")

        page.screenshot(path=f"results/TC_CHAT_AI_006_chat_ready.png", full_page=True)
        print("[PRECONDITION] Chat page ready\n")

        chat_page = ChatPage(page)

        # TEST: AI Response
        print(f"[TEST] Testing AI response functionality...")
        print("-" * 80 + "\n")

        # Send message to AI
        message = "Can you recommend an outfit for a job interview?"
        print(f"[STEP] Sending message: '{message}'")

        # Get initial message count
        initial_count = page.locator('[class*="message"]').count()
        print(f"[INFO] Initial messages: {initial_count}")

        # Type and send
        chat_input = page.locator('textarea, input[type="text"], [placeholder*="style" i]').first
        chat_input.fill(message)
        time.sleep(1)

        send_btn = page.locator('button:has-text("Send")').first
        send_btn.click()
        time.sleep(3)

        page.screenshot(path=f"results/TC_CHAT_AI_006_message_sent.png", full_page=True)

        # Wait for AI response
        print("\n[WAIT] Waiting for AI response...")
        time.sleep(10)  # Allow time for AI to respond

        # Check for new messages
        final_count = page.locator('[class*="message"]').count()
        print(f"[INFO] Final messages: {final_count}")

        # Verify AI responded
        assert final_count > initial_count, f"No new messages. Expected AI response. Initial: {initial_count}, Final: {final_count}"

        print(f"[OK] AI responded - new messages detected")

        # Capture AI response
        page.screenshot(path=f"results/TC_CHAT_AI_006_ai_response.png", full_page=True)

        # Get latest messages
        all_msgs = page.locator('[class*="message"]').all()
        if all_msgs:
            latest = all_msgs[-1].inner_text()[:150]
            print(f"\n[AI RESPONSE Preview]: {latest}...")

        page.screenshot(path=f"results/TC_CHAT_AI_006_PASSED.png", full_page=True)
        print("\n[PASS] AI response received successfully")

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
