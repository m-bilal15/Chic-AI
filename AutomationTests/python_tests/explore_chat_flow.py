"""
Explore Complete User Flow to Chat Page
Navigate: Signup > Onboarding > Dashboard > Chat
Understand structure, elements, and functionality
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
    return f"test_chat_{timestamp}_{random_num}@example.com"

def explore_chat_flow():
    """Complete user flow to reach and explore chat page"""

    print("\n" + "=" * 80)
    print("EXPLORING COMPLETE USER FLOW TO CHAT PAGE")
    print("=" * 80)
    print("Flow: Signup > Onboarding > Dashboard > Welcome Tour > Chat")
    print("=" * 80 + "\n")

    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False, slow_mo=1500)
        context = browser.new_context(viewport={"width": 1280, "height": 720})
        page = context.new_page()

        # Store findings
        findings = {
            "flow": [],
            "chat_page": {
                "url": "",
                "elements": [],
                "features": [],
                "interactions": []
            }
        }

        try:
            # PHASE 1: SIGNUP
            print("\n" + "=" * 80)
            print("PHASE 1: SIGNUP")
            print("=" * 80)

            page.goto("http://localhost:5173")
            page.wait_for_load_state("networkidle")
            time.sleep(2)

            # Generate unique email
            test_email = generate_unique_email()
            test_password = "TestChat@123"

            print(f"[INFO] Test Account:")
            print(f"  Email: {test_email}")
            print(f"  Password: {test_password}")

            # Fill signup form
            print("\n[STEP] Filling signup form...")
            page.fill('input[name="fullName"]', "Chat Test User")
            page.fill('input[name="email"]', test_email)
            page.fill('input[name="password"]', test_password)
            page.fill('input[name="confirmPassword"]', test_password)

            page.screenshot(path="results/chat_flow_01_signup.png", full_page=True)
            print("[SCREENSHOT] Signup form filled")

            # Submit signup
            print("[STEP] Submitting signup...")
            page.click('button[type="submit"]')
            time.sleep(3)

            findings["flow"].append("Signup completed")

            # PHASE 2: ONBOARDING
            print("\n" + "=" * 80)
            print("PHASE 2: ONBOARDING QUESTIONNAIRE")
            print("=" * 80)

            # Check if on onboarding page
            current_url = page.url
            print(f"[INFO] Current URL: {current_url}")

            if "onboarding" in current_url or "questionnaire" in current_url:
                print("[INFO] On onboarding page - completing questionnaire...")

                # Step 1: Body Type
                print("\n[STEP 1] Selecting body type...")
                time.sleep(2)
                body_types = page.locator('button, [role="button"]').all()
                if len(body_types) > 0:
                    body_types[0].click()
                    time.sleep(1)
                    page.screenshot(path="results/chat_flow_02_onboarding_step1.png")
                    print("[SCREENSHOT] Body type selected")

                # Click Continue
                continue_btn = page.locator('button:has-text("Continue"), button:has-text("Next")')
                if continue_btn.count() > 0:
                    continue_btn.first.click()
                    time.sleep(2)

                # Step 2: Highlight Areas
                print("\n[STEP 2] Selecting highlight areas...")
                highlight_btns = page.locator('button, [role="button"]').all()
                if len(highlight_btns) >= 2:
                    highlight_btns[0].click()
                    time.sleep(0.5)
                    highlight_btns[1].click()
                    time.sleep(1)
                    page.screenshot(path="results/chat_flow_03_onboarding_step2.png")

                if continue_btn.count() > 0:
                    continue_btn.first.click()
                    time.sleep(2)

                # Step 3: Minimize Areas
                print("\n[STEP 3] Selecting minimize areas...")
                minimize_btns = page.locator('button, [role="button"]').all()
                if len(minimize_btns) >= 2:
                    minimize_btns[0].click()
                    time.sleep(0.5)
                    minimize_btns[1].click()
                    time.sleep(1)
                    page.screenshot(path="results/chat_flow_04_onboarding_step3.png")

                if continue_btn.count() > 0:
                    continue_btn.first.click()
                    time.sleep(2)

                # Step 4: Favorite Colors
                print("\n[STEP 4] Selecting colors...")
                color_btns = page.locator('button, [role="button"]').all()
                if len(color_btns) >= 3:
                    for i in range(min(3, len(color_btns))):
                        color_btns[i].click()
                        time.sleep(0.3)
                    page.screenshot(path="results/chat_flow_05_onboarding_step4.png")

                if continue_btn.count() > 0:
                    continue_btn.first.click()
                    time.sleep(2)

                # Step 5: Style Description
                print("\n[STEP 5] Selecting style...")
                style_btns = page.locator('button, [role="button"]').all()
                if len(style_btns) >= 2:
                    style_btns[0].click()
                    time.sleep(0.5)
                    style_btns[1].click()
                    time.sleep(1)
                    page.screenshot(path="results/chat_flow_06_onboarding_step5.png")

                # Complete onboarding
                complete_btn = page.locator('button:has-text("Complete"), button:has-text("Finish"), button:has-text("Continue")')
                if complete_btn.count() > 0:
                    complete_btn.first.click()
                    time.sleep(3)

                findings["flow"].append("Onboarding completed")
                print("[SUCCESS] Onboarding questionnaire completed")

            # PHASE 3: DASHBOARD / WELCOME TOUR
            print("\n" + "=" * 80)
            print("PHASE 3: DASHBOARD / WELCOME TOUR")
            print("=" * 80)

            current_url = page.url
            print(f"[INFO] Current URL: {current_url}")
            page.screenshot(path="results/chat_flow_07_after_onboarding.png", full_page=True)

            # Check for welcome tour
            time.sleep(2)
            tour_elements = page.locator('[class*="tour"], [class*="welcome"], [class*="tutorial"]').count()

            if tour_elements > 0:
                print("[INFO] Welcome tour detected - skipping...")
                # Try to skip/close tour
                skip_btns = page.locator('button:has-text("Skip"), button:has-text("Close"), button:has-text("Got it")')
                attempts = 0
                while skip_btns.count() > 0 and attempts < 10:
                    skip_btns.first.click()
                    time.sleep(1)
                    attempts += 1
                    skip_btns = page.locator('button:has-text("Skip"), button:has-text("Close"), button:has-text("Got it")')

                findings["flow"].append("Welcome tour skipped")

            page.screenshot(path="results/chat_flow_08_dashboard.png", full_page=True)
            print("[SCREENSHOT] Dashboard captured")

            # PHASE 4: NAVIGATE TO CHAT
            print("\n" + "=" * 80)
            print("PHASE 4: ACCESSING CHAT PAGE")
            print("=" * 80)

            current_url = page.url
            print(f"[INFO] Current URL: {current_url}")

            # Try to find chat link/button
            print("\n[SEARCH] Looking for chat access...")

            # Common chat navigation patterns
            chat_selectors = [
                'a[href*="chat"]',
                'button:has-text("Chat")',
                'a:has-text("Chat")',
                '[data-testid*="chat"]',
                'nav a:has-text("Chat")',
                '[class*="chat"]',
            ]

            chat_found = False
            for selector in chat_selectors:
                try:
                    chat_elem = page.locator(selector).first
                    if chat_elem.is_visible(timeout=1000):
                        print(f"[FOUND] Chat element with selector: {selector}")
                        chat_elem.click()
                        time.sleep(3)
                        chat_found = True
                        break
                except:
                    continue

            # If no chat button found, check if already on chat page
            if not chat_found:
                print("[INFO] No chat button found - checking current page...")
                if "chat" in current_url.lower():
                    print("[INFO] Already on chat page!")
                    chat_found = True
                else:
                    # Try direct navigation
                    print("[TRY] Navigating directly to /chat...")
                    page.goto("http://localhost:5173/chat")
                    time.sleep(3)
                    chat_found = True

            # PHASE 5: ANALYZE CHAT PAGE
            print("\n" + "=" * 80)
            print("PHASE 5: ANALYZING CHAT PAGE")
            print("=" * 80)

            current_url = page.url
            findings["chat_page"]["url"] = current_url
            print(f"[INFO] Chat Page URL: {current_url}")

            # Take full page screenshot
            page.screenshot(path="results/chat_flow_09_chat_page.png", full_page=True)
            print("[SCREENSHOT] Chat page captured")

            # Analyze page structure
            print("\n[ANALYSIS] Chat Page Structure:")
            print("-" * 80)

            # 1. Page Title
            title = page.title()
            print(f"\n1. Page Title: {title}")

            # 2. Main Elements
            print("\n2. Main UI Elements:")

            elements_to_check = {
                "Chat Input": [
                    'textarea',
                    'input[type="text"]',
                    '[placeholder*="message" i]',
                    '[placeholder*="type" i]',
                    '[contenteditable="true"]'
                ],
                "Send Button": [
                    'button:has-text("Send")',
                    'button[type="submit"]',
                    '[aria-label*="send" i]'
                ],
                "Messages Container": [
                    '[class*="message"]',
                    '[class*="chat"]',
                    '[role="log"]',
                    '[class*="conversation"]'
                ],
                "User Profile": [
                    '[class*="profile"]',
                    '[class*="avatar"]',
                    '[class*="user"]'
                ],
                "Navigation": [
                    'nav',
                    '[role="navigation"]'
                ],
                "Settings": [
                    'button:has-text("Settings")',
                    '[aria-label*="settings" i]'
                ],
                "Logout": [
                    'button:has-text("Logout")',
                    'button:has-text("Sign out")',
                    'a:has-text("Logout")'
                ],
                "Chat History": [
                    '[class*="history"]',
                    '[class*="sidebar"]',
                    '[class*="conversations"]'
                ],
                "New Chat Button": [
                    'button:has-text("New")',
                    'button:has-text("Start")',
                    '[aria-label*="new chat" i]'
                ],
                "Image Upload": [
                    'input[type="file"]',
                    'button:has-text("Upload")',
                    '[aria-label*="upload" i]'
                ]
            }

            for element_name, selectors in elements_to_check.items():
                found = False
                found_selector = None
                for selector in selectors:
                    try:
                        if page.locator(selector).count() > 0:
                            count = page.locator(selector).count()
                            found = True
                            found_selector = selector
                            print(f"  [OK] {element_name}: Found ({count} element(s)) - {selector}")
                            findings["chat_page"]["elements"].append({
                                "name": element_name,
                                "selector": selector,
                                "count": count
                            })
                            break
                    except:
                        continue

                if not found:
                    print(f"  [X] {element_name}: Not found")

            # 3. Get all visible text
            print("\n3. Visible Text Content:")
            print("-" * 80)
            try:
                body_text = page.locator('body').inner_text()
                lines = [line.strip() for line in body_text.split('\n') if line.strip()]
                for i, line in enumerate(lines[:30], 1):
                    print(f"  {i}. {line}")
                if len(lines) > 30:
                    print(f"  ... and {len(lines) - 30} more lines")
            except:
                print("  [ERROR] Could not extract text")

            # 4. Check for initial messages
            print("\n4. Initial Messages/Greetings:")
            print("-" * 80)
            message_containers = page.locator('[class*="message"], [class*="chat"]').all()
            if len(message_containers) > 0:
                print(f"  Found {len(message_containers)} message elements")
                for i, msg in enumerate(message_containers[:5], 1):
                    try:
                        text = msg.inner_text().strip()
                        if text:
                            print(f"  Message {i}: {text[:100]}")
                            findings["chat_page"]["features"].append(f"Initial message: {text[:50]}")
                    except:
                        pass
            else:
                print("  No messages found (empty chat)")

            # 5. Test interaction - try sending a message
            print("\n5. Testing Message Send Functionality:")
            print("-" * 80)

            # Find input field
            input_found = False
            input_selector = None
            for selector in ['textarea', 'input[type="text"]', '[contenteditable="true"]']:
                if page.locator(selector).count() > 0:
                    input_selector = selector
                    input_found = True
                    print(f"  [FOUND] Input field: {selector}")
                    break

            if input_found:
                try:
                    # Type test message
                    test_message = "Hello! I need styling advice."
                    print(f"  [TEST] Typing message: '{test_message}'")
                    page.fill(input_selector, test_message)
                    time.sleep(1)

                    page.screenshot(path="results/chat_flow_10_message_typed.png", full_page=True)
                    print("  [SCREENSHOT] Message typed")

                    # Find and click send button
                    send_btn = page.locator('button:has-text("Send"), button[type="submit"]').first
                    if send_btn.is_visible():
                        print("  [ACTION] Clicking send button...")
                        send_btn.click()
                        time.sleep(3)

                        page.screenshot(path="results/chat_flow_11_message_sent.png", full_page=True)
                        print("  [SCREENSHOT] After message sent")

                        findings["chat_page"]["interactions"].append("Successfully sent message")

                        # Check for response
                        print("  [WAIT] Waiting for AI response...")
                        time.sleep(5)

                        page.screenshot(path="results/chat_flow_12_ai_response.png", full_page=True)
                        print("  [SCREENSHOT] AI response captured")

                        # Count messages after sending
                        new_messages = page.locator('[class*="message"], [class*="chat"]').count()
                        print(f"  [INFO] Total messages after send: {new_messages}")
                        findings["chat_page"]["interactions"].append(f"AI responded - total messages: {new_messages}")

                except Exception as e:
                    print(f"  [ERROR] Failed to send message: {e}")
            else:
                print("  [SKIP] No input field found - cannot test messaging")

            # 6. Check page structure (HTML)
            print("\n6. Page HTML Structure:")
            print("-" * 80)

            # Get main containers
            main_containers = page.locator('main, [role="main"], .main, #main').count()
            print(f"  Main containers: {main_containers}")

            sections = page.locator('section, aside, header, footer').count()
            print(f"  Sections/Layout elements: {sections}")

            buttons = page.locator('button').count()
            print(f"  Total buttons: {buttons}")

            links = page.locator('a').count()
            print(f"  Total links: {links}")

            inputs = page.locator('input, textarea').count()
            print(f"  Total inputs: {inputs}")

            # 7. Get page source (first 500 lines)
            print("\n7. Extracting Page Source...")
            page_source = page.content()
            with open("results/chat_page_source.html", "w", encoding="utf-8") as f:
                f.write(page_source)
            print("  [SAVED] Page source saved to: results/chat_page_source.html")

            # Save findings to JSON
            with open("results/chat_page_findings.json", "w", encoding="utf-8") as f:
                json.dump(findings, f, indent=2)
            print("  [SAVED] Findings saved to: results/chat_page_findings.json")

            # Keep browser open for manual inspection
            print("\n" + "=" * 80)
            print("EXPLORATION COMPLETE - Browser will stay open for 15 seconds")
            print("=" * 80)
            print("Manually inspect the chat page for additional details...")
            time.sleep(15)

        except Exception as e:
            print(f"\n[ERROR] Exploration failed: {e}")
            page.screenshot(path="results/chat_flow_error.png", full_page=True)
            import traceback
            traceback.print_exc()

        finally:
            browser.close()

    # Print summary
    print("\n" + "=" * 80)
    print("EXPLORATION SUMMARY")
    print("=" * 80)
    print(f"\nFlow completed: {' > '.join(findings['flow'])}")
    print(f"\nChat page URL: {findings['chat_page']['url']}")
    print(f"\nElements found: {len(findings['chat_page']['elements'])}")
    for elem in findings['chat_page']['elements']:
        print(f"  - {elem['name']}: {elem['selector']}")

    print(f"\nInteractions tested: {len(findings['chat_page']['interactions'])}")
    for interaction in findings['chat_page']['interactions']:
        print(f"  - {interaction}")

    print("\n" + "=" * 80)
    print("SCREENSHOTS CAPTURED:")
    print("=" * 80)
    print("  1. chat_flow_01_signup.png - Signup form")
    print("  2. chat_flow_02-06_onboarding_*.png - Onboarding steps")
    print("  3. chat_flow_07_after_onboarding.png - After onboarding")
    print("  4. chat_flow_08_dashboard.png - Dashboard")
    print("  5. chat_flow_09_chat_page.png - Chat page initial")
    print("  6. chat_flow_10_message_typed.png - Message typed")
    print("  7. chat_flow_11_message_sent.png - After send")
    print("  8. chat_flow_12_ai_response.png - AI response")
    print("\n  HTML Source: results/chat_page_source.html")
    print("  Findings JSON: results/chat_page_findings.json")
    print("=" * 80 + "\n")

if __name__ == "__main__":
    explore_chat_flow()
