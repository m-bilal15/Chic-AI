"""
Analyze Digital Stylist Chat Page
Captures page structure, elements, and functionality
Created: February 12, 2026
"""

from playwright.sync_api import sync_playwright
import time
import json

def analyze_chat_page():
    """Analyze the chat page structure and elements"""

    url = "https://app.digitalstylist.com/chat"

    print("\n" + "=" * 70)
    print("DIGITAL STYLIST CHAT PAGE ANALYSIS")
    print("=" * 70)
    print(f"URL: {url}")
    print("=" * 70 + "\n")

    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False, slow_mo=2000)
        context = browser.new_context(
            viewport={"width": 1280, "height": 720}
        )
        page = context.new_page()

        try:
            # Navigate to page
            print("[STEP 1] Navigating to chat page...")
            page.goto(url, wait_until="networkidle", timeout=60000)
            time.sleep(3)

            # Take initial screenshot
            page.screenshot(path="results/chat_page_initial.png", full_page=True)
            print("[SCREENSHOT] Initial page captured: results/chat_page_initial.png")

            # Get page title
            title = page.title()
            print(f"\n[INFO] Page Title: {title}")

            # Get current URL (might redirect)
            current_url = page.url
            print(f"[INFO] Current URL: {current_url}")

            # Check if redirected to login
            if "login" in current_url.lower() or "signin" in current_url.lower():
                print("\n[NOTICE] Page redirected to login/signin")
                print("[INFO] Authentication required to access chat page")

                # Analyze login page instead
                print("\n" + "-" * 70)
                print("ANALYZING LOGIN PAGE INSTEAD")
                print("-" * 70 + "\n")

                analyze_login_page(page)

            else:
                # Analyze chat page
                print("\n" + "-" * 70)
                print("ANALYZING CHAT PAGE")
                print("-" * 70 + "\n")

                analyze_page_elements(page)

            # Take final screenshot
            page.screenshot(path="results/chat_page_analysis.png", full_page=True)
            print("\n[SCREENSHOT] Analysis screenshot captured: results/chat_page_analysis.png")

            # Keep browser open for manual inspection
            print("\n" + "=" * 70)
            print("Browser will stay open for 10 seconds for manual inspection...")
            print("=" * 70)
            time.sleep(10)

        except Exception as e:
            print(f"\n[ERROR] Analysis failed: {e}")
            page.screenshot(path="results/chat_page_error.png", full_page=True)
            print("[SCREENSHOT] Error screenshot captured")

        finally:
            browser.close()

    print("\n" + "=" * 70)
    print("ANALYSIS COMPLETE")
    print("=" * 70)
    print("Screenshots saved in results/ folder")
    print("Review screenshots to understand page structure")
    print("=" * 70 + "\n")


def analyze_login_page(page):
    """Analyze login page structure"""

    print("[CHECK] Looking for common login elements...")

    # Common login selectors
    elements = {
        "Email input": 'input[type="email"], input[name="email"], input[placeholder*="email" i]',
        "Password input": 'input[type="password"], input[name="password"]',
        "Submit button": 'button[type="submit"], button:has-text("Sign"), button:has-text("Login")',
        "Sign up link": 'a:has-text("Sign up"), a:has-text("Register"), a:has-text("Create")',
        "Google login": 'button:has-text("Google"), a:has-text("Google")',
        "Forgot password": 'a:has-text("Forgot"), a:has-text("Reset")',
        "Logo": 'img[alt*="logo" i], img[alt*="chic" i]',
        "Form": 'form'
    }

    found_elements = []
    for element_name, selector in elements.items():
        try:
            if page.locator(selector).first.is_visible(timeout=2000):
                found_elements.append(element_name)
                print(f"  [FOUND] {element_name}")
        except:
            print(f"  [NOT FOUND] {element_name}")

    print(f"\n[SUMMARY] Found {len(found_elements)} login elements")

    # Get all visible text
    print("\n[INFO] Visible text on page:")
    try:
        body_text = page.locator('body').inner_text()
        lines = [line.strip() for line in body_text.split('\n') if line.strip()]
        for line in lines[:20]:  # First 20 lines
            print(f"  {line}")
        if len(lines) > 20:
            print(f"  ... and {len(lines) - 20} more lines")
    except:
        print("  [ERROR] Could not extract text")

    return found_elements


def analyze_page_elements(page):
    """Analyze main page elements"""

    print("[CHECK] Analyzing page structure...")

    # Common chat page elements
    elements = {
        "Chat input": 'input[type="text"], textarea',
        "Send button": 'button:has-text("Send"), button[type="submit"]',
        "Message container": '[class*="message"], [class*="chat"]',
        "Navigation menu": 'nav, [role="navigation"]',
        "User profile": '[class*="profile"], [class*="user"], [class*="avatar"]',
        "Settings": 'button:has-text("Settings"), a:has-text("Settings")',
        "Logout": 'button:has-text("Logout"), a:has-text("Logout"), button:has-text("Sign out")',
        "Chat history": '[class*="history"], [class*="conversation"]',
        "AI assistant": '[class*="bot"], [class*="assistant"], [class*="ai"]'
    }

    found_elements = []
    for element_name, selector in elements.items():
        try:
            if page.locator(selector).first.is_visible(timeout=2000):
                found_elements.append(element_name)
                count = page.locator(selector).count()
                print(f"  [FOUND] {element_name} ({count} instance(s))")
        except:
            print(f"  [NOT FOUND] {element_name}")

    print(f"\n[SUMMARY] Found {len(found_elements)} chat page elements")

    # Get page structure
    print("\n[INFO] Page structure (headings):")
    try:
        headings = page.locator('h1, h2, h3').all()
        for i, heading in enumerate(headings[:10], 1):
            text = heading.inner_text().strip()
            tag = heading.evaluate('el => el.tagName')
            print(f"  {i}. <{tag}> {text}")
    except:
        print("  [ERROR] Could not extract headings")

    return found_elements


if __name__ == "__main__":
    analyze_chat_page()
