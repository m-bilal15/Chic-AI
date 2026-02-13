"""
Onboarding Questionnaire Page Object Model
CHIC Concierge - 5-Step Style Profile Questionnaire
Created: February 12, 2026

Multi-step onboarding flow with data persistence
"""

import time
from playwright.sync_api import Page
from pages.base_page import BasePage


class OnboardingBasePage(BasePage):
    """Base class for all onboarding steps - Common elements"""

    # ============ Common Locators (Present on all steps) ============

    # Header
    HEADING = 'h1:has-text("Let\'s set up your Style Profile"), h2:has-text("Style Profile")'
    QUESTION_SUBTITLE = 'text=/Question \\d+ of 5/'  # Matches "Question 1 of 5", etc.

    # Progress Indicator
    PROGRESS_BAR = '.progress, [class*="progress"], [class*="stepper"]'
    STEP_1_INDICATOR = 'text="1", [class*="step-1"]'
    STEP_2_INDICATOR = 'text="2", [class*="step-2"]'
    STEP_3_INDICATOR = 'text="3", [class*="step-3"]'
    STEP_4_INDICATOR = 'text="4", [class*="step-4"]'
    STEP_5_INDICATOR = 'text="5", [class*="step-5"]'

    # Navigation Buttons
    CONTINUE_BUTTON = 'button:has-text("Continue"), button:has-text("Next")'
    BACK_BUTTON = 'button:has-text("Back"), button:has-text("< Back")'
    SKIP_LINK = 'a:has-text("Skip for now"), button:has-text("Skip")'
    COMPLETE_BUTTON = 'button:has-text("Complete Setup"), button:has-text("Finish")'

    def __init__(self, page: Page):
        super().__init__(page)

    def navigate_to_onboarding(self, url: str = "http://localhost:5173/questionnaire"):
        """Navigate to onboarding page"""
        print("[STEP] Navigating to onboarding questionnaire...")
        self.navigate(url)
        self.wait(2)

    # ============ Navigation Actions ============

    def click_continue(self):
        """Click Continue button to go to next step"""
        print("[STEP] Clicking Continue button")
        self.click(self.CONTINUE_BUTTON)
        self.wait(2)

    def click_back(self):
        """Click Back button to go to previous step"""
        print("[STEP] Clicking Back button")
        self.click(self.BACK_BUTTON)
        self.wait(2)

    def click_skip(self):
        """Click Skip for now link"""
        print("[STEP] Clicking Skip for now")
        self.click(self.SKIP_LINK)
        self.wait(2)

    def click_complete_setup(self):
        """Click Complete Setup button on final step"""
        print("[STEP] Clicking Complete Setup")
        self.click(self.COMPLETE_BUTTON)
        self.wait(2)

    # ============ Validation Methods ============

    def is_heading_visible(self) -> bool:
        """Check if main heading is visible"""
        return self.is_visible(self.HEADING)

    def is_progress_bar_visible(self) -> bool:
        """Check if progress bar is visible"""
        return self.is_visible(self.PROGRESS_BAR)

    def is_skip_link_visible(self) -> bool:
        """Check if Skip for now link is visible"""
        return self.is_visible(self.SKIP_LINK)

    def is_continue_button_visible(self) -> bool:
        """Check if Continue button is visible"""
        return self.is_visible(self.CONTINUE_BUTTON)

    def is_back_button_visible(self) -> bool:
        """Check if Back button is visible"""
        return self.is_visible(self.BACK_BUTTON)

    def get_current_step_number(self) -> int:
        """Get current step number from subtitle"""
        try:
            subtitle = self.get_text(self.QUESTION_SUBTITLE)
            # Extract number from "Question X of 5"
            import re
            match = re.search(r'Question (\d+) of 5', subtitle)
            if match:
                return int(match.group(1))
        except:
            pass
        return 0


