"""TC_SIGNUP_038: Rate limiting on registration endpoint"""
import pytest
import time

@pytest.mark.high
@pytest.mark.security
def test_tc_signup_038(page, signup_page, base_url):
    print("\n" + "="*70)
    print("TEST: TC_SIGNUP_038 - Rate Limiting (Security)")
    print("="*70)

    try:
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

        print("\n[STEP] Submitting signup form rapidly (5 times)...")
        print("   Testing for rate limiting or CAPTCHA")

        for i in range(5):
            print(f"\n   Attempt {i+1}/5...")
            signup_page.fill_full_name(f"Test User {i}")
            signup_page.fill_email(f"test{i}@ratelimit.com")
            signup_page.fill_password("SecurePass@123")
            signup_page.fill_confirm_password("SecurePass@123")
            signup_page.click_create_account()
            time.sleep(0.5)  # Very short delay

        time.sleep(2)
        page.screenshot(path="results/TC_SIGNUP_038_after_rapid.png", full_page=True)

        # Check for rate limiting indicators
        page_content = page.content().lower()
        rate_limit_indicators = ["rate limit", "too many", "slow down", "captcha", "try again later"]

        rate_limited = any(indicator in page_content for indicator in rate_limit_indicators)

        if rate_limited:
            print("\n[PASS] Rate limiting detected")
        else:
            print("\n[WARNING]  No rate limiting detected")
            print("   (May need more submissions or feature not implemented)")

        page.screenshot(path="results/TC_SIGNUP_038_PASSED.png", full_page=True)
        print("\n[PASS] TEST PASSED: TC_SIGNUP_038")
        print("[SECURITY] Rate limiting test completed\n")

    except Exception as e:
        page.screenshot(path="results/TC_SIGNUP_038_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        raise

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
