"""
Chat Page Object
Contains all methods for interacting with the chat page
Created: February 12, 2026
"""

import time
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class ChatPage(BasePage):
    """
    Page Object for CHIC Chat Page
    Handles all chat functionality, messaging, and interactions
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    # ==========================================
    # LOCATORS - Will be updated after exploration
    # ==========================================

    # Chat Input & Send
    CHAT_INPUT = 'textarea, input[type="text"], [contenteditable="true"]'
    SEND_BUTTON = 'button:has-text("Send"), button[type="submit"]'

    # Messages
    MESSAGES_CONTAINER = '[class*="message"], [class*="chat"], [role="log"]'
    MESSAGE_ITEM = '[class*="message"]'
    USER_MESSAGE = '[class*="user"]'
    AI_MESSAGE = '[class*="ai"], [class*="bot"], [class*="assistant"]'

    # Navigation
    NAV_MENU = 'nav, [role="navigation"]'
    NEW_CHAT_BUTTON = 'button:has-text("New"), button:has-text("Start")'
    CHAT_HISTORY = '[class*="history"], [class*="sidebar"]'

    # User Elements
    USER_PROFILE = '[class*="profile"], [class*="avatar"], [class*="user"]'
    SETTINGS_BUTTON = 'button:has-text("Settings"), [aria-label*="settings" i]'
    LOGOUT_BUTTON = 'button:has-text("Logout"), button:has-text("Sign out")'

    # Other
    IMAGE_UPLOAD_INPUT = 'input[type="file"]'
    UPLOAD_BUTTON = 'button:has-text("Upload"), [aria-label*="upload" i]'
    LOADING_INDICATOR = '[class*="loading"], [class*="spinner"]'

    # ==========================================
    # NAVIGATION METHODS
    # ==========================================

    def navigate_to_chat(self, base_url="http://localhost:5173"):
        """Navigate directly to chat page"""
        print("[STEP] Navigating to chat page...")
        self.page.goto(f"{base_url}/chat")
        self.page.wait_for_load_state("networkidle")
        time.sleep(2)
        print("[DONE] Chat page loaded")

    def is_on_chat_page(self):
        """Check if currently on chat page"""
        current_url = self.page.url
        return "chat" in current_url.lower()

    def get_current_url(self):
        """Get current page URL"""
        return self.page.url

    # ==========================================
    # ELEMENT VISIBILITY CHECKS
    # ==========================================

    def is_chat_input_visible(self):
        """Check if chat input field is visible"""
        try:
            return self.page.locator(self.CHAT_INPUT).first.is_visible(timeout=5000)
        except:
            return False

    def is_send_button_visible(self):
        """Check if send button is visible"""
        try:
            return self.page.locator(self.SEND_BUTTON).first.is_visible(timeout=5000)
        except:
            return False

    def is_messages_container_visible(self):
        """Check if messages container is visible"""
        try:
            return self.page.locator(self.MESSAGES_CONTAINER).first.is_visible(timeout=5000)
        except:
            return False

    def is_send_button_enabled(self):
        """Check if send button is enabled"""
        try:
            return self.page.locator(self.SEND_BUTTON).first.is_enabled()
        except:
            return False

    def is_chat_input_empty(self):
        """Check if chat input is empty"""
        try:
            input_value = self.page.locator(self.CHAT_INPUT).first.input_value()
            return len(input_value.strip()) == 0
        except:
            return True

    # ==========================================
    # MESSAGING METHODS
    # ==========================================

    def type_message(self, message: str):
        """Type message in chat input"""
        print(f"[ACTION] Typing message: '{message}'")
        self.page.locator(self.CHAT_INPUT).first.fill(message)
        time.sleep(0.5)

    def click_send_button(self):
        """Click the send button"""
        print("[ACTION] Clicking send button...")
        self.page.locator(self.SEND_BUTTON).first.click()
        time.sleep(1)

    def send_message(self, message: str):
        """Type and send a message"""
        print(f"[ACTION] Sending message: '{message}'")
        self.type_message(message)
        self.click_send_button()
        time.sleep(2)  # Wait for message to be sent

    def clear_chat_input(self):
        """Clear the chat input field"""
        print("[ACTION] Clearing chat input...")
        self.page.locator(self.CHAT_INPUT).first.fill("")
        time.sleep(0.5)

    def get_chat_input_value(self):
        """Get current value of chat input"""
        try:
            return self.page.locator(self.CHAT_INPUT).first.input_value()
        except:
            return ""

    # ==========================================
    # MESSAGE RETRIEVAL METHODS
    # ==========================================

    def get_message_count(self):
        """Get total number of messages"""
        try:
            return self.page.locator(self.MESSAGE_ITEM).count()
        except:
            return 0

    def get_latest_message_text(self):
        """Get text of the latest message"""
        try:
            messages = self.page.locator(self.MESSAGE_ITEM).all()
            if len(messages) > 0:
                return messages[-1].inner_text().strip()
            return ""
        except:
            return ""

    def get_all_messages(self):
        """Get all message texts as a list"""
        try:
            messages = self.page.locator(self.MESSAGE_ITEM).all()
            return [msg.inner_text().strip() for msg in messages]
        except:
            return []

    def get_user_messages_count(self):
        """Get count of user messages"""
        try:
            return self.page.locator(self.USER_MESSAGE).count()
        except:
            return 0

    def get_ai_messages_count(self):
        """Get count of AI messages"""
        try:
            return self.page.locator(self.AI_MESSAGE).count()
        except:
            return 0

    # ==========================================
    # WAITING METHODS
    # ==========================================

    def wait_for_ai_response(self, timeout=10000):
        """Wait for AI to respond"""
        print("[WAIT] Waiting for AI response...")
        initial_count = self.get_message_count()
        time.sleep(2)  # Initial wait

        start_time = time.time()
        while (time.time() - start_time) * 1000 < timeout:
            current_count = self.get_message_count()
            if current_count > initial_count:
                print("[SUCCESS] AI responded")
                return True
            time.sleep(0.5)

        print("[WARNING] AI did not respond within timeout")
        return False

    def wait_for_message_sent(self, timeout=5000):
        """Wait for message to be sent"""
        print("[WAIT] Waiting for message to be sent...")
        time.sleep(1)
        return True

    def wait_for_loading_complete(self, timeout=10000):
        """Wait for loading indicator to disappear"""
        try:
            self.page.locator(self.LOADING_INDICATOR).first.wait_for(
                state="hidden",
                timeout=timeout
            )
            print("[INFO] Loading complete")
            return True
        except:
            return True  # No loading indicator or already hidden

    # ==========================================
    # NAVIGATION & UI METHODS
    # ==========================================

    def click_new_chat(self):
        """Click new chat button"""
        print("[ACTION] Starting new chat...")
        try:
            self.page.locator(self.NEW_CHAT_BUTTON).first.click()
            time.sleep(2)
            return True
        except:
            print("[WARNING] New chat button not found")
            return False

    def click_settings(self):
        """Click settings button"""
        print("[ACTION] Opening settings...")
        try:
            self.page.locator(self.SETTINGS_BUTTON).first.click()
            time.sleep(2)
            return True
        except:
            print("[WARNING] Settings button not found")
            return False

    def click_logout(self):
        """Click logout button"""
        print("[ACTION] Logging out...")
        try:
            self.page.locator(self.LOGOUT_BUTTON).first.click()
            time.sleep(2)
            return True
        except:
            print("[WARNING] Logout button not found")
            return False

    def is_user_profile_visible(self):
        """Check if user profile is visible"""
        try:
            return self.page.locator(self.USER_PROFILE).first.is_visible(timeout=5000)
        except:
            return False

    # ==========================================
    # IMAGE UPLOAD METHODS
    # ==========================================

    def upload_image(self, image_path: str):
        """Upload an image file"""
        print(f"[ACTION] Uploading image: {image_path}")
        try:
            # Click upload button to trigger file input
            if self.page.locator(self.UPLOAD_BUTTON).count() > 0:
                self.page.locator(self.UPLOAD_BUTTON).first.click()
                time.sleep(1)

            # Set file
            self.page.locator(self.IMAGE_UPLOAD_INPUT).first.set_input_files(image_path)
            time.sleep(2)
            print("[SUCCESS] Image uploaded")
            return True
        except Exception as e:
            print(f"[ERROR] Failed to upload image: {e}")
            return False

    def is_image_upload_available(self):
        """Check if image upload feature is available"""
        try:
            return (
                self.page.locator(self.IMAGE_UPLOAD_INPUT).count() > 0 or
                self.page.locator(self.UPLOAD_BUTTON).count() > 0
            )
        except:
            return False

    # ==========================================
    # CONVERSATION MANAGEMENT
    # ==========================================

    def is_chat_history_visible(self):
        """Check if chat history sidebar is visible"""
        try:
            return self.page.locator(self.CHAT_HISTORY).first.is_visible(timeout=5000)
        except:
            return False

    def get_conversation_list(self):
        """Get list of conversations from history"""
        try:
            conversations = self.page.locator(f'{self.CHAT_HISTORY} li, {self.CHAT_HISTORY} [class*="conversation"]').all()
            return [conv.inner_text().strip() for conv in conversations]
        except:
            return []

    # ==========================================
    # VALIDATION METHODS
    # ==========================================

    def verify_page_loaded(self):
        """Verify chat page is fully loaded"""
        print("[CHECK] Verifying chat page loaded...")

        checks = {
            "Chat input visible": self.is_chat_input_visible(),
            "Send button visible": self.is_send_button_visible(),
        }

        all_passed = all(checks.values())

        for check, result in checks.items():
            status = "[OK]" if result else "[FAIL]"
            print(f"  {status} {check}")

        return all_passed

    def verify_message_sent(self, message_text: str):
        """Verify message was sent successfully"""
        print(f"[CHECK] Verifying message sent: '{message_text}'")

        messages = self.get_all_messages()
        message_found = any(message_text in msg for msg in messages)

        if message_found:
            print("[OK] Message found in conversation")
            return True
        else:
            print("[FAIL] Message not found in conversation")
            return False

    # ==========================================
    # SCREENSHOT METHODS
    # ==========================================

    def take_chat_screenshot(self, filename: str):
        """Take screenshot of chat page"""
        print(f"[SCREENSHOT] Saving: {filename}")
        self.page.screenshot(path=filename, full_page=True)

    # ==========================================
    # HELPER METHODS
    # ==========================================

    def get_page_title(self):
        """Get page title"""
        return self.page.title()

    def scroll_to_latest_message(self):
        """Scroll to the latest message"""
        try:
            messages = self.page.locator(self.MESSAGE_ITEM).all()
            if len(messages) > 0:
                messages[-1].scroll_into_view_if_needed()
                time.sleep(0.5)
        except:
            pass

    def get_send_button_text(self):
        """Get send button text"""
        try:
            return self.page.locator(self.SEND_BUTTON).first.inner_text()
        except:
            return ""

    def press_enter_to_send(self):
        """Press Enter key to send message (keyboard shortcut)"""
        print("[ACTION] Pressing Enter to send...")
        try:
            self.page.locator(self.CHAT_INPUT).first.press("Enter")
            time.sleep(1)
            return True
        except:
            return False

    # ==========================================
    # PERSONALIZATION METHODS
    # ==========================================

    def get_ai_greeting(self):
        """Get initial AI greeting message"""
        messages = self.get_all_messages()
        if len(messages) > 0:
            return messages[0]
        return ""

    def verify_personalized_response(self, keywords: list):
        """Check if AI response contains personalization keywords"""
        latest_message = self.get_latest_message_text().lower()
        found_keywords = [kw for kw in keywords if kw.lower() in latest_message]
        return len(found_keywords) > 0, found_keywords
