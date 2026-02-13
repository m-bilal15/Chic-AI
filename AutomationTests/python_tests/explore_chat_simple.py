"""
Explore Chat Page (Simple) - Login and Access Chat
Created: February 12, 2026
"""

from playwright.sync_api import sync_playwright
import time
import json

def explore_chat_simple():
    """Login and explore chat page"""

    print("\n" + "=" * 80)
    print("EXPLORING CHAT PAGE - SIMPLE FLOW")
    print("=" * 80)
    print("Flow: Login > Dashboard > Chat")
    print("=" * 80 + "\n")

    # Test credentials - using from .env or default
    test_email = "bilal@test.com"  # From CLAUDE.md
    test_password = "ValidPass@123"  # From CLAUDE.md

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1500)
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()

        findings = {
            "chat_elements": [],
            "selectors": {},
            "features": [],
            "flow": []
        }

        try:
            # STEP 1: Go to localhost
            print("\n[STEP 1] Navigating to localhost...")
            page.goto("http://localhost:5173")
            page.wait_for_load_state("networkidle")
            time.sleep(2)

            current_url = page.url
            print(f"[INFO] Loaded page: {current_url}")

            page.screenshot(path="results/chat_simple_01_initial.png", full_page=True)

            # STEP 2: Check if on login page
            if "login" in current_url.lower() or "sign in" in page.content().lower():
                print("\n[STEP 2] On login page - attempting login...")

                # Fill login form
                print(f"  [ACTION] Entering email: {test_email}")
                page.fill('input[type="email"], input[name="email"]', test_email)
                time.sleep(1)

                print(f"  [ACTION] Entering password")
                page.fill('input[type="password"], input[name="password"]', test_password)
                time.sleep(1)

                page.screenshot(path="results/chat_simple_02_login_filled.png", full_page=True)

                # Click sign in
                print("  [ACTION] Clicking Sign In...")
                page.click('button:has-text("Sign In"), button:has-text("Sign in"), button[type="submit"]')
                time.sleep(5)  # Wait for login

                current_url = page.url
                print(f"  [INFO] After login: {current_url}")

                page.screenshot(path="results/chat_simple_03_after_login.png", full_page=True)
                findings["flow"].append("Login completed")

            # STEP 3: Navigate to chat
            print("\n[STEP 3] Navigating to chat page...")

            # Try different methods to access chat
            chat_accessed = False

            # Method 1: Direct URL
            print("  [TRY] Direct navigation to /chat...")
            page.goto("http://localhost:5173/chat")
            time.sleep(3)

            current_url = page.url
            print(f"  [INFO] Current URL: {current_url}")

            if "chat" in current_url.lower():
                print("  [SUCCESS] Accessed chat page via URL")
                chat_accessed = True
            else:
                # Method 2: Look for chat link
                print("  [TRY] Looking for chat link/button...")
                chat_selectors = [
                    'a[href="/chat"]',
                    'a[href*="chat"]',
                    'button:has-text("Chat")',
                    'nav a:has-text("Chat")'
                ]

                for selector in chat_selectors:
                    if page.locator(selector).count() > 0:
                        print(f"  [FOUND] Chat link: {selector}")
                        page.click(selector)
                        time.sleep(3)
                        chat_accessed = True
                        break

            page.screenshot(path="results/chat_simple_04_chat_page.png", full_page=True)

            if not chat_accessed:
                print("  [WARNING] Could not access chat - analyzing current page instead")

            # STEP 4: ANALYZE PAGE
            print("\n" + "=" * 80)
            print("ANALYZING CURRENT PAGE")
            print("=" * 80)

            current_url = page.url
            title = page.title()

            print(f"\n[INFO] URL: {current_url}")
            print(f"[INFO] Title: {title}")

            # Get all visible text
            print("\n[CONTENT] Visible Page Text:")
            print("-" * 80)
            body_text = page.locator('body').inner_text()
            lines = [line.strip() for line in body_text.split('\n') if line.strip()]
            for i, line in enumerate(lines[:40], 1):
                print(f"  {i}. {line}")
            if len(lines) > 40:
                print(f"  ... and {len(lines) - 40} more lines")

            # Check for chat elements
            print("\n[ANALYSIS] Looking for Chat Elements:")
            print("-" * 80)

            chat_elements = {
                "Chat Input (textarea)": "textarea",
                "Chat Input (text input)": 'input[type="text"]',
                "Chat Input (placeholder)": '[placeholder*="message" i], [placeholder*="type" i]',
                "Send Button (text)": 'button:has-text("Send")',
                "Send Button (submit)": 'button[type="submit"]',
                "Messages Container": '[class*="message"], [class*="chat"], [role="log"]',
                "Message Items": '[class*="message"]',
                "User Avatar/Profile": '[class*="avatar"], [class*="profile"]',
                "Navigation Menu": 'nav, [role="navigation"]',
                "Sidebar": '[class*="sidebar"], aside',
                "Header": 'header, [role="banner"]',
                "Main Content": 'main, [role="main"]',
                "Buttons (all)": 'button',
                "Links (all)": 'a',
                "Inputs (all)": 'input',
                "Images": 'img'
            }

            for name, selector in chat_elements.items():
                count = page.locator(selector).count()
                if count > 0:
                    print(f"  [FOUND] {name}: {count} element(s)")
                    findings["chat_elements"].append(name)
                    findings["selectors"][name] = selector

                    # Get first element details
                    try:
                        first_elem = page.locator(selector).first
                        if first_elem.is_visible():
                            print(f"    - First element is VISIBLE")
                            if name in ["Chat Input (textarea)", "Chat Input (text input)"]:
                                placeholder = first_elem.get_attribute("placeholder")
                                if placeholder:
                                    print(f"    - Placeholder: '{placeholder}'")
                    except:
                        pass
                else:
                    print(f"  [NOT FOUND] {name}")

            # Get detailed element analysis
            print("\n[ANALYSIS] Detailed Element Information:")
            print("-" * 80)

            # Analyze main areas
            print("\n1. Main Container:")
            main = page.locator('main, [role="main"], .main-content').first
            try:
                if main.is_visible():
                    main_text = main.inner_text()[:200]
                    print(f"   Content preview: {main_text}...")
            except:
                print("   No main container found")

            # Analyze inputs
            print("\n2. All Input Fields:")
            inputs = page.locator('input, textarea').all()
            for i, inp in enumerate(inputs[:10], 1):
                try:
                    inp_type = inp.get_attribute("type") or "textarea"
                    inp_name = inp.get_attribute("name") or "unnamed"
                    inp_placeholder = inp.get_attribute("placeholder") or ""
                    print(f"   Input {i}: type={inp_type}, name={inp_name}, placeholder='{inp_placeholder}'")
                except:
                    pass

            # Analyze buttons
            print("\n3. All Buttons:")
            buttons = page.locator('button').all()
            for i, btn in enumerate(buttons[:15], 1):
                try:
                    btn_text = btn.inner_text().strip() or btn.get_attribute("aria-label") or "no text"
                    print(f"   Button {i}: '{btn_text}'")
                except:
                    pass

            # Get page HTML structure
            print("\n4. Page Structure (main elements):")
            structure_selectors = ['header', 'nav', 'main', 'aside', 'footer']
            for sel in structure_selectors:
                count = page.locator(sel).count()
                if count > 0:
                    print(f"   <{sel}>: {count} element(s)")

            # Save page source
            print("\n[SAVE] Saving page source...")
            page_html = page.content()
            with open("results/chat_page_source.html", "w", encoding="utf-8") as f:
                f.write(page_html)
            print("  [OK] Saved to: results/chat_page_source.html")

            # Save findings
            with open("results/chat_findings.json", "w", encoding="utf-8") as f:
                json.dump(findings, f, indent=2)
            print("  [OK] Saved to: results/chat_findings.json")

            # Final screenshots
            page.screenshot(path="results/chat_simple_05_analysis.png", full_page=True)
            print("\n[SCREENSHOT] Full page screenshot saved")

            # Keep browser open
            print("\n" + "=" * 80)
            print("EXPLORATION COMPLETE - Keeping browser open for 20 seconds")
            print("=" * 80)
            print("Manually inspect the page to understand its structure...")
            print("=" * 80)
            time.sleep(20)

        except Exception as e:
            print(f"\n[ERROR] Exploration failed: {e}")
            page.screenshot(path="results/chat_simple_error.png", full_page=True)
            import traceback
            traceback.print_exc()

        finally:
            browser.close()

    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Elements found: {len(findings['chat_elements'])}")
    for elem in findings['chat_elements']:
        print(f"  - {elem}")

    print(f"\nFlow: {' > '.join(findings['flow'])}")

    print("\nFiles created:")
    print("  - results/chat_page_source.html")
    print("  - results/chat_findings.json")
    print("  - results/chat_simple_*.png (screenshots)")
    print("=" * 80 + "\n")

if __name__ == "__main__":
    explore_chat_simple()
