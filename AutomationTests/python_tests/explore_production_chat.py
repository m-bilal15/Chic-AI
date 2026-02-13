"""
Explore Production Chat Page
Access live app: https://app.digitalstylist.com/chat
Complete signup flow to access chat
Created: February 12, 2026
"""

from playwright.sync_api import sync_playwright
import time
import random
import json

def generate_unique_email():
    """Generate unique email for testing"""
    timestamp = int(time.time())
    random_num = random.randint(1000, 9999)
    return f"chattest_{timestamp}_{random_num}@testmail.com"

def explore_production_chat():
    """Complete signup flow and explore production chat page"""

    print("\n" + "=" * 80)
    print("EXPLORING PRODUCTION CHAT PAGE")
    print("=" * 80)
    print("URL: https://app.digitalstylist.com/chat")
    print("Flow: Signup > Onboarding > Dashboard/Chat")
    print("=" * 80 + "\n")

    # Generate test account
    test_email = generate_unique_email()
    test_password = "ChatTest@2026"
    test_name = "Chat Test User"

    print(f"[INFO] Creating test account:")
    print(f"  Email: {test_email}")
    print(f"  Password: {test_password}")
    print(f"  Name: {test_name}\n")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()

        findings = {
            "url": "https://app.digitalstylist.com/chat",
            "chat_elements": [],
            "selectors": {},
            "features": [],
            "messages": [],
            "flow_completed": []
        }

        try:
            # PHASE 1: Navigate and Signup
            print("=" * 80)
            print("PHASE 1: SIGNUP")
            print("=" * 80 + "\n")

            print("[STEP] Navigating to app...")
            page.goto("https://app.digitalstylist.com")
            page.wait_for_load_state("networkidle")
            time.sleep(2)

            current_url = page.url
            print(f"[INFO] Current URL: {current_url}")

            page.screenshot(path="results/prod_chat_01_initial.png", full_page=True)

            # Navigate to signup
            print("\n[STEP] Accessing signup page...")
            if "login" in current_url.lower():
                # Click "Sign up here" link
                signup_link = page.locator('a:has-text("Sign up"), button:has-text("Sign up")')
                if signup_link.count() > 0:
                    print("[ACTION] Clicking 'Sign up' link...")
                    signup_link.first.click()
                    time.sleep(2)

            # Fill signup form
            print("\n[STEP] Filling signup form...")

            # Try different selector patterns for full name
            name_filled = False
            name_selectors = [
                'input[name="fullName"]',
                'input[name="name"]',
                'input[name="full_name"]',
                'input[placeholder*="name" i]',
                'input[type="text"]'
            ]

            for selector in name_selectors:
                try:
                    if page.locator(selector).count() > 0:
                        print(f"  [FOUND] Name field: {selector}")
                        page.fill(selector, test_name)
                        name_filled = True
                        break
                except:
                    continue

            if not name_filled:
                print("  [WARNING] Could not find name field")

            # Fill email
            page.fill('input[type="email"], input[name="email"]', test_email)
            print(f"  [OK] Email: {test_email}")

            # Fill password
            page.fill('input[name="password"]:not([name*="confirm"])', test_password)
            print(f"  [OK] Password: {test_password}")

            # Fill confirm password
            confirm_selectors = [
                'input[name="confirmPassword"]',
                'input[name="confirm_password"]',
                'input[name="password_confirmation"]'
            ]

            for selector in confirm_selectors:
                try:
                    if page.locator(selector).count() > 0:
                        page.fill(selector, test_password)
                        print(f"  [OK] Confirm Password")
                        break
                except:
                    continue

            page.screenshot(path="results/prod_chat_02_signup_filled.png", full_page=True)

            # Submit signup
            print("\n[STEP] Submitting signup...")
            page.click('button[type="submit"], button:has-text("Create"), button:has-text("Sign up")')
            time.sleep(5)

            current_url = page.url
            print(f"[INFO] After signup: {current_url}")
            page.screenshot(path="results/prod_chat_03_after_signup.png", full_page=True)

            findings["flow_completed"].append("Signup")

            # PHASE 2: Onboarding (Quick completion)
            print("\n" + "=" * 80)
            print("PHASE 2: ONBOARDING QUESTIONNAIRE")
            print("=" * 80 + "\n")

            if "onboarding" in current_url.lower() or "questionnaire" in current_url.lower():
                print("[INFO] On onboarding page - completing quickly...")

                # Complete 5 steps
                for step in range(1, 6):
                    print(f"\n[STEP {step}] Selecting options...")
                    time.sleep(2)

                    # Click first few options
                    clickable = page.locator('button:not([disabled]), [role="button"]:not([disabled])').all()
                    clicks = min(2, len(clickable))  # Click 1-2 options

                    for i in range(clicks):
                        try:
                            if clickable[i].is_visible():
                                clickable[i].click()
                                time.sleep(0.5)
                        except:
                            pass

                    page.screenshot(path=f"results/prod_chat_04_onboarding_step{step}.png")

                    # Click Continue/Next/Complete
                    continue_btns = page.locator('button:has-text("Continue"), button:has-text("Next"), button:has-text("Complete"), button:has-text("Finish")')
                    if continue_btns.count() > 0:
                        continue_btns.first.click()
                        time.sleep(3)
                    else:
                        break

                findings["flow_completed"].append("Onboarding")
                print("\n[SUCCESS] Onboarding completed")

            # PHASE 3: Skip Welcome Tour
            print("\n" + "=" * 80)
            print("PHASE 3: DASHBOARD/WELCOME TOUR")
            print("=" * 80 + "\n")

            time.sleep(3)
            current_url = page.url
            print(f"[INFO] Current URL: {current_url}")
            page.screenshot(path="results/prod_chat_05_after_onboarding.png", full_page=True)

            # Skip tour if present
            for attempt in range(5):
                skip_btns = page.locator('button:has-text("Skip"), button:has-text("Close"), button:has-text("Got it"), button:has-text("Next")')
                if skip_btns.count() > 0:
                    skip_btns.first.click()
                    time.sleep(1)
                else:
                    break

            findings["flow_completed"].append("Dashboard")

            # PHASE 4: Access Chat
            print("\n" + "=" * 80)
            print("PHASE 4: ACCESSING CHAT PAGE")
            print("=" * 80 + "\n")

            print("[STEP] Navigating to chat...")
            page.goto("https://app.digitalstylist.com/chat")
            time.sleep(5)

            current_url = page.url
            print(f"[INFO] Chat URL: {current_url}")

            if "chat" in current_url.lower():
                print("[SUCCESS] Accessed chat page!")
                findings["flow_completed"].append("Chat accessed")
            else:
                print(f"[WARNING] Not on chat page. Current: {current_url}")

            page.screenshot(path="results/prod_chat_06_chat_page.png", full_page=True)

            # PHASE 5: Analyze Chat Page
            print("\n" + "=" * 80)
            print("PHASE 5: ANALYZING CHAT PAGE")
            print("=" * 80 + "\n")

            # Page info
            title = page.title()
            print(f"[INFO] Page Title: {title}")

            # Visible text
            print("\n[CONTENT] Visible Text:")
            print("-" * 80)
            body_text = page.locator('body').inner_text()
            lines = [line.strip() for line in body_text.split('\n') if line.strip()]
            for i, line in enumerate(lines[:30], 1):
                print(f"  {i}. {line}")
            if len(lines) > 30:
                print(f"  ... and {len(lines) - 30} more lines")

            # Analyze chat elements
            print("\n[ANALYSIS] Chat Elements:")
            print("-" * 80)

            chat_elements = {
                "Chat Input (textarea)": "textarea",
                "Chat Input (text)": 'input[type="text"]',
                "Chat Input (contenteditable)": '[contenteditable="true"]',
                "Send Button": 'button:has-text("Send"), button[type="submit"]',
                "Messages": '[class*="message"], [class*="chat"]',
                "User Avatar": '[class*="avatar"], [class*="profile"]',
                "Navigation": 'nav, [role="navigation"]',
                "Buttons": 'button',
                "Links": 'a',
                "Images": 'img'
            }

            for name, selector in chat_elements.items():
                count = page.locator(selector).count()
                if count > 0:
                    print(f"  [FOUND] {name}: {count} element(s)")
                    findings["chat_elements"].append(name)
                    findings["selectors"][name] = selector

                    # Get details
                    try:
                        first = page.locator(selector).first
                        if first.is_visible():
                            if "input" in name.lower() or "textarea" in name.lower():
                                placeholder = first.get_attribute("placeholder")
                                if placeholder:
                                    print(f"    Placeholder: '{placeholder}'")
                    except:
                        pass
                else:
                    print(f"  [NOT FOUND] {name}")

            # Test sending a message
            print("\n[TEST] Attempting to send test message...")
            print("-" * 80)

            # Find input
            input_selector = None
            for sel in ["textarea", 'input[type="text"]', '[contenteditable="true"]']:
                if page.locator(sel).count() > 0:
                    input_selector = sel
                    print(f"[FOUND] Input: {sel}")
                    break

            if input_selector:
                try:
                    test_msg = "Hello! Can you help me with my style?"
                    print(f"[ACTION] Typing: '{test_msg}'")

                    page.locator(input_selector).first.fill(test_msg)
                    time.sleep(2)

                    page.screenshot(path="results/prod_chat_07_message_typed.png", full_page=True)

                    # Click send
                    send_btn = page.locator('button:has-text("Send"), button[type="submit"]').first
                    if send_btn.is_visible():
                        print("[ACTION] Clicking send...")
                        send_btn.click()
                        time.sleep(5)

                        page.screenshot(path="results/prod_chat_08_message_sent.png", full_page=True)
                        findings["messages"].append("User: " + test_msg)

                        # Wait for AI response
                        print("[WAIT] Waiting for AI response...")
                        time.sleep(10)

                        page.screenshot(path="results/prod_chat_09_ai_response.png", full_page=True)

                        # Check messages
                        messages = page.locator('[class*="message"]').all()
                        print(f"\n[INFO] Total messages visible: {len(messages)}")

                        for i, msg in enumerate(messages[:10], 1):
                            try:
                                text = msg.inner_text().strip()[:100]
                                print(f"  Message {i}: {text}")
                                findings["messages"].append(text)
                            except:
                                pass

                        findings["features"].append("Successfully sent and received messages")

                except Exception as e:
                    print(f"[ERROR] Failed to send message: {e}")
            else:
                print("[SKIP] No input field found")

            # Save page source
            print("\n[SAVE] Saving page source...")
            html = page.content()
            with open("results/prod_chat_page_source.html", "w", encoding="utf-8") as f:
                f.write(html)
            print("  Saved: results/prod_chat_page_source.html")

            # Save findings
            with open("results/prod_chat_findings.json", "w", encoding="utf-8") as f:
                json.dump(findings, f, indent=2)
            print("  Saved: results/prod_chat_findings.json")

            # Final screenshot
            page.screenshot(path="results/prod_chat_10_final.png", full_page=True)

            # Keep browser open
            print("\n" + "=" * 80)
            print("EXPLORATION COMPLETE")
            print("=" * 80)
            print("Browser will stay open for 30 seconds for manual inspection...")
            print("=" * 80 + "\n")
            time.sleep(30)

        except Exception as e:
            print(f"\n[ERROR] Exploration failed: {e}")
            page.screenshot(path="results/prod_chat_error.png", full_page=True)
            import traceback
            traceback.print_exc()

        finally:
            browser.close()

    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"\nFlow completed: {' > '.join(findings['flow_completed'])}")
    print(f"\nElements found: {len(findings['chat_elements'])}")
    for elem in findings['chat_elements']:
        print(f"  - {elem}")

    print(f"\nFeatures tested: {len(findings['features'])}")
    for feature in findings['features']:
        print(f"  - {feature}")

    print(f"\nMessages captured: {len(findings['messages'])}")

    print("\n[FILES CREATED]")
    print("  Screenshots: results/prod_chat_*.png")
    print("  Page source: results/prod_chat_page_source.html")
    print("  Findings: results/prod_chat_findings.json")

    print("\n" + "=" * 80)
    print("Test Account Created:")
    print(f"  Email: {test_email}")
    print(f"  Password: {test_password}")
    print("  (Save these for future test runs)")
    print("=" * 80 + "\n")

if __name__ == "__main__":
    explore_production_chat()
