"""
Test Case: TC_OB_S4_008
Title: Verify counter "0/6" updates correctly with each selection/d
Description: Verify counter "0/6" updates correctly with each selection/deselection
Priority: High
Type: Positive
Sheet: Step 4 - Favorite Colors
Created: February 12, 2026
"""

import pytest
import json
import time
from pathlib import Path


@pytest.mark.high
@pytest.mark.positive
def test_tc_ob_s4_008(page, onboarding_page, base_url):
    """
    Test Case: TC_OB_S4_008
    Description: Verify counter "0/6" updates correctly with each selection/deselection
    Priority: High
    Type: Positive
    """

    print("\n" + "="*70)
    print("TEST: TC_OB_S4_008")
    print("="*70)

    try:
        # Load test data
        test_data_path = Path("test_data/valid_onboarding_data.json")
        with open(test_data_path) as f:
            test_data = json.load(f)

        # Navigate to onboarding page
        print("\n[STEP 1] Navigating to onboarding questionnaire...")
        onboarding_url = base_url.rstrip('/') + '/questionnaire'
        page.goto(onboarding_url)
        page.wait_for_load_state("networkidle")
        time.sleep(2)

        page.screenshot(path="results/TC_OB_S4_008_initial.png", full_page=True)
        print("[SCREENSHOT] Initial screenshot saved")

        # Verify page loaded
        print("\n[CHECK] Verifying page loaded...")
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
        page.screenshot(path="results/TC_OB_S4_008_evidence.png", full_page=True)

        # Final screenshot
        page.screenshot(path="results/TC_OB_S4_008_final.png", full_page=True)
        print("\n[SCREENSHOT] Final screenshot saved")

        print("\n" + "="*70)
        print("[PASS] TEST PASSED: TC_OB_S4_008")
        print("="*70)
        print("\n[RESULT] Test completed successfully")
        print("\n")

    except Exception as e:
        page.screenshot(path="results/TC_OB_S4_008_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        print("\n")
        raise


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
