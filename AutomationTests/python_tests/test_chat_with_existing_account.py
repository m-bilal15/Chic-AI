"""
Test Chat Functionality with Existing Account
Login: tim@gmail.com / Qwerty@123
No signup - direct login and chat testing
Created: February 13, 2026
"""

from playwright.sync_api import sync_playwright
import time

def test_chat_with_login():
    """Test chat messaging and AI with existing account"""

    print("\n" + "=" * 80)
    print("CHAT FUNCTIONALITY TEST - WITH EXISTING ACCOUNT")
    print("=" * 80)
    print("Account: tim@gmail.com")
    print("Method: LOGIN (no signup)")
    print("=" * 80 + "\n")

    # Credentials
    email = "tim@gmail.com"
    password = "Qwerty@123"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=800)
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        try:
            # ==========================================
            # STEP 1: LOGIN
            # ==========================================
            print("[STEP 1] Logging in...")
            print("-" * 80)

            page.goto("https://app.digitalstylist.com/login")
            time.sleep(3)

            # Fill login form
            print(f"  Email: {email}")
            page.fill('input[type="email"]', email)
            time.sleep(1)

            print(f"  Password: ***")
            page.fill('input[type="password"]', password)
            time.sleep(1)

            page.screenshot(path="results/login_test_01_filled.png", full_page=True)

            # Click Sign In
            print("  Clicking Sign In...")
            page.click('button:has-text("Sign In"), button[type="submit"]')
            time.sleep(5)

            print(f"[OK] Login attempted\n")

            # ==========================================
            # STEP 2: NAVIGATE TO CHAT
            # ==========================================
            print("[STEP 2] Navigating to chat...")
            print("-" * 80)

            page.goto("https://app.digitalstylist.com/chat")
            time.sleep(5)

            page.screenshot(path="results/login_test_02_after_nav.png", full_page=True)

            # Handle any modals (tour, paywall, etc.)
            print("  Handling any modals...")

            for attempt in range(15):
                # Check for different modal types
                modal_buttons = page.locator('button:has-text("Next"), button:has-text("Get Started"), button:has-text("Start Trial"), button:has-text("Got it"), [aria-label*="close" i]')

                if modal_buttons.count() > 0:
                    try:
                        btn_text = modal_buttons.first.inner_text() or "button"
                        print(f"    Clicking '{btn_text}'...")
                        modal_buttons.first.click(timeout=2000)
                        time.sleep(2)
                    except:
                        break
                else:
                    break

            page.screenshot(path="results/login_test_03_chat_ready.png", full_page=True)
            print(f"[OK] Chat page ready\n")

            # ==========================================
            # STEP 3: TEST MESSAGING
            # ==========================================
            print("[STEP 3] Testing Chat Messaging")
            print("=" * 80 + "\n")

            test_messages = [
                "Hello! Can you help me with my style?",
                "What should I wear to a wedding?",
                "What colors look good on me?",
            ]

            results = {"sent": 0, "validated": 0}

            for i, msg in enumerate(test_messages, 1):
                print(f"\n[MESSAGE {i}/{len(test_messages)}]")
                print("-" * 80)
                print(f"User: {msg}")

                # Type message
                chat_input = page.locator('textarea, input[placeholder*="style" i]').first

                if chat_input.count() == 0:
                    print("[ERROR] Chat input not found!")
                    break

                chat_input.fill(msg)
                time.sleep(1)

                # Click send
                send_btn = page.locator('button[type="submit"], button svg, button:has-text("Send")').first

                if send_btn.count() == 0:
                    print("[ERROR] Send button not found!")
                    break

                send_btn.click()
                time.sleep(2)

                print(f"  [OK] Message sent")
                results["sent"] += 1

                page.screenshot(path=f"results/login_test_msg{i}_sent.png", full_page=True)

                # Wait for AI response
                print(f"  [WAIT] Waiting for AI response...")
                time.sleep(10)

                # Capture response
                all_msgs = page.locator('[class*="message"]').all()
                if len(all_msgs) > 0:
                    try:
                        latest = all_msgs[-1].text_content()
                        print(f"  [AI] {latest[:150]}...")
                        results["validated"] += 1
                    except:
                        print(f"  [AI] Response detected (text not captured)")

                page.screenshot(path=f"results/login_test_msg{i}_response.png", full_page=True)

                print(f"  [COMPLETE] Conversation {i} finished\n")

                time.sleep(2)

            # ==========================================
            # SUMMARY
            # ==========================================
            print("\n" + "=" * 80)
            print("TEST RESULTS")
            print("=" * 80)
            print(f"Messages sent:     {results['sent']}/{len(test_messages)}")
            print(f"Responses seen:    {results['validated']}/{results['sent']}")
            print("=" * 80)

            if results['sent'] == len(test_messages):
                print("\n[SUCCESS] All messages sent successfully!")
            else:
                print(f"\n[WARNING] Only {results['sent']}/{len(test_messages)} sent")

            # Final screenshot
            page.screenshot(path="results/login_test_final.png", full_page=True)

            # Keep browser open
            print("\nBrowser will stay open for 15 seconds...")
            time.sleep(15)

            return True

        except Exception as e:
            print(f"\n[ERROR] Test failed: {e}")
            page.screenshot(path="results/login_test_error.png", full_page=True)
            import traceback
            traceback.print_exc()
            return False

        finally:
            browser.close()

    print("\n" + "=" * 80)
    print("TEST COMPLETE")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    test_chat_with_login()