class Step1BodyTypePage(OnboardingBasePage):
    """Step 1: Body Type Selection"""

    # Body type options
    HOURGLASS_OPTION = 'button:has-text("Hourglass"), [value="hourglass"]'
    PEAR_OPTION = 'button:has-text("Pear"), [value="pear"]'
    APPLE_OPTION = 'button:has-text("Apple"), [value="apple"]'
    RECTANGLE_OPTION = 'button:has-text("Rectangle"), [value="rectangle"]'
    INVERTED_TRIANGLE_OPTION = 'button:has-text("Inverted Triangle"), [value="inverted-triangle"]'

    def select_hourglass(self):
        """Select Hourglass body type"""
        print("[STEP] Selecting Hourglass body type")
        self.click(self.HOURGLASS_OPTION)
        self.wait(1)

    def select_pear(self):
        """Select Pear body type"""
        print("[STEP] Selecting Pear body type")
        self.click(self.PEAR_OPTION)
        self.wait(1)

    def select_apple(self):
        """Select Apple body type"""
        print("[STEP] Selecting Apple body type")
        self.click(self.APPLE_OPTION)
        self.wait(1)

    def select_body_type(self, body_type: str):
        """Select body type by name"""
        print(f"[STEP] Selecting body type: {body_type}")
        selector_map = {
            "Hourglass": self.HOURGLASS_OPTION,
            "Pear": self.PEAR_OPTION,
            "Apple": self.APPLE_OPTION,
            "Rectangle": self.RECTANGLE_OPTION,
            "Inverted Triangle": self.INVERTED_TRIANGLE_OPTION
        }
        if body_type in selector_map:
            self.click(selector_map[body_type])
            self.wait(1)


class Step2HighlightAreasPage(OnboardingBasePage):
    """Step 2: Highlight Areas Selection (Multiple selection)"""

    # Highlight area options
    SHOULDERS_OPTION = 'button:has-text("Shoulders"), input[value="shoulders"]'
    WAIST_OPTION = 'button:has-text("Waist"), input[value="waist"]'
    LEGS_OPTION = 'button:has-text("Legs"), input[value="legs"]'
    BUST_OPTION = 'button:has-text("Bust"), input[value="bust"]'
    ARMS_OPTION = 'button:has-text("Arms"), input[value="arms"]'

    def select_areas(self, areas: list):
        """Select multiple highlight areas"""
        print(f"[STEP] Selecting highlight areas: {', '.join(areas)}")
        for area in areas:
            if area.lower() == "shoulders":
                self.click(self.SHOULDERS_OPTION)
            elif area.lower() == "waist":
                self.click(self.WAIST_OPTION)
            elif area.lower() == "legs":
                self.click(self.LEGS_OPTION)
            elif area.lower() == "bust":
                self.click(self.BUST_OPTION)
            elif area.lower() == "arms":
                self.click(self.ARMS_OPTION)
            self.wait(0.5)


class Step3MinimizeAreasPage(OnboardingBasePage):
    """Step 3: Minimize Areas Selection (Multiple selection)"""

    # Minimize area options
    MIDSECTION_OPTION = 'button:has-text("Midsection"), input[value="midsection"]'
    ARMS_OPTION = 'button:has-text("Arms"), input[value="arms"]'
    HIPS_OPTION = 'button:has-text("Hips"), input[value="hips"]'
    THIGHS_OPTION = 'button:has-text("Thighs"), input[value="thighs"]'

    def select_areas(self, areas: list):
        """Select multiple minimize areas"""
        print(f"[STEP] Selecting minimize areas: {', '.join(areas)}")
        for area in areas:
            if area.lower() == "midsection":
                self.click(self.MIDSECTION_OPTION)
            elif area.lower() == "arms":
                self.click(self.ARMS_OPTION)
            elif area.lower() == "hips":
                self.click(self.HIPS_OPTION)
            elif area.lower() == "thighs":
                self.click(self.THIGHS_OPTION)
            self.wait(0.5)


