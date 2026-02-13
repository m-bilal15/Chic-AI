"""
Authentication Helper for Chat Tests
Handles signup, onboarding with TRACKED selections, and tour completion
Uses page objects for reliability
Created: February 12, 2026
"""

import time
import random
import uuid
from pages.signup_page import SignupPage
from pages.onboarding_page import OnboardingFlow


def complete_signup_and_onboarding_with_tracking(page, test_name_prefix="chat_test"):
    """
    Complete signup and onboarding with specific tracked selections
    Returns dictionary with all selected preferences for AI validation
    """

    base_url = "https://app.digitalstylist.com"

    # Generate highly unique credentials (email AND name)
    unique_id = str(uuid.uuid4())[:8]
    timestamp = int(time.time())
    random_num = random.randint(10000,99999)
    test_email = f"{test_name_prefix}_{timestamp}_{unique_id}_{random_num}@testmail.com"
    test_password = "ChatTest@2026"
    # Generate unique name too!
    name_uuid = str(uuid.uuid4())[:6]
    test_name = f"{test_name_prefix.title()} User {name_uuid}"

    # Track all selections
    user_profile = {
        "email": test_email,
        "password": test_password,
        "name": test_name,
        "onboarding": {
            "body_type": "",
            "highlight_areas": [],
            "minimize_areas": [],
            "favorite_colors": [],
            "style_descriptions": []
        }
    }

    print(f"\n[SETUP] Creating account: {test_email}")

    # Initialize page objects
    signup_page = SignupPage(page)
    onboarding_page = OnboardingFlow(page)

    # ==========================================
    # STEP 1: SIGNUP
    # ==========================================
    print("\n[STEP 1/7] Signup...")

    page.goto(base_url)
    time.sleep(2)

    # Navigate to signup if on login page
    try:
        # Try different signup link selectors
        signup_selectors = [
            'a:has-text("Sign up here")',
            'a:has-text("Sign up")',
            'button:has-text("Sign up")',
            'a[href*="signup"]',
            'a[href*="register"]'
        ]

        signup_clicked = False
        for selector in signup_selectors:
            signup_link = page.locator(selector).first
            if signup_link.count() > 0:
                try:
                    if signup_link.is_visible(timeout=2000):
                        print(f"[INFO] Found signup link: {selector}")
                        signup_link.click()
                        time.sleep(3)
                        signup_clicked = True
                        break
                except:
                    continue

        if not signup_clicked:
            print("[WARNING] Could not find signup link")

    except Exception as e:
        print(f"[WARNING] Signup link click failed: {e}")

    # Fill signup form using page object methods
    signup_page.fill_full_name(test_name)
    signup_page.fill_email(test_email)
    signup_page.fill_password(test_password)
    signup_page.fill_confirm_password(test_password)
    signup_page.click_create_account()

    time.sleep(5)

    # Check for signup errors
    error_messages = page.locator('[class*="error" i], [class*="Error"], [role="alert"]').all()
    for error in error_messages:
        try:
            if error.is_visible():
                error_text = error.inner_text()
                if error_text:
                    print(f"[ERROR] Signup error: {error_text}")
                    # If email already exists, try with a completely new random email
                    if "already" in error_text.lower() or "exist" in error_text.lower() or "taken" in error_text.lower():
                        print("[RETRY] Account already exists, generating completely new credentials...")
                        # Generate completely new random email AND name
                        new_unique_id = str(uuid.uuid4())
                        test_email = f"{test_name_prefix}_{new_unique_id}@testmail.com"
                        new_name_uuid = str(uuid.uuid4())[:8]
                        test_name = f"{test_name_prefix.title()} User {new_name_uuid}"

                        print(f"[RETRY] New email: {test_email}")

                        # Refill form with new credentials
                        signup_page.fill_full_name(test_name)
                        signup_page.fill_email(test_email)
                        signup_page.fill_password(test_password)
                        signup_page.fill_confirm_password(test_password)
                        signup_page.click_create_account()

                        time.sleep(5)
                        user_profile["email"] = test_email
                        user_profile["name"] = test_name
                        break
        except:
            pass

    current_url = page.url
    print(f"[INFO] After signup, current URL: {current_url}")

    # If still on login/signup page, signup failed
    if "login" in current_url.lower() or "signup" in current_url.lower():
        print("[ERROR] Signup failed - still on login/signup page")
        print("[ERROR] Cannot proceed with test")
        raise Exception("Signup failed - account not created")

    print("[OK] Signup successful, account created")

    # ==========================================
    # STEP 2-6: ONBOARDING (5 Questions)
    # ==========================================

    if "questionnaire" in current_url or "onboarding" in current_url:
        print("\n[ONBOARDING] Completing style profile questionnaire...")

        try:
            # Question 1: Body Type
            print("\n[STEP 2/7] Question 1: Body Type...")
            time.sleep(2)

            selected_body_type = "Hourglass"
            onboarding_page.step1.select_body_type(selected_body_type)
            user_profile["onboarding"]["body_type"] = selected_body_type
            print(f"  [SELECTED] {selected_body_type}")

            time.sleep(1)
            onboarding_page.base.click_continue()
            time.sleep(3)

            # Question 2: Highlight Areas
            print("\n[STEP 3/7] Question 2: Areas to Highlight...")
            time.sleep(2)

            selected_highlights = ["Waist", "Shoulders"]
            onboarding_page.step2.select_areas(selected_highlights)
            user_profile["onboarding"]["highlight_areas"] = selected_highlights
            print(f"  [SELECTED] {selected_highlights}")

            time.sleep(1)
            onboarding_page.base.click_continue()
            time.sleep(3)

            # Question 3: Minimize Areas
            print("\n[STEP 4/7] Question 3: Areas to Minimize...")
            time.sleep(2)

            selected_minimize = ["Hips", "Arms"]
            onboarding_page.step3.select_areas(selected_minimize)
            user_profile["onboarding"]["minimize_areas"] = selected_minimize
            print(f"  [SELECTED] {selected_minimize}")

            time.sleep(1)
            onboarding_page.base.click_continue()
            time.sleep(3)

            # Question 4: Favorite Colors
            print("\n[STEP 5/7] Question 4: Favorite Colors...")
            time.sleep(2)

            selected_colors = ["Black", "White", "Red"]
            onboarding_page.step4.select_colors(selected_colors)
            user_profile["onboarding"]["favorite_colors"] = selected_colors
            print(f"  [SELECTED] {selected_colors}")

            time.sleep(1)
            onboarding_page.base.click_continue()
            time.sleep(3)

            # Question 5: Style Descriptions
            print("\n[STEP 6/7] Question 5: Style Preferences...")
            time.sleep(2)

            selected_styles = ["Chic", "Elegant"]
            onboarding_page.step5.select_styles(selected_styles)
            user_profile["onboarding"]["style_descriptions"] = selected_styles
            print(f"  [SELECTED] {selected_styles}")

            time.sleep(1)
            onboarding_page.base.click_complete_setup()
            time.sleep(5)

            print("[OK] Onboarding questionnaire completed")

        except Exception as e:
            print(f"[WARNING] Onboarding may have failed: {e}")
            print("[INFO] Attempting to continue...")

    # ==========================================
    # STEP 7: COMPLETE WELCOME TOUR
    # ==========================================
    print("\n[STEP 7/7] Completing Welcome Tour (7 steps)...")

    # Navigate to chat (tour appears here)
    page.goto(f"{base_url}/chat")
    time.sleep(5)

    # Complete tour by clicking Next through all 7 steps
    for step_num in range(1, 10):  # Try up to 10 times
        try:
            # Try different button texts for different tour steps
            tour_btn = page.locator('button:has-text("Next"), button:has-text("Got it"), button:has-text("Finish"), button:has-text("Get Started")')

            if tour_btn.count() > 0 and tour_btn.first.is_visible(timeout=2000):
                btn_text = tour_btn.first.inner_text() or "Next"
                print(f"  [TOUR {step_num}/7] Clicking '{btn_text}'...")
                tour_btn.first.click()
                time.sleep(2)
            else:
                print(f"  [INFO] Tour step {step_num} - No more buttons found")
                break

        except Exception as e:
            print(f"  [INFO] Tour completed")
            break

    # Give tour time to close
    time.sleep(2)

    print("[OK] Welcome tour completed")

    # Ensure we're on chat page
    time.sleep(2)
    current_url = page.url
    if "chat" not in current_url:
        print(f"[WARNING] Not on chat page ({current_url}), navigating...")
        page.goto(f"{base_url}/chat")
        time.sleep(3)

    # ==========================================
    # HANDLE PAYWALL/SUBSCRIPTION MODAL (if appears)
    # ==========================================
    print("\n[CHECK] Checking for paywall/subscription modal...")

    # Look for subscription modal
    paywall_modal = page.locator('[class*="modal"], [role="dialog"]')
    trial_button = page.locator('button:has-text("Start Trial"), button:has-text("Trial")')

    if paywall_modal.count() > 0 or trial_button.count() > 0:
        print("[FOUND] Subscription modal detected")

        # Check for trial button
        if trial_button.count() > 0 and trial_button.first.is_visible():
            print("[ACTION] Clicking 'Start Trial' to access chat...")
            try:
                trial_button.first.click()
                time.sleep(5)
                print("[OK] Trial started - chat should be accessible")
            except Exception as e:
                print(f"[WARNING] Could not click trial button: {e}")

            # Check for close button as fallback
            close_btn = page.locator('button[aria-label*="close" i], button:has-text("X"), [aria-label*="Close"]')
            if close_btn.count() > 0:
                try:
                    close_btn.first.click()
                    time.sleep(2)
                    print("[INFO] Closed modal")
                except:
                    pass
    else:
        print("[OK] No paywall modal - chat is accessible")

    # Final summary
    print(f"\n[COMPLETE] Setup finished - Chat ready for testing")
    print(f"[PROFILE] User Profile:")
    print(f"  Email: {user_profile['email']}")
    print(f"  Body Type: {user_profile['onboarding']['body_type']}")
    print(f"  Highlight: {user_profile['onboarding']['highlight_areas']}")
    print(f"  Minimize: {user_profile['onboarding']['minimize_areas']}")
    print(f"  Colors: {user_profile['onboarding']['favorite_colors']}")
    print(f"  Styles: {user_profile['onboarding']['style_descriptions']}")

    return user_profile


