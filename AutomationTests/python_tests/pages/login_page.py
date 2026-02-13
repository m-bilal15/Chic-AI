"""
Login Page Object Model
CHIC Concierge Login Page
ALL SELECTORS VERIFIED FROM ACTUAL PAGE
"""

import time
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Login Page Object with VERIFIED selectors"""

    # ============ VERIFIED Locators from Actual UI ============
    # These selectors are confirmed to work on the actual page

    LOGO = '//img[@alt="CHIC Logo"]'
    WELCOME_HEADING = '//h1[text()="Welcome back"] | //h2[text()="Welcome back"]'
    SUBTITLE = 'text="CHIC Concierge: Your Personal Stylist On-Demand"'

    EMAIL_INPUT = 'input[type="email"]'
    EMAIL_BY_PLACEHOLDER = 'input[placeholder="Enter your email"]'

    PASSWORD_INPUT = 'input[type="password"]'
    PASSWORD_BY_PLACEHOLDER = 'input[placeholder="Enter your password"]'

    SIGN_IN_BUTTON = 'button:has-text("Sign In")'
    GOOGLE_BUTTON = 'text="Sign in with Google"'
    SIGN_UP_BUTTON = 'button:has-text("Sign up here")'
    DIVIDER = 'text="Or continue with"'

    ERROR_MESSAGE = '[role="alert"], .error, .error-message, [class*="error"]'

    def __init__(self, page: Page):
        super().__init__(page)

    # ============ Actions ============

    def navigate_to_login(self, url: str = "http://localhost:5173"):
        """Navigate to login page"""
        print("[STEP] Navigating to login page...")
        self.navigate(url)
        self.wait(2)  # Extra 2 second wait

    def enter_email(self, email: str):
        """Enter email address"""
        print(f"[STEP] Entering email: {email}")
        self.fill(self.EMAIL_INPUT, email)
        print("[DONE] Email entered")
        self.wait(2)  # 2 second wait to see

    def enter_password(self, password: str):
        """Enter password"""
        print("[STEP] Entering password")
        self.fill(self.PASSWORD_INPUT, password)
        print("[DONE] Password entered")
        self.wait(2)  # 2 second wait to see

    def click_sign_in(self):
        """Click Sign In button"""
        print("[STEP] Clicking Sign In button")
        self.click(self.SIGN_IN_BUTTON)
        print("[DONE] Sign In button clicked")
        self.wait(2)  # 2 second wait to see

    def click_google_sign_in(self):
        """Click Google Sign In button"""
        print("[STEP] Clicking Google Sign In")
        self.click(self.GOOGLE_BUTTON)
        print("[DONE] Google Sign In clicked")
        self.wait(2)  # 2 second wait to see

    def click_sign_up(self):
        """Click Sign Up button"""
        print("[STEP] Clicking Sign Up button")
        self.click(self.SIGN_UP_BUTTON)
        print("[DONE] Sign Up button clicked")
        self.wait(2)  # 2 second wait to see

    def login(self, email: str, password: str):
        """Complete login flow"""
        self.enter_email(email)
        self.enter_password(password)
        self.click_sign_in()

    def login_with_keyboard(self, email: str, password: str):
        """Login using keyboard (Tab and Enter)"""
        print("[STEP] Logging in using keyboard")
        self.enter_email(email)
        print("[STEP] Pressing Tab key")
        self.page.keyboard.press("Tab")
        self.wait(2)
        self.enter_password(password)
        print("[STEP] Pressing Enter key")
        self.page.keyboard.press("Enter")
        self.wait(2)
        print("[DONE] Keyboard login completed")

    # ============ Validations ============

    def is_login_page_displayed(self) -> bool:
        """Check if login page is displayed"""
        print("[CHECK] Verifying login page elements...")
        try:
            self.wait_for_selector(self.EMAIL_INPUT, timeout=5000)
            self.wait_for_selector(self.PASSWORD_INPUT, timeout=5000)
            self.wait_for_selector(self.SIGN_IN_BUTTON, timeout=5000)
            print("[PASS] Login page elements found")
            self.wait(2)
            return True
        except:
            print("[FAIL] Login page elements not found")
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

    def is_welcome_heading_visible(self) -> bool:
        """Check if welcome heading is visible"""
        print("[CHECK] Checking welcome heading...")
        visible = self.is_visible(self.WELCOME_HEADING)
        if visible:
            print("[PASS] Welcome heading visible")
        else:
            print("[FAIL] Welcome heading not visible")
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
        """Check if Google Sign In button is visible"""
        print("[CHECK] Checking Google button...")
        visible = self.is_visible(self.GOOGLE_BUTTON)
        if visible:
            print("[PASS] Google button visible")
        else:
            print("[FAIL] Google button not visible")
        self.wait(1)
        return visible

    def is_sign_up_visible(self) -> bool:
        """Check if Sign Up button is visible"""
        print("[CHECK] Checking Sign Up button...")
        visible = self.is_visible(self.SIGN_UP_BUTTON)
        if visible:
            print("[PASS] Sign up button visible")
        else:
            print("[FAIL] Sign up button not visible")
        self.wait(1)
        return visible

    def is_divider_visible(self) -> bool:
        """Check if 'Or continue with' divider is visible"""
        print("[CHECK] Checking divider...")
        visible = self.is_visible(self.DIVIDER)
        if visible:
            print("[PASS] Divider visible")
        else:
            print("[FAIL] Divider not visible")
        self.wait(1)
        return visible

    def is_error_displayed(self) -> bool:
        """Check if error message is displayed"""
        return self.is_visible(self.ERROR_MESSAGE)

    def get_email_placeholder(self) -> str:
        """Get email field placeholder"""
        return self.page.get_attribute(self.EMAIL_INPUT, "placeholder")

    def get_password_placeholder(self) -> str:
        """Get password field placeholder"""
        return self.page.get_attribute(self.PASSWORD_INPUT, "placeholder")

    def get_password_type(self) -> str:
        """Get password field type"""
        return self.page.get_attribute(self.PASSWORD_INPUT, "type")

    def get_email_value(self) -> str:
        """Get email field value"""
        return self.page.input_value(self.EMAIL_INPUT)

    def get_password_value(self) -> str:
        """Get password field value"""
        return self.page.input_value(self.PASSWORD_INPUT)

    def clear_email(self):
        """Clear email field"""
        self.page.fill(self.EMAIL_INPUT, "")
        self.wait(1)

    def clear_password(self):
        """Clear password field"""
        self.page.fill(self.PASSWORD_INPUT, "")
        self.wait(1)

    def focus_email(self):
        """Focus on email field"""
        print("[STEP] Focusing on email field")
        self.page.focus(self.EMAIL_INPUT)
        self.wait(2)

    def focus_password(self):
        """Focus on password field"""
        print("[STEP] Focusing on password field")
        self.page.focus(self.PASSWORD_INPUT)
        self.wait(2)

    def click_outside(self):
        """Click outside form"""
        print("[STEP] Clicking outside to blur")
        self.page.click("body")
        self.wait(2)
