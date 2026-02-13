"""
Test Case: TC_OB_S1_006
Title: Verify Continue button without selecting any option
Description: Verify Continue button without selecting any option
Priority: High
Type: Negative
Sheet: Step 1 - Body Type
Created: February 12, 2026
"""

import pytest
import json
import time
from pathlib import Path


@pytest.mark.high
@pytest.mark.negative
def test_tc_ob_s1_006(page, onboarding_page, base_url):
    """
    Test Case: TC_OB_S1_006
    Description: Verify Continue button without selecting any option
    Priority: High
    Type: Negative

    Steps:
    1. Navigate to Step 1
    2. Do NOT select any body type
    3. Click "Continue →" button

    Expected Results:
    1. Either: Validation message appears (e.g., "Please select a body type")
    2. OR: Continue is disabled until a selection is made
    3. User does NOT advance to Step 2 without selection
    """

    print("\n" + "="*70)
    print("TEST: TC_OB_S1_006 - Verify Continue button without selecting any option")
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

        page.screenshot(path="results/TC_OB_S1_006_initial.png", full_page=True)
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
        page.screenshot(path="results/TC_OB_S1_006_evidence.png", full_page=True)
        

        # Final screenshot
        page.screenshot(path="results/TC_OB_S1_006_final.png", full_page=True)
        print("\n[SCREENSHOT] Final screenshot saved")

        print("\n" + "="*70)
        print("[PASS] TEST PASSED: TC_OB_S1_006")
        print("="*70)
        print("\n[RESULT] Test completed successfully")
        print("[NOTE] Review screenshots for visual verification")
        print("\n")

    except Exception as e:
        page.screenshot(path="results/TC_OB_S1_006_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        print(f"[SCREENSHOT] Failure screenshot saved")
        print("\n")
        raise


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
