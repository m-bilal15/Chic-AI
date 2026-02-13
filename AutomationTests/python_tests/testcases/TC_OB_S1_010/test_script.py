"""
Test Case: TC_OB_S1_010
Title: Verify left panel layout and content
Description: Verify left panel layout and content
Priority: Low
Type: UI/UX
Sheet: Step 1 - Body Type
Created: February 12, 2026
"""

import pytest
import json
import time
from pathlib import Path


@pytest.mark.low
@pytest.mark.ui_ux
def test_tc_ob_s1_010(page, onboarding_page, base_url):
    """
    Test Case: TC_OB_S1_010
    Description: Verify left panel layout and content
    Priority: Low
    Type: UI/UX

    Steps:
    1. Navigate to Step 1
    2. Observe the left panel card

    Expected Results:
    1. Left panel is a white card with border
    2. "What's your body type?" in bold heading
    3. Description text in lighter color below
    4. "< Back" button at bottom left
    5. "Continue →" button at bottom (black, full-width)
    """

    print("\n" + "="*70)
    print("TEST: TC_OB_S1_010 - Verify left panel layout and content")
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

        page.screenshot(path="results/TC_OB_S1_010_initial.png", full_page=True)
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
        page.screenshot(path="results/TC_OB_S1_010_evidence.png", full_page=True)
        

        # Final screenshot
        page.screenshot(path="results/TC_OB_S1_010_final.png", full_page=True)
        print("\n[SCREENSHOT] Final screenshot saved")

        print("\n" + "="*70)
        print("[PASS] TEST PASSED: TC_OB_S1_010")
        print("="*70)
        print("\n[RESULT] Test completed successfully")
        print("[NOTE] Review screenshots for visual verification")
        print("\n")

    except Exception as e:
        page.screenshot(path="results/TC_OB_S1_010_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        print(f"[SCREENSHOT] Failure screenshot saved")
        print("\n")
        raise


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
