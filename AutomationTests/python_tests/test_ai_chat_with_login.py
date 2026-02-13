"""
Test AI Chat Functionality with Existing Account
Login credentials: tim@gmail.com / Qwerty@123
Tests AI conversation and responses
Created: February 13, 2026
"""

from playwright.sync_api import sync_playwright
import time

def test_ai_chat():
    """Test AI chat with existing account"""

    print("\n" + "=" * 80)
    print("TESTING AI CHAT FUNCTIONALITY")
    print("=" * 80)
    print("Account: tim@gmail.com")
    print("Environment: Production (app.digitalstylist.com)")
    print("=" * 80 + "\n")

    # Test credentials
    email = "tim@gmail.com"
    password = "Qwerty@123"

    # Test messages for AI
    test_messages = [
        "Hello! Can you help me with my style?",
        "What should I wear to a wedding?",
        "What colors would look good on me?",
        "Can you recommend an outfit for a job interview?",
        "Show me some dress options"
    ]

    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()

        try:
            # ==========================================
            # STEP 1: LOGIN
            # ==========================================
            print("\n[STEP 1] Logging in...")
            print("-" * 80)

            page.goto("https://app.digitalstylist.com/login")
            page.wait_for_load_state("networkidle")
            time.sleep(2)

            page.screenshot(path="results/ai_chat_01_login_page.png", full_page=True)

            # Fill login form
            print(f"[ACTION] Entering email: {email}")
            page.fill('input[type="email"], input[name="email"]', email)
            time.sleep(1)

            print(f"[ACTION] Entering password")
            page.fill('input[type="password"], input[name="password"]', password)
            time.sleep(1)

            page.screenshot(path="results/ai_chat_02_login_filled.png", full_page=True)

            # Click Sign In
            print("[ACTION] Clicking Sign In...")
            page.click('button:has-text("Sign In"), button:has-text("Sign in"), button[type="submit"]')
            time.sleep(5)

            current_url = page.url
            print(f"[INFO] After login: {current_url}")

            page.screenshot(path="results/ai_chat_03_after_login.png", full_page=True)

            # Check if login successful
            if "login" in current_url.lower():
                print("\n[ERROR] Login failed - still on login page")
                # Check for error messages
                errors = page.locator('[class*="error"], [role="alert"]').all()
                for error in errors:
                    if error.is_visible():
                        print(f"[ERROR] {error.inner_text()}")
                print("\n[STOP] Cannot proceed without login")
                return False

            print("[OK] Login successful!\n")

            # ==========================================
            # STEP 2: NAVIGATE TO CHAT
            # ==========================================
            print("\n[STEP 2] Navigating to chat...")
            print("-" * 80)

            page.goto("https://app.digitalstylist.com/chat")
            time.sleep(5)

            # Skip/complete any tour if present
            print("[INFO] Checking for welcome tour...")
            for attempt in range(10):
                tour_btn = page.locator('button:has-text("Next"), button:has-text("Get Started"), button:has-text("Got it"), [aria-label*="close" i]')
                if tour_btn.count() > 0:
                    try:
                        btn_text = tour_btn.first.inner_text() or "Next"
                        print(f"  [TOUR] Clicking '{btn_text}'...")
                        tour_btn.first.click(timeout=2000)
                        time.sleep(2)
                    except:
                        break
                else:
                    break

            current_url = page.url
            print(f"[INFO] Current URL: {current_url}")

            page.screenshot(path="results/ai_chat_04_chat_page.png", full_page=True)

            if "chat" not in current_url.lower():
                print("[WARNING] Not on chat page")
            else:
                print("[OK] On chat page!\n")

            # ==========================================
            # STEP 3: TEST AI CHAT
            # ==========================================
            print("\n[STEP 3] Testing AI Chat Functionality")
            print("=" * 80)

            results = {
                "total_messages": len(test_messages),
                "sent_successfully": 0,
                "ai_responses": 0,
                "conversations": []
            }

            # Get initial message count
            initial_messages = page.locator('[class*="message"]').count()
            print(f"[INFO] Initial messages in chat: {initial_messages}\n")

            # Send each test message and check AI response
            for i, test_msg in enumerate(test_messages, 1):
                print(f"\n{'=' * 80}")
                print(f"CONVERSATION {i}/{len(test_messages)}")
                print('=' * 80)

                print(f"\n[USER MESSAGE {i}] {test_msg}")
                print("-" * 80)

                # Get message count before sending
                msg_count_before = page.locator('[class*="message"]').count()

                # Type message
                print(f"[ACTION] Typing message...")
                chat_input = page.locator('textarea, input[type="text"], [placeholder*="style" i]').first

                if chat_input.count() == 0:
                    print("[ERROR] Chat input not found!")
                    break

                chat_input.fill(test_msg)
                time.sleep(1)

                page.screenshot(path=f"results/ai_chat_msg{i}_typed.png", full_page=True)

                # Click Send
                print(f"[ACTION] Clicking Send button...")
                send_btn = page.locator('button:has-text("Send"), button[aria-label*="send" i], button[type="submit"], button svg, button:has([class*="send" i])').first

                if send_btn.count() == 0:
                    print("[ERROR] Send button not found!")
                    break

                send_btn.click()
                time.sleep(2)

                print(f"[OK] Message sent")
                results["sent_successfully"] += 1

                page.screenshot(path=f"results/ai_chat_msg{i}_sent.png", full_page=True)

                # Wait for AI response
                print(f"[WAIT] Waiting for AI response...")
                time.sleep(10)  # Give AI time to respond

                page.screenshot(path=f"results/ai_chat_msg{i}_ai_response.png", full_page=True)

                # Check for new messages
                msg_count_after = page.locator('[class*="message"]').count()

                print(f"[INFO] Messages before: {msg_count_before}, after: {msg_count_after}")

                if msg_count_after > msg_count_before:
                    new_messages = msg_count_after - msg_count_before
                    print(f"[OK] AI responded! ({new_messages} new message(s))")
                    results["ai_responses"] += 1

                    # Try to capture AI response text
                    try:
                        all_msgs = page.locator('[class*="message"]').all()
                        if len(all_msgs) > 0:
                            latest_msg = all_msgs[-1].text_content()
                            ai_response_preview = latest_msg[:200] if latest_msg else "Could not capture"
                            print(f"\n[AI RESPONSE Preview]:")
                            print(f"  {ai_response_preview}...")

                            results["conversations"].append({
                                "user_message": test_msg,
                                "ai_responded": True,
                                "ai_preview": ai_response_preview
                            })
                    except Exception as e:
                        print(f"[WARNING] Could not capture AI response text: {e}")
                        results["conversations"].append({
                            "user_message": test_msg,
                            "ai_responded": True,
                            "ai_preview": "Text not captured"
                        })
                else:
                    print(f"[WARNING] No AI response detected")
                    results["conversations"].append({
                        "user_message": test_msg,
                        "ai_responded": False
                    })

                print(f"\n[COMPLETE] Conversation {i} finished")

                # Small delay before next message
                time.sleep(3)

            # ==========================================
            # FINAL RESULTS
            # ==========================================
            print("\n\n" + "=" * 80)
            print("AI CHAT TEST RESULTS")
            print("=" * 80)
            print(f"Total messages sent:     {results['sent_successfully']}/{results['total_messages']}")
            print(f"AI responses received:   {results['ai_responses']}/{results['sent_successfully']}")
            print(f"Response rate:           {results['ai_responses']/results['sent_successfully']*100 if results['sent_successfully'] > 0 else 0:.1f}%")
            print("=" * 80)

            # Print conversation summary
            print("\nConversation Summary:")
            print("-" * 80)
            for i, conv in enumerate(results["conversations"], 1):
                status = "OK" if conv.get("ai_responded") else "NO RESPONSE"
                print(f"\n{i}. User: {conv['user_message']}")
                print(f"   AI: [{status}] {conv.get('ai_preview', 'N/A')[:100]}...")

            # Final screenshot
            page.screenshot(path="results/ai_chat_final.png", full_page=True)

            # Keep browser open for inspection
            print("\n" + "=" * 80)
            print("Browser will stay open for 15 seconds for inspection...")
            print("=" * 80)
            time.sleep(15)

            # Save results
            import json
            with open("results/ai_chat_test_results.json", "w") as f:
                json.dump(results, f, indent=2)

            print("\n[SAVED] Results saved to: results/ai_chat_test_results.json")

            return results

        except Exception as e:
            print(f"\n[ERROR] Test failed: {e}")
            page.screenshot(path="results/ai_chat_error.png", full_page=True)
            import traceback
            traceback.print_exc()
            return None

        finally:
            browser.close()

    print("\n" + "=" * 80)
    print("AI CHAT TEST COMPLETE")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    test_ai_chat()
