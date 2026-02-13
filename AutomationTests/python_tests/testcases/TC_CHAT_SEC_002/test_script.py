"""
Test Case: TC_CHAT_SEC_002
Title: XSS script injection in chat message
Description: Verify XSS attacks are prevented
Priority: Critical
Type: Negative - Security
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


@pytest.mark.critical
@pytest.mark.security
def test_tc_chat_sec_002(page):
    """
    TC_CHAT_SEC_002: XSS script injection in chat message

    Security test: Verify XSS attacks are prevented
    Expected: Script tags sanitized, no execution
    """

    # Test ID constant
    tc_id = "TC_CHAT_SEC_002"

    print("\n" + "=" * 80)
    print(f"SECURITY TEST: TC_CHAT_SEC_002 - XSS script injection in chat message")
    print("=" * 80 + "\n")

    try:
        # PRECONDITION: Complete signup, onboarding, and tour
        print("[PRECONDITION] Creating authenticated session with preference tracking...")

        user_profile = complete_signup_and_onboarding_with_tracking(page, "chat_sec")

        print("\n[READY] Chat page ready for testing")
        print(f"[PROFILE] Tracked preferences available for validation")

        page.screenshot(path=f"results/TC_CHAT_SEC_002_chat_ready.png", full_page=True)
        print("[PRECONDITION] Chat page ready\n")

        chat_page = ChatPage(page)

        # SECURITY TEST: Attempt injection
        malicious_payload = "<script>alert('XSS')</script>"

        print(f"[SECURITY TEST] Attempting injection...")
        print(f"[PAYLOAD] {malicious_payload}")

        # Type malicious payload
        chat_input = page.locator('textarea, input[type="text"]').first
        chat_input.fill(malicious_payload)
        time.sleep(1)

        page.screenshot(path=f"results/TC_CHAT_SEC_002_payload_entered.png", full_page=True)

        # Send
        page.locator('button:has-text("Send")').first.click()
        time.sleep(3)

        page.screenshot(path=f"results/TC_CHAT_SEC_002_payload_sent.png", full_page=True)

        # VALIDATION: Check payload was sanitized
        print("\n[VALIDATION] Checking payload was sanitized...")

        # Get page source
        page_source = page.content()

        # Check if script tags are in HTML (should be escaped/sanitized)
        if "<script>" in page_source and "alert" in page_source:
            # Script not sanitized - SECURITY ISSUE
            assert False, "SECURITY VULNERABILITY: Script was not sanitized!"
        else:
            print("[OK] Malicious payload sanitized - no script execution")

        # Check message appears as plain text
        messages = page.locator('[class*="message"]').all()
        payload_found_as_text = False

        for msg in messages:
            msg_text = msg.inner_text()
            # Should contain the text but not execute
            if malicious_payload[:20] in msg_text:
                payload_found_as_text = True
                print(f"[OK] Payload displayed as plain text")
                break

        page.screenshot(path=f"results/TC_CHAT_SEC_002_PASSED.png", full_page=True)
        print("\n[PASS] Security test passed - injection prevented")

    except AssertionError as e:
        page.screenshot(path=f"results/TC_CHAT_SEC_002_FAILED.png", full_page=True)
        print(f"\n[FAIL] SECURITY ISSUE: {e}")
        raise

    except Exception as e:
        page.screenshot(path=f"results/TC_CHAT_SEC_002_ERROR.png", full_page=True)
        print(f"\n[ERROR] {e}")
        raise

    finally:
        print("\n" + "=" * 80)
        print(f"SECURITY TEST TC_CHAT_SEC_002 COMPLETE")
        print("=" * 80 + "\n")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
