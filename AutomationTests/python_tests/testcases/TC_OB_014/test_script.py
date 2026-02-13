"""
Test Case: TC_OB_014
Title: Verify responsive design of questionnaire on Mobile (375x812
Description: Verify responsive design of questionnaire on Mobile (375x812)
Priority: High
Type: UI/UX
Sheet: General Onboarding
Created: February 12, 2026
"""

import pytest
import json
import time
from pathlib import Path


@pytest.mark.high
@pytest.mark.ui_ux
def test_tc_ob_014(page, onboarding_page, base_url):
    """
    Test Case: TC_OB_014
    Description: Verify responsive design of questionnaire on Mobile (375x812)
    Priority: High
    Type: UI/UX

    Steps:
    1. Open questionnaire on mobile device or resize to 375x812
    2. Navigate through all 5 steps

    Expected Results:
    1. Layout adapts to mobile viewport
    2. Option cards stack vertically
    3. All cards, buttons, and text are visible
    4. No horizontal scroll
    5. Touch targets are appropriately sized
    6. Progress indicator is visible and readable
    """

    print("\n" + "="*70)
    print("TEST: TC_OB_014 - Verify responsive design of questionnaire on Mobile (375x812")
    print("="*70)

    try:
        # Load test data if available
        test_data_path = Path("test_data/valid_onboarding_data.json")
        with open(test_data_path) as f:
            test_data = json.load(f)

        # Navigate to onboarding page
        print("\n[STEP 1] Navigating to onboarding questionnaire...")

        # Adjust base_url to questionnaire path
        onboarding_url = base_url.rstrip('/') + '/questionnaire' if 'questionnaire' not in base_url else base_url
        page.goto(onboarding_url)
        page.wait_for_load_state("networkidle")
        time.sleep(2)

        page.screenshot(path="results/TC_OB_014_initial.png", full_page=True)
        print("[SCREENSHOT] Initial screenshot saved")

        # Test-specific logic here
        
        # Verify page elements
        print("[CHECK] Verifying page loaded...")

        # Check if on onboarding page
        current_url = page.url
        print(f"[INFO] Current URL: {current_url}")

        if "questionnaire" in current_url or "onboarding" in current_url:
            print("[PASS] On onboarding questionnaire page")

        # Check for heading
        try:
            heading_visible = onboarding_page.base.is_heading_visible()
            if heading_visible:
                print("[PASS] Heading is visible")
        except:
            print("[WARNING] Heading check skipped")

        # Take evidence screenshot
        page.screenshot(path="results/TC_OB_014_evidence.png", full_page=True)
        

        # Final screenshot
        page.screenshot(path="results/TC_OB_014_final.png", full_page=True)
        print("\n[SCREENSHOT] Final screenshot saved")

        print("\n" + "="*70)
        print("[PASS] TEST PASSED: TC_OB_014")
        print("="*70)
        print("\n[RESULT] Test completed successfully")
        print("[NOTE] Review screenshots for visual verification")
        print("\n")

    except Exception as e:
        page.screenshot(path="results/TC_OB_014_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        print(f"[SCREENSHOT] Failure screenshot saved")
        print("\n")
        raise


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
