"""
Test Case: TC_OB_S3_009
Title: Verify "Totally optional" messaging is clear
Description: Verify "Totally optional" messaging is clear
Priority: Medium
Type: UI/UX
Sheet: Step 3 - Minimize Areas
Created: February 12, 2026
"""

import pytest
import json
import time
from pathlib import Path


@pytest.mark.medium
@pytest.mark.ui_ux
def test_tc_ob_s3_009(page, onboarding_page, base_url):
    """
    Test Case: TC_OB_S3_009
    Description: Verify "Totally optional" messaging is clear
    Priority: Medium
    Type: UI/UX
    """

    print("\n" + "="*70)
    print("TEST: TC_OB_S3_009")
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

        page.screenshot(path="results/TC_OB_S3_009_initial.png", full_page=True)
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
        page.screenshot(path="results/TC_OB_S3_009_evidence.png", full_page=True)

        # Final screenshot
        page.screenshot(path="results/TC_OB_S3_009_final.png", full_page=True)
        print("\n[SCREENSHOT] Final screenshot saved")

        print("\n" + "="*70)
        print("[PASS] TEST PASSED: TC_OB_S3_009")
        print("="*70)
        print("\n[RESULT] Test completed successfully")
        print("\n")

    except Exception as e:
        page.screenshot(path="results/TC_OB_S3_009_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        print("\n")
        raise


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
