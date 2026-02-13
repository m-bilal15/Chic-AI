"""
Base Page Class
Contains common methods for all page objects
"""

import time
from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        """Navigate to URL"""
        print(f"[STEP] Navigating to {url}")
        self.page.goto(url)
        time.sleep(2)
        print("[DONE] Page loaded")

    def click(self, selector: str):
        """Click an element"""
        self.page.click(selector)
        time.sleep(2)

    def fill(self, selector: str, value: str):
        """Fill input field"""
        self.page.fill(selector, value)
        time.sleep(1)

    def get_text(self, selector: str) -> str:
        """Get text content"""
        return self.page.text_content(selector)

    def is_visible(self, selector: str) -> bool:
        """Check if element is visible"""
        try:
            return self.page.is_visible(selector, timeout=5000)
        except:
            return False

    def wait_for_selector(self, selector: str, timeout: int = 5000):
        """Wait for element to be visible"""
        self.page.wait_for_selector(selector, timeout=timeout)

    def take_screenshot(self, filename: str):
        """Take screenshot"""
        self.page.screenshot(path=filename, full_page=True)

    def get_current_url(self) -> str:
        """Get current URL"""
        return self.page.url

    def wait(self, seconds: int):
        """Wait for specified seconds"""
        time.sleep(seconds)