def quick_auth_without_tracking(page, test_name_prefix="chat_quick"):
    """
    Quick authentication without detailed tracking
    For tests that don't need personalization validation
    """

    base_url = "https://app.digitalstylist.com"

    # Generate unique email AND name
    unique_id = str(uuid.uuid4())[:8]
    timestamp = int(time.time())
    test_email = f"{test_name_prefix}_{timestamp}_{unique_id}@testmail.com"
    name_uuid = str(uuid.uuid4())[:6]
    test_name = f"Quick User {name_uuid}"

    print(f"[SETUP] Quick auth: {test_email}")

    signup_page = SignupPage(page)
    onboarding_page = OnboardingFlow(page)

    # Signup
    page.goto(base_url)
    time.sleep(2)

    try:
        page.locator('a:has-text("Sign up")').first.click()
        time.sleep(2)
    except:
        pass

    signup_page.fill_full_name(test_name)
    signup_page.fill_email(test_email)
    signup_page.fill_password("ChatTest@2026")
    signup_page.fill_confirm_password("ChatTest@2026")
    signup_page.click_create_account()
    time.sleep(5)

    # Quick onboarding (use correct page object structure)
    try:
        onboarding_page.step1.select_body_type("Hourglass")
        onboarding_page.base.click_continue()
        time.sleep(2)

        onboarding_page.step2.select_areas(["Waist"])
        onboarding_page.base.click_continue()
        time.sleep(2)

        onboarding_page.step3.select_areas(["Hips"])
        onboarding_page.base.click_continue()
        time.sleep(2)

        onboarding_page.step4.select_colors(["Black"])
        onboarding_page.base.click_continue()
        time.sleep(2)

        onboarding_page.step5.select_styles(["Chic"])
        onboarding_page.base.click_complete_setup()
        time.sleep(3)
    except Exception as e:
        print(f"[WARNING] Quick onboarding may have issues: {e}")

    # Complete tour
    page.goto(f"{base_url}/chat")
    time.sleep(3)

    for _ in range(7):
        try:
            page.locator('button:has-text("Next")').first.click(timeout=2000)
            time.sleep(1)
        except:
            break

    return {"email": test_email}
