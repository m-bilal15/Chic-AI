"""
AI Chat Model - Single Conversation Test
Tests AI responses properly by waiting for actual replies
Uses: tim@gmail.com
Created: February 13, 2026
"""

from playwright.sync_api import sync_playwright
import time
from datetime import datetime

def test_ai_single_conversation():
    """Test AI chat with proper wait for responses"""

    print("\n" + "=" * 80)
    print("AI CHAT - SINGLE CONVERSATION TEST")
    print("=" * 80)
    print("Focus: Send message, wait for ACTUAL AI response, validate")
    print("=" * 80 + "\n")

    email = "tim@gmail.com"
    password = "Qwerty@123"

    # Test question
    test_question = "What should I wear to a wedding?"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        try:
            # Login
            print("[STEP 1] Logging in...")
            page.goto("https://app.digitalstylist.com/login")
            time.sleep(2)

            page.fill('input[type="email"]', email)
            page.fill('input[type="password"]', password)
            page.click('button[type="submit"]')
            time.sleep(5)

            # Go to chat
            print("[STEP 2] Navigating to chat...")
            page.goto("https://app.digitalstylist.com/chat")
            time.sleep(5)

            # Handle modals
            print("[STEP 3] Handling modals...")
            for _ in range(15):
                btn = page.locator('button:has-text("Next"), button:has-text("Get Started"), button:has-text("Start Trial"), [aria-label*="close"]').first
                if btn.count() > 0:
                    try:
                        btn.click(timeout=2000)
                        time.sleep(2)
                    except:
                        break
                else:
                    break

            page.screenshot(path="results/single_conv_01_ready.png", full_page=True)
            print("[OK] Chat ready\n")

            # Wait for initial AI greeting
            print("[STEP 4] Waiting for initial AI greeting...")
            time.sleep(5)

            page.screenshot(path="results/single_conv_02_greeting.png", full_page=True)

            # Count initial messages
            initial_msgs = page.locator('[class*="message"]').all()
            print(f"[INFO] Initial messages: {len(initial_msgs)}")

            for i, msg in enumerate(initial_msgs):
                try:
                    text = msg.text_content()[:100]
                    print(f"  Message {i+1}: {text}...")
                except:
                    pass

            # Now send our test question
            print(f"\n[STEP 5] Sending test question...")
            print(f"[USER] {test_question}")
            print("-" * 80)

            # Type message
            chat_input = page.locator('textarea, input[placeholder*="style"]').first
            chat_input.fill(test_question)
            time.sleep(2)

            page.screenshot(path="results/single_conv_03_typed.png", full_page=True)

            # Click send
            print("[ACTION] Clicking Send...")
            send_btn = page.locator('button[type="submit"], button svg').first
            send_btn.click()
            time.sleep(3)

            page.screenshot(path="results/single_conv_04_sent.png", full_page=True)
            print("[OK] Message sent\n")

            # Wait for AI response with proper polling
            print("[STEP 6] Waiting for AI response...")
            print("-" * 80)

            initial_count = len(initial_msgs)
            ai_responded = False
            start_time = time.time()
            max_wait = 60  # 60 seconds max

            while (time.time() - start_time) < max_wait:
                current_msgs = page.locator('[class*="message"]').all()
                current_count = len(current_msgs)

                elapsed = time.time() - start_time
                print(f"  [{elapsed:.0f}s] Messages: {current_count} (initial: {initial_count})")

                if current_count > initial_count + 1:  # User message + AI response
                    ai_responded = True
                    print(f"\n[SUCCESS] AI responded after {elapsed:.1f} seconds!")
                    break

                time.sleep(2)  # Check every 2 seconds

                # Take screenshot every 10 seconds
                if int(elapsed) % 10 == 0:
                    page.screenshot(path=f"results/single_conv_wait_{int(elapsed)}s.png", full_page=True)

            # Final screenshot
            page.screenshot(path="results/single_conv_05_final.png", full_page=True)

            # Capture all messages
            print("\n[STEP 7] Capturing conversation...")
            print("-" * 80)

            all_msgs = page.locator('[class*="message"]').all()
            print(f"[INFO] Total messages in conversation: {len(all_msgs)}\n")

            conversation = []
            for i, msg in enumerate(all_msgs):
                try:
                    text = msg.text_content()
                    sender = "AI" if i % 2 == 0 else "User"  # Assuming alternating
                    conversation.append({
                        "sender": sender,
                        "text": text
                    })
                    print(f"[{sender}] {text[:150]}...")
                    print()
                except:
                    pass

            # Analysis
            print("\n" + "=" * 80)
            print("ANALYSIS")
            print("=" * 80)

            if ai_responded:
                print(f"[PASS] AI responded to the question")

                # Get AI's response (should be last message)
                if len(all_msgs) > 0:
                    ai_response = all_msgs[-1].text_content()

                    # Check for keywords
                    keywords_found = []
                    required_keywords = ["wedding", "dress", "outfit", "formal", "style"]

                    for kw in required_keywords:
                        if kw.lower() in ai_response.lower():
                            keywords_found.append(kw)

                    print(f"\n[VALIDATION] Keywords found: {keywords_found}")
                    print(f"[VALIDATION] Response length: {len(ai_response)} characters")

                    if len(keywords_found) >= 2:
                        print(f"\n[PASS] AI provided relevant wedding styling advice!")
                    else:
                        print(f"\n[WARNING] AI response may not be specific enough")

            else:
                print(f"[FAIL] AI did not respond within {max_wait} seconds")

            print("=" * 80)

            # Keep browser open
            print("\nBrowser staying open for 30 seconds for review...")
            time.sleep(30)

        except Exception as e:
            print(f"\n[ERROR] {e}")
            page.screenshot(path="results/single_conv_error.png", full_page=True)
            import traceback
            traceback.print_exc()

        finally:
            browser.close()

    print("\n" + "=" * 80)
    print("TEST COMPLETE")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    test_ai_single_conversation()
