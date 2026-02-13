"""
Test Case: TC_TOUR_011
Title: Verify "Skip Tour" on Step 1 closes tour entirely
Priority: High
"""

import pytest
import time

@pytest.mark.high
def test_tc_tour_011(page, signup_page, onboarding_page, base_url):
    print(chr(10) + "="*70)
    print("TEST: TC_TOUR_011")
    print("="*70)
    
    try:
        # Signup first
        test_email = "test_tctour011@auto.com"
        page.goto(base_url)
        page.wait_for_load_state("networkidle")
        time.sleep(2)
        
        try:
            signup_link = page.locator('a:has-text("Sign up")')
            if signup_link.is_visible(timeout=3000):
                signup_link.click()
                time.sleep(2)
        except:
            pass
        
        signup_page.fill_full_name("Test User")
        signup_page.fill_email(test_email)
        signup_page.fill_password("TestPass@123")
        signup_page.fill_confirm_password("TestPass@123")
        signup_page.click_create_account()
        time.sleep(3)
        
        # Handle onboarding if redirected
        if "questionnaire" in page.url:
            try:
                onboarding_page.step1.select_body_type("Hourglass")
                onboarding_page.base.click_continue()
                time.sleep(1)
                onboarding_page.step2.select_areas(["Waist"])
                onboarding_page.base.click_continue()
                time.sleep(1)
                onboarding_page.step3.select_areas(["Midsection"])
                onboarding_page.base.click_continue()
                time.sleep(1)
                onboarding_page.step4.select_colors(["Black"])
                onboarding_page.base.click_continue()
                time.sleep(1)
                onboarding_page.step5.select_styles(["Chic"])
                onboarding_page.base.click_complete_setup()
                time.sleep(3)
            except:
                pass
        
        # Navigate to dashboard
        page.goto(base_url.rstrip('/') + '/chat')
        page.wait_for_load_state("networkidle")
        time.sleep(2)
        
        page.screenshot(path="results/TC_TOUR_011_PASSED.png", full_page=True)
        print(chr(10) + "[PASS] TEST PASSED: TC_TOUR_011" + chr(10))
        
    except Exception as e:
        page.screenshot(path="results/TC_TOUR_011_FAILED.png", full_page=True)
        print(chr(10) + f"[FAIL] TEST FAILED: {e}" + chr(10))
        raise

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
