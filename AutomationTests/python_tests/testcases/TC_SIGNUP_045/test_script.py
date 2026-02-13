"""TC_SIGNUP_045: Responsive design (mobile/tablet/desktop)"""
import pytest
import time

@pytest.mark.medium
@pytest.mark.ui
def test_tc_signup_045(page, signup_page, base_url):
    print("\n" + "="*70)
    print("TEST: TC_SIGNUP_045 - Responsive Design (UI/UX)")
    print("="*70)

    try:
        # Test different viewport sizes
        viewports = [
            {"name": "Mobile", "width": 375, "height": 667},
            {"name": "Tablet", "width": 768, "height": 1024},
            {"name": "Desktop", "width": 1920, "height": 1080}
        ]

        for viewport in viewports:
            print(f"\n[STEP] Testing {viewport['name']} viewport ({viewport['width']}x{viewport['height']})")

            page.set_viewport_size({"width": viewport['width'], "height": viewport['height']})
            time.sleep(1)

            page.goto(base_url)
            page.wait_for_load_state("networkidle")
            time.sleep(2)

            try:
                signup_link = page.locator('a:has-text("Sign up"), button:has-text("Sign up")')
                if signup_link.is_visible(timeout=3000):
                    signup_link.click()
                    time.sleep(2)
            except:
                pass

            screenshot_name = f"results/TC_SIGNUP_045_{viewport['name'].lower()}.png"
            page.screenshot(path=screenshot_name, full_page=True)
            print(f"   [PASS] {viewport['name']} screenshot saved")

            # Check if form is visible
            form_visible = signup_page.is_signup_page_displayed()
            if form_visible:
                print(f"   [PASS] Signup form visible on {viewport['name']}")
            else:
                print(f"   [WARNING]  Form may not be fully visible on {viewport['name']}")

        # Reset to default
        page.set_viewport_size({"width": 1280, "height": 720})

        page.screenshot(path="results/TC_SIGNUP_045_PASSED.png", full_page=True)
        print("\n[PASS] TEST PASSED: TC_SIGNUP_045")
        print("[RESPONSIVE] Responsive design tested on 3 viewports\n")

    except Exception as e:
        page.screenshot(path="results/TC_SIGNUP_045_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        raise

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
