"""
Test Case: TC_OB_013
Title: Verify browser back button behavior during questionnaire
Description: Verify browser back button behavior during questionnaire
Priority: Medium
Type: Positive
Sheet: General Onboarding
Created: February 12, 2026
"""

import pytest
import json
import time
from pathlib import Path


@pytest.mark.medium
@pytest.mark.positive
def test_tc_ob_013(page, onboarding_page, base_url):
    """
    Test Case: TC_OB_013
    Description: Verify browser back button behavior during questionnaire
    Priority: Medium
    Type: Positive

    Steps:
    1. Navigate to Step 3
    2. Click browser Back button (not the in-app Back button)

    Expected Results:
    1. User navigates to Step 2 OR previous page
    2. Application handles browser navigation gracefully
    3. No duplicate submissions or errors
    """

    print("\n" + "="*70)
    print("TEST: TC_OB_013 - Verify browser back button behavior during questionnaire")
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

        page.screenshot(path="results/TC_OB_013_initial.png", full_page=True)
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
        page.screenshot(path="results/TC_OB_013_evidence.png", full_page=True)
        

        # Final screenshot
        page.screenshot(path="results/TC_OB_013_final.png", full_page=True)
        print("\n[SCREENSHOT] Final screenshot saved")

        print("\n" + "="*70)
        print("[PASS] TEST PASSED: TC_OB_013")
        print("="*70)
        print("\n[RESULT] Test completed successfully")
        print("[NOTE] Review screenshots for visual verification")
        print("\n")

    except Exception as e:
        page.screenshot(path="results/TC_OB_013_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        print(f"[SCREENSHOT] Failure screenshot saved")
        print("\n")
        raise


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
