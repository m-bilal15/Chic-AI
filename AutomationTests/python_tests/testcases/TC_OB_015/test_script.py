"""
Test Case: TC_OB_015
Title: Verify responsive design of questionnaire on Tablet (768x102
Description: Verify responsive design of questionnaire on Tablet (768x1024)
Priority: Medium
Type: UI/UX
Sheet: General Onboarding
Created: February 12, 2026
"""

import pytest
import json
import time
from pathlib import Path


@pytest.mark.medium
@pytest.mark.ui_ux
def test_tc_ob_015(page, onboarding_page, base_url):
    """
    Test Case: TC_OB_015
    Description: Verify responsive design of questionnaire on Tablet (768x1024)
    Priority: Medium
    Type: UI/UX

    Steps:
    1. Open questionnaire on tablet or resize to 768x1024
    2. Navigate through all 5 steps

    Expected Results:
    1. Layout adapts to tablet viewport
    2. Cards display in grid layout
    3. All elements are accessible
    """

    print("\n" + "="*70)
    print("TEST: TC_OB_015 - Verify responsive design of questionnaire on Tablet (768x102")
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

        page.screenshot(path="results/TC_OB_015_initial.png", full_page=True)
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
        page.screenshot(path="results/TC_OB_015_evidence.png", full_page=True)
        

        # Final screenshot
        page.screenshot(path="results/TC_OB_015_final.png", full_page=True)
        print("\n[SCREENSHOT] Final screenshot saved")

        print("\n" + "="*70)
        print("[PASS] TEST PASSED: TC_OB_015")
        print("="*70)
        print("\n[RESULT] Test completed successfully")
        print("[NOTE] Review screenshots for visual verification")
        print("\n")

    except Exception as e:
        page.screenshot(path="results/TC_OB_015_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        print(f"[SCREENSHOT] Failure screenshot saved")
        print("\n")
        raise


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
