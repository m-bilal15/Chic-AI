"""
Selector Inspector - Extracts all selectors from login page
This will help us get the CORRECT selectors before running tests
"""

from playwright.sync_api import sync_playwright
import json

def inspect_login_page():
    print("=" * 80)
    print("INSPECTING LOGIN PAGE FOR SELECTORS")
    print("=" * 80)
    print()

    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()

        # Navigate to login page
        print("Navigating to http://localhost:5173...")
        page.goto("http://localhost:5173")
        page.wait_for_load_state("networkidle")

        print("Page loaded! Inspecting elements...\n")

        selectors = {}

        # Logo
        try:
            logo = page.locator('img').first
            selectors['logo'] = {
                'selector': 'img',
                'alt': logo.get_attribute('alt'),
                'xpath': '//img[@alt="' + str(logo.get_attribute('alt')) + '"]' if logo.get_attribute('alt') else None,
                'found': True
            }
            print(f"[FOUND] Logo: alt='{logo.get_attribute('alt')}'")
        except:
            selectors['logo'] = {'found': False}
            print("[NOT FOUND] Logo")

        # Welcome heading
        try:
            heading = page.locator('h1, h2').first
            heading_text = heading.text_content()
            selectors['welcome_heading'] = {
                'text': heading_text,
                'xpath': f'//h1[text()="{heading_text}"] | //h2[text()="{heading_text}"]',
                'found': True
            }
            print(f"[FOUND] Heading: '{heading_text}'")
        except:
            selectors['welcome_heading'] = {'found': False}
            print("[NOT FOUND] Welcome heading")

        # Subtitle
        try:
            # Look for text containing "CHIC Concierge"
            subtitle = page.get_by_text("CHIC Concierge", exact=False).first
            subtitle_text = subtitle.text_content()
            selectors['subtitle'] = {
                'text': subtitle_text,
                'selector': f'text="{subtitle_text}"',
                'found': True
            }
            print(f"[FOUND] Subtitle: '{subtitle_text}'")
        except:
            selectors['subtitle'] = {'found': False}
            print("[NOT FOUND] Subtitle")

        # Email input
        try:
            email_input = page.locator('input[type="email"]').first
            selectors['email_input'] = {
                'type': 'email',
                'placeholder': email_input.get_attribute('placeholder'),
                'name': email_input.get_attribute('name'),
                'selector': 'input[type="email"]',
                'placeholder_selector': f'input[placeholder="{email_input.get_attribute("placeholder")}"]',
                'found': True
            }
            print(f"[FOUND] Email input: placeholder='{email_input.get_attribute('placeholder')}'")
        except:
            selectors['email_input'] = {'found': False}
            print("[NOT FOUND] Email input")

        # Password input
        try:
            pwd_input = page.locator('input[type="password"]').first
            selectors['password_input'] = {
                'type': 'password',
                'placeholder': pwd_input.get_attribute('placeholder'),
                'name': pwd_input.get_attribute('name'),
                'selector': 'input[type="password"]',
                'placeholder_selector': f'input[placeholder="{pwd_input.get_attribute("placeholder")}"]',
                'found': True
            }
            print(f"[FOUND] Password input: placeholder='{pwd_input.get_attribute('placeholder')}'")
        except:
            selectors['password_input'] = {'found': False}
            print("[NOT FOUND] Password input")

        # Sign In button
        try:
            sign_in_btn = page.get_by_role('button', name='Sign In').first
            btn_text = sign_in_btn.text_content()
            selectors['sign_in_button'] = {
                'text': btn_text,
                'role': 'button',
                'selector': f'button:has-text("{btn_text}")',
                'xpath': f'//button[contains(text(), "{btn_text.strip()}")]',
                'found': True
            }
            print(f"[FOUND] Sign In button: '{btn_text}'")
        except:
            selectors['sign_in_button'] = {'found': False}
            print("[NOT FOUND] Sign In button")

        # Google button
        try:
            google_btn = page.get_by_text('Sign in with Google').first
            btn_text = google_btn.text_content()
            selectors['google_button'] = {
                'text': btn_text,
                'selector': f'text="{btn_text}"',
                'found': True
            }
            print(f"[FOUND] Google button: '{btn_text}'")
        except:
            selectors['google_button'] = {'found': False}
            print("[NOT FOUND] Google button")

        # Sign up link/button
        try:
            signup = page.get_by_text('Sign up here').first
            signup_text = signup.text_content()
            tag_name = signup.evaluate('el => el.tagName')
            selectors['sign_up'] = {
                'text': signup_text,
                'tag': tag_name,
                'selector': f'{tag_name.lower()}:has-text("{signup_text}")',
                'found': True
            }
            print(f"[FOUND] Sign up: tag={tag_name}, text='{signup_text}'")
        except:
            selectors['sign_up'] = {'found': False}
            print("[NOT FOUND] Sign up")

        # Or continue with divider
        try:
            divider = page.get_by_text('Or continue with').first
            divider_text = divider.text_content()
            selectors['divider'] = {
                'text': divider_text,
                'selector': f'text="{divider_text}"',
                'found': True
            }
            print(f"[FOUND] Divider: '{divider_text}'")
        except:
            selectors['divider'] = {'found': False}
            print("[NOT FOUND] Divider")

        # Save selectors to JSON
        with open('found_selectors.json', 'w', encoding='utf-8') as f:
            json.dump(selectors, f, indent=2)

        print("\n" + "=" * 80)
        print("SELECTORS SAVED TO: found_selectors.json")
        print("=" * 80)
        print("\nKeeping browser open for 10 seconds so you can inspect...")

        # Keep browser open for inspection
        page.wait_for_timeout(10000)

        browser.close()

if __name__ == "__main__":
    inspect_login_page()
