"""
Sign Up Page Object Model
CHIC Concierge Sign Up / Create Account Page
Created: February 12, 2026

NOTE: Selectors need to be verified against actual page.
This is a template based on common patterns.
"""

import time
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class SignupPage(BasePage):
    """Sign Up Page Object - Template selectors to be verified"""

    # ============ Locators (TO BE VERIFIED) ============
    # These are initial selectors - will need verification against actual UI

    # Page elements
    LOGO = '//img[@alt="CHIC Logo"]'
    HEADING = 'h1:has-text("Create your account"), h2:has-text("Create your account")'
    SUBTITLE = 'text="Join CHIC and discover your perfect style"'

    # Form fields
    FULL_NAME_INPUT = 'input[type="text"][placeholder*="name" i], input[name="fullName"], input[name="name"], input#fullName'
    EMAIL_INPUT = 'input[type="email"], input[placeholder*="email" i], input[name="email"]'
    PASSWORD_INPUT = 'input[type="password"][placeholder*="Password" i]:not([placeholder*="Confirm" i])'
    CONFIRM_PASSWORD_INPUT = 'input[type="password"][placeholder*="Confirm" i], input[name="confirmPassword"]'

    # Password visibility toggles
    PASSWORD_TOGGLE = '(//input[@type="password"][1]/following-sibling::*[contains(@class, "eye") or contains(text(), "👁")])[1]'
    CONFIRM_PASSWORD_TOGGLE = '(//input[@type="password"][2]/following-sibling::*[contains(@class, "eye") or contains(text(), "👁")])[1]'

    # Buttons
    CREATE_ACCOUNT_BUTTON = 'button:has-text("Create Account"), button[type="submit"]'
    GOOGLE_SIGNUP_BUTTON = 'button:has-text("Sign up with Google"), text="Sign up with Google"'
    SIGN_IN_LINK = 'a:has-text("Sign in here"), a:has-text("sign in")'

    # Error messages
    ERROR_MESSAGE = '[role="alert"], .error, .error-message, [class*="error"]'
    FULL_NAME_ERROR = '[class*="error"]:near(input[name="fullName"]), [id*="fullName"][class*="error"]'
    EMAIL_ERROR = '[class*="error"]:near(input[type="email"]), [id*="email"][class*="error"]'
    PASSWORD_ERROR = '[class*="error"]:near(input[type="password"])'

    # Loading state
    LOADING_SPINNER = '.loading, .spinner, [class*="loading"]'

    def __init__(self, page: Page):
        super().__init__(page)

    # ============ Navigation ============

    def navigate_to_signup(self, url: str = "http://localhost:5173"):
        """Navigate to signup page"""
        print("[STEP] Navigating to signup page...")
        self.navigate(url)
        self.wait(2)
        print("[DONE] Signup page loaded")

    def navigate_from_login(self, login_page_url: str = "http://localhost:5173"):
        """Navigate to signup from login page by clicking 'Sign up here' link"""
        print("[STEP] Navigating to login page first...")
        self.navigate(login_page_url)
        self.wait(2)

        # Click sign up link (will be on login page)
        try:
            sign_up_link = 'a:has-text("Sign up here"), button:has-text("Sign up here")'
            print("[STEP] Clicking 'Sign up here' link...")
            self.click(sign_up_link)
            self.wait(2)
            print("[DONE] Navigated to signup page")
        except:
            print("[WARNING] Could not find 'Sign up here' link - already on signup page?")

    # ============ Form Filling Actions ============

    def fill_full_name(self, name: str):
        """Enter full name"""
        print(f"[STEP] Entering full name: {name}")
        self.fill(self.FULL_NAME_INPUT, name)
        print("[DONE] Full name entered")
        self.wait(1)

    def fill_email(self, email: str):
        """Enter email address"""
        print(f"[STEP] Entering email: {email}")
        self.fill(self.EMAIL_INPUT, email)
        print("[DONE] Email entered")
        self.wait(1)

    def fill_password(self, password: str):
        """Enter password"""
        print(f"[STEP] Entering password")
        self.fill(self.PASSWORD_INPUT, password)
        print("[DONE] Password entered")
        self.wait(1)

    def fill_confirm_password(self, password: str):
        """Enter confirm password"""
        print(f"[STEP] Entering confirm password")
        self.fill(self.CONFIRM_PASSWORD_INPUT, password)
        print("[DONE] Confirm password entered")
        self.wait(1)

    def fill_all_fields(self, name: str, email: str, password: str, confirm_password: str = None):
        """Fill all signup form fields"""
        print("[STEP] Filling all signup form fields...")
        self.fill_full_name(name)
        self.fill_email(email)
        self.fill_password(password)
        self.fill_confirm_password(confirm_password or password)
        print("[DONE] All fields filled")

    def clear_full_name(self):
        """Clear full name field"""
        print("[STEP] Clearing full name field")
        self.page.fill(self.FULL_NAME_INPUT, "")
        self.wait(1)

    def clear_email(self):
        """Clear email field"""
        print("[STEP] Clearing email field")
        self.page.fill(self.EMAIL_INPUT, "")
        self.wait(1)

    def clear_password(self):
        """Clear password field"""
        print("[STEP] Clearing password field")
        self.page.fill(self.PASSWORD_INPUT, "")
        self.wait(1)

    def clear_confirm_password(self):
        """Clear confirm password field"""
        print("[STEP] Clearing confirm password field")
        self.page.fill(self.CONFIRM_PASSWORD_INPUT, "")
        self.wait(1)

    def clear_all_fields(self):
        """Clear all form fields"""
        print("[STEP] Clearing all fields...")
        self.clear_full_name()
        self.clear_email()
        self.clear_password()
        self.clear_confirm_password()
        print("[DONE] All fields cleared")

    # ============ Button Click Actions ============

    def click_create_account(self):
        """Click Create Account button"""
        print("[STEP] Clicking Create Account button")
        self.click(self.CREATE_ACCOUNT_BUTTON)
        print("[DONE] Create Account button clicked")
        self.wait(2)

    def click_google_signup(self):
        """Click Sign up with Google button"""
        print("[STEP] Clicking Google Sign Up button")
        self.click(self.GOOGLE_SIGNUP_BUTTON)
        print("[DONE] Google Sign Up button clicked")
        self.wait(2)

    def click_sign_in_link(self):
        """Click 'Sign in here' link to navigate to login"""
        print("[STEP] Clicking 'Sign in here' link")
        self.click(self.SIGN_IN_LINK)
        print("[DONE] Navigating to sign in page")
        self.wait(2)

    # ============ Password Visibility Toggle ============

    def toggle_password_visibility(self):
        """Toggle password field visibility (click eye icon)"""
        print("[STEP] Toggling password visibility")
        try:
            self.click(self.PASSWORD_TOGGLE)
            print("[DONE] Password visibility toggled")
            self.wait(1)
        except:
            print("[WARNING] Password toggle not found or not clickable")

    def toggle_confirm_password_visibility(self):
        """Toggle confirm password field visibility (click eye icon)"""
        print("[STEP] Toggling confirm password visibility")
        try:
            self.click(self.CONFIRM_PASSWORD_TOGGLE)
            print("[DONE] Confirm password visibility toggled")
            self.wait(1)
        except:
            print("[WARNING] Confirm password toggle not found or not clickable")

    # ============ Focus Actions ============

    def focus_full_name(self):
        """Focus on full name field"""
        print("[STEP] Focusing on full name field")
        self.page.focus(self.FULL_NAME_INPUT)
        self.wait(1)

    def focus_email(self):
        """Focus on email field"""
        print("[STEP] Focusing on email field")
        self.page.focus(self.EMAIL_INPUT)
        self.wait(1)

    def focus_password(self):
        """Focus on password field"""
        print("[STEP] Focusing on password field")
        self.page.focus(self.PASSWORD_INPUT)
        self.wait(1)

    def focus_confirm_password(self):
        """Focus on confirm password field"""
        print("[STEP] Focusing on confirm password field")
        self.page.focus(self.CONFIRM_PASSWORD_INPUT)
        self.wait(1)

    def click_outside(self):
        """Click outside form to trigger blur/validation"""
        print("[STEP] Clicking outside form to blur")
        self.page.click("body")
        self.wait(1)

    # ============ Keyboard Navigation ============

    def signup_with_keyboard(self, name: str, email: str, password: str, confirm_password: str = None):
        """Complete signup using keyboard (Tab and Enter)"""
        print("[STEP] Signing up using keyboard navigation...")

        # Fill name, press Tab
        self.fill_full_name(name)
        print("[STEP] Pressing Tab")
        self.page.keyboard.press("Tab")
        self.wait(1)

        # Fill email, press Tab
        self.fill_email(email)
        print("[STEP] Pressing Tab")
        self.page.keyboard.press("Tab")
        self.wait(1)

        # Fill password, press Tab
        self.fill_password(password)
        print("[STEP] Pressing Tab")
        self.page.keyboard.press("Tab")
        self.wait(1)

        # Fill confirm password
        self.fill_confirm_password(confirm_password or password)

        # Press Enter to submit
        print("[STEP] Pressing Enter to submit")
        self.page.keyboard.press("Enter")
        self.wait(2)
        print("[DONE] Keyboard signup completed")

    # ============ Complete Signup Flow ============

    def signup(self, name: str, email: str, password: str, confirm_password: str = None):
        """Complete signup flow with mouse"""
        print("[STEP] Starting signup process...")
        self.fill_all_fields(name, email, password, confirm_password)
        self.click_create_account()
        print("[DONE] Signup process completed")

    # ============ Validations - Page Elements ============

    def is_signup_page_displayed(self) -> bool:
        """Check if signup page is displayed"""
        print("[CHECK] Verifying signup page elements...")
        try:
            self.wait_for_selector(self.FULL_NAME_INPUT, timeout=5000)
            self.wait_for_selector(self.EMAIL_INPUT, timeout=5000)
            self.wait_for_selector(self.PASSWORD_INPUT, timeout=5000)
            self.wait_for_selector(self.CONFIRM_PASSWORD_INPUT, timeout=5000)
            self.wait_for_selector(self.CREATE_ACCOUNT_BUTTON, timeout=5000)
            print("[PASS] Signup page elements found")
            self.wait(1)
            return True
        except Exception as e:
            print(f"[FAIL] Signup page elements not found: {e}")
            return False

    def is_logo_visible(self) -> bool:
        """Check if logo is visible"""
        print("[CHECK] Checking logo...")
        visible = self.is_visible(self.LOGO)
        if visible:
            print("[PASS] Logo is visible")
        else:
            print("[FAIL] Logo not visible")
        self.wait(1)
        return visible

    def is_heading_visible(self) -> bool:
        """Check if 'Create your account' heading is visible"""
        print("[CHECK] Checking heading...")
        visible = self.is_visible(self.HEADING)
        if visible:
            print("[PASS] Heading is visible")
        else:
            print("[FAIL] Heading not visible")
        self.wait(1)
        return visible

    def is_subtitle_visible(self) -> bool:
        """Check if subtitle is visible"""
        print("[CHECK] Checking subtitle...")
        visible = self.is_visible(self.SUBTITLE)
        if visible:
            print("[PASS] Subtitle visible")
        else:
            print("[FAIL] Subtitle not visible")
        self.wait(1)
        return visible

    def is_google_button_visible(self) -> bool:
        """Check if Google Sign Up button is visible"""
        print("[CHECK] Checking Google signup button...")
        visible = self.is_visible(self.GOOGLE_SIGNUP_BUTTON)
        if visible:
            print("[PASS] Google button visible")
        else:
            print("[FAIL] Google button not visible")
        self.wait(1)
        return visible

    def is_sign_in_link_visible(self) -> bool:
        """Check if 'Sign in here' link is visible"""
        print("[CHECK] Checking sign in link...")
        visible = self.is_visible(self.SIGN_IN_LINK)
        if visible:
            print("[PASS] Sign in link visible")
        else:
            print("[FAIL] Sign in link not visible")
        self.wait(1)
        return visible

    def is_create_account_button_visible(self) -> bool:
        """Check if Create Account button is visible"""
        print("[CHECK] Checking Create Account button...")
        visible = self.is_visible(self.CREATE_ACCOUNT_BUTTON)
        if visible:
            print("[PASS] Create Account button visible")
        else:
            print("[FAIL] Create Account button not visible")
        self.wait(1)
        return visible

    # ============ Validations - Field States ============

    def is_error_displayed(self) -> bool:
        """Check if any error message is displayed"""
        return self.is_visible(self.ERROR_MESSAGE)

    def get_error_text(self) -> str:
        """Get error message text"""
        try:
            return self.get_text(self.ERROR_MESSAGE)
        except:
            return ""

    def is_loading(self) -> bool:
        """Check if loading spinner is displayed"""
        return self.is_visible(self.LOADING_SPINNER)

    def get_password_type(self) -> str:
        """Get password field type (password or text)"""
        return self.page.get_attribute(self.PASSWORD_INPUT, "type")

    def get_confirm_password_type(self) -> str:
        """Get confirm password field type (password or text)"""
        return self.page.get_attribute(self.CONFIRM_PASSWORD_INPUT, "type")

    def is_password_masked(self) -> bool:
        """Check if password is masked (type='password')"""
        return self.get_password_type() == "password"

    def is_confirm_password_masked(self) -> bool:
        """Check if confirm password is masked (type='password')"""
        return self.get_confirm_password_type() == "password"

    # ============ Get Field Values ============

    def get_full_name_value(self) -> str:
        """Get full name field value"""
        return self.page.input_value(self.FULL_NAME_INPUT)

    def get_email_value(self) -> str:
        """Get email field value"""
        return self.page.input_value(self.EMAIL_INPUT)

    def get_password_value(self) -> str:
        """Get password field value"""
        return self.page.input_value(self.PASSWORD_INPUT)

    def get_confirm_password_value(self) -> str:
        """Get confirm password field value"""
        return self.page.input_value(self.CONFIRM_PASSWORD_INPUT)

    # ============ Get Field Attributes ============

    def get_full_name_placeholder(self) -> str:
        """Get full name field placeholder"""
        return self.page.get_attribute(self.FULL_NAME_INPUT, "placeholder")

    def get_email_placeholder(self) -> str:
        """Get email field placeholder"""
        return self.page.get_attribute(self.EMAIL_INPUT, "placeholder")

    def get_password_placeholder(self) -> str:
        """Get password field placeholder"""
        return self.page.get_attribute(self.PASSWORD_INPUT, "placeholder")

    def get_confirm_password_placeholder(self) -> str:
        """Get confirm password field placeholder"""
        return self.page.get_attribute(self.CONFIRM_PASSWORD_INPUT, "placeholder")

    # ============ Validation Helpers ============

    def wait_for_error_message(self, timeout: int = 5000) -> bool:
        """Wait for error message to appear"""
        try:
            self.wait_for_selector(self.ERROR_MESSAGE, timeout=timeout)
            return True
        except:
            return False

    def wait_for_page_load(self, timeout: int = 10000):
        """Wait for signup page to fully load"""
        print("[STEP] Waiting for page to load...")
        self.page.wait_for_load_state("networkidle", timeout=timeout)
        self.wait(2)
        print("[DONE] Page loaded")
