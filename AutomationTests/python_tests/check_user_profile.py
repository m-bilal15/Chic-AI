"""
Check User Profile - Verify Onboarding Data
Login as tim@gmail.com and check if questionnaire was completed
Created: February 13, 2026
"""

from playwright.sync_api import sync_playwright
import time

def check_user_profile():
    """Login and check user's style profile data"""

    print("\n" + "=" * 80)
    print("CHECKING USER PROFILE - tim@gmail.com")
    print("=" * 80)
    print("Purpose: Verify if onboarding questionnaire was completed")
    print("=" * 80 + "\n")

    email = "tim@gmail.com"
    password = "Qwerty@123"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        try:
            # Login
            print("[STEP 1] Logging in...")
            print("-" * 80)
            page.goto("https://app.digitalstylist.com/login")
            time.sleep(2)

            page.fill('input[type="email"]', email)
            page.fill('input[type="password"]', password)
            page.click('button[type="submit"]')
            time.sleep(5)

            print(f"[OK] Logged in as {email}\n")

            # Go to chat
            page.goto("https://app.digitalstylist.com/chat")
            time.sleep(5)

            # Handle modals
            for _ in range(10):
                btn = page.locator('button:has-text("Next"), button:has-text("Get Started"), [aria-label*="close"]').first
                if btn.count() > 0:
                    try:
                        btn.click(timeout=2000)
                        time.sleep(2)
                    except:
                        break
                else:
                    break

            page.screenshot(path="results/profile_check_01_chat.png", full_page=True)

            # Check for Basic Profile button
            print("[STEP 2] Checking for profile access...")
            print("-" * 80)

            # Try to access profile
            profile_buttons = [
                'button:has-text("Basic Profile")',
                'button:has-text("Profile")',
                'a:has-text("Profile")',
                'a[href*="profile"]',
                '[aria-label*="profile" i]'
            ]

            profile_found = False
            for selector in profile_buttons:
                if page.locator(selector).count() > 0:
                    print(f"[FOUND] Profile button: {selector}")
                    try:
                        page.locator(selector).first.click()
                        time.sleep(3)
                        profile_found = True
                        break
                    except:
                        continue

            if not profile_found:
                print("[INFO] No direct profile button, trying Settings...")

                # Try Settings
                settings_btn = page.locator('a:has-text("Settings"), button:has-text("Settings")').first
                if settings_btn.count() > 0:
                    print("[FOUND] Settings button")
                    settings_btn.click()
                    time.sleep(3)

            page.screenshot(path="results/profile_check_02_profile_page.png", full_page=True)

            # Check current URL
            current_url = page.url
            print(f"\n[INFO] Current URL: {current_url}")

            # Try to find profile data on page
            print("\n[STEP 3] Looking for profile data...")
            print("-" * 80)

            # Look for onboarding data indicators
            profile_data = {
                "body_type": None,
                "colors": [],
                "styles": [],
                "completed": False
            }

            # Check page content for profile information
            page_text = page.locator('body').text_content().lower()

            # Look for body type mentions
            body_types = ["hourglass", "pear", "apple", "rectangle", "triangle", "athletic"]
            for bt in body_types:
                if bt in page_text:
                    profile_data["body_type"] = bt
                    print(f"[FOUND] Body Type mentioned: {bt}")

            # Look for color mentions
            colors = ["black", "white", "red", "blue", "green", "pink", "purple", "yellow", "beige", "navy"]
            for color in colors:
                if color in page_text and color not in profile_data["colors"]:
                    profile_data["colors"].append(color)

            if profile_data["colors"]:
                print(f"[FOUND] Colors mentioned: {profile_data['colors']}")

            # Look for style mentions
            styles = ["chic", "elegant", "casual", "bohemian", "classic", "trendy", "minimalist"]
            for style in styles:
                if style in page_text and style not in profile_data["styles"]:
                    profile_data["styles"].append(style)

            if profile_data["styles"]:
                print(f"[FOUND] Styles mentioned: {profile_data['styles']}")

            # Check for questionnaire completion indicators
            questionnaire_keywords = ["style profile", "questionnaire", "completed", "preferences set"]
            for keyword in questionnaire_keywords:
                if keyword in page_text:
                    profile_data["completed"] = True
                    print(f"[FOUND] Profile indicator: '{keyword}'")

            # Look for "Complete Profile" or "Set up profile" buttons (indicates incomplete)
            incomplete_indicators = page.locator('button:has-text("Complete Profile"), button:has-text("Set up"), a:has-text("Complete your profile")')
            if incomplete_indicators.count() > 0:
                print(f"\n[WARNING] Found 'Complete Profile' button - profile may be incomplete!")
                profile_data["completed"] = False

            # Try navigating to profile/preferences directly
            print("\n[STEP 4] Attempting to access profile/preferences page...")
            print("-" * 80)

            # Try different profile URLs
            profile_urls = [
                "https://app.digitalstylist.com/profile",
                "https://app.digitalstylist.com/settings",
                "https://app.digitalstylist.com/preferences",
                "https://app.digitalstylist.com/account"
            ]

            for url in profile_urls:
                print(f"\n[TRY] {url}")
                page.goto(url)
                time.sleep(3)

                current_url = page.url
                if current_url != url and "login" in current_url:
                    print(f"  Redirected to login - URL not accessible")
                else:
                    print(f"  Current URL: {current_url}")
                    page.screenshot(path=f"results/profile_check_url_{url.split('/')[-1]}.png", full_page=True)

                    # Check for profile data
                    page_content = page.locator('body').text_content()

                    # Look for questionnaire data
                    if "body type" in page_content.lower():
                        print(f"  [FOUND] 'Body Type' mentioned on page")

                    if any(color in page_content.lower() for color in ["black", "white", "red", "blue"]):
                        print(f"  [FOUND] Colors mentioned on page")

                    if any(style in page_content.lower() for style in ["chic", "elegant", "casual"]):
                        print(f"  [FOUND] Styles mentioned on page")

                    # Look for "complete questionnaire" or similar
                    if "complete" in page_content.lower() and "questionnaire" in page_content.lower():
                        print(f"  [FOUND] Questionnaire completion reference")

            # Final analysis
            print("\n\n" + "=" * 80)
            print("PROFILE DATA ANALYSIS")
            print("=" * 80)
            print(f"Account: {email}")
            print(f"\nProfile Data Found:")
            print(f"  Body Type: {profile_data['body_type'] or 'NOT FOUND'}")
            print(f"  Favorite Colors: {profile_data['colors'] or 'NOT FOUND'}")
            print(f"  Style Preferences: {profile_data['styles'] or 'NOT FOUND'}")
            print(f"  Questionnaire Completed: {profile_data['completed']}")

            print("\n" + "-" * 80)

            if profile_data["body_type"] and len(profile_data["colors"]) > 0:
                print("\n[CONCLUSION] ✅ PROFILE DATA EXISTS")
                print("User HAS completed onboarding questionnaire")
                print("\n=> BUG CONFIRMED: AI should use this data but is NOT!")
            elif not profile_data["completed"]:
                print("\n[CONCLUSION] ⚠️ PROFILE INCOMPLETE")
                print("User may NOT have completed onboarding questionnaire")
                print("\n=> NOT A BUG: AI correctly asks for information when profile is empty")
            else:
                print("\n[CONCLUSION] ❓ UNCLEAR")
                print("Could not definitively determine profile status")
                print("\n=> NEED TO VERIFY: Check account settings or database")

            print("=" * 80)

            # Keep browser open for manual inspection
            print("\n[INSPECT] Browser will stay open for 30 seconds...")
            print("Please manually check the profile/settings pages")
            print("=" * 80 + "\n")
            time.sleep(30)

        except Exception as e:
            print(f"\n[ERROR] {e}")
            page.screenshot(path="results/profile_check_error.png", full_page=True)
            import traceback
            traceback.print_exc()

        finally:
            browser.close()

    print("\n" + "=" * 80)
    print("PROFILE CHECK COMPLETE")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    check_user_profile()