class Step4FavoriteColorsPage(OnboardingBasePage):
    """Step 4: Favorite Colors Selection (Select up to 6)"""

    # Color options
    BLACK = 'button:has-text("Black"), input[value="black"]'
    WHITE = 'button:has-text("White"), input[value="white"]'
    NAVY_BLUE = 'button:has-text("Navy Blue"), input[value="navy"]'
    RED = 'button:has-text("Red"), input[value="red"]'
    BEIGE = 'button:has-text("Beige"), button:has-text("Cream"), input[value="beige"]'
    GOLD = 'button:has-text("Gold"), input[value="gold"]'

    def select_colors(self, colors: list):
        """Select multiple colors (up to 6)"""
        print(f"[STEP] Selecting {len(colors)} colors: {', '.join(colors)}")

        color_map = {
            "Black": self.BLACK,
            "White": self.WHITE,
            "Navy Blue": self.NAVY_BLUE,
            "Red": self.RED,
            "Beige": self.BEIGE,
            "Cream": self.BEIGE,
            "Gold": self.GOLD
        }

        for color in colors:
            if color in color_map:
                try:
                    self.click(color_map[color])
                    self.wait(0.5)
                except:
                    print(f"[WARNING] Could not select {color}")


class Step5StyleDescriptionPage(OnboardingBasePage):
    """Step 5: Style Description Selection (Select up to 3)"""

    # Style options
    CHIC = 'button:has-text("Chic"), input[value="chic"]'
    CLASSIC = 'button:has-text("Classic"), input[value="classic"]'
    MINIMALIST = 'button:has-text("Minimalist"), input[value="minimalist"]'
    BOHEMIAN = 'button:has-text("Bohemian"), input[value="bohemian"]'
    EDGY = 'button:has-text("Edgy"), input[value="edgy"]'
    ROMANTIC = 'button:has-text("Romantic"), input[value="romantic"]'

    def select_styles(self, styles: list):
        """Select multiple styles (up to 3)"""
        print(f"[STEP] Selecting {len(styles)} styles: {', '.join(styles)}")

        style_map = {
            "Chic": self.CHIC,
            "Classic": self.CLASSIC,
            "Minimalist": self.MINIMALIST,
            "Bohemian": self.BOHEMIAN,
            "Edgy": self.EDGY,
            "Romantic": self.ROMANTIC
        }

        for style in styles:
            if style in style_map:
                try:
                    self.click(style_map[style])
                    self.wait(0.5)
                except:
                    print(f"[WARNING] Could not select {style}")


class OnboardingFlow:
    """Complete onboarding flow helper - combines all steps"""

    def __init__(self, page: Page):
        self.page = page
        self.base = OnboardingBasePage(page)
        self.step1 = Step1BodyTypePage(page)
        self.step2 = Step2HighlightAreasPage(page)
        self.step3 = Step3MinimizeAreasPage(page)
        self.step4 = Step4FavoriteColorsPage(page)
        self.step5 = Step5StyleDescriptionPage(page)

    def complete_full_flow(self, body_type: str, highlight: list, minimize: list,
                          colors: list, styles: list):
        """Complete entire onboarding flow"""
        print("\n[FLOW] Starting complete onboarding flow...")

        # Step 1
        print("[FLOW] Step 1 - Body Type")
        self.step1.select_body_type(body_type)
        self.base.click_continue()

        # Step 2
        print("[FLOW] Step 2 - Highlight Areas")
        self.step2.select_areas(highlight)
        self.base.click_continue()

        # Step 3
        print("[FLOW] Step 3 - Minimize Areas")
        self.step3.select_areas(minimize)
        self.base.click_continue()

        # Step 4
        print("[FLOW] Step 4 - Favorite Colors")
        self.step4.select_colors(colors)
        self.base.click_continue()

        # Step 5
        print("[FLOW] Step 5 - Style Description")
        self.step5.select_styles(styles)
        self.base.click_complete_setup()

        print("[FLOW] Complete onboarding flow finished")
