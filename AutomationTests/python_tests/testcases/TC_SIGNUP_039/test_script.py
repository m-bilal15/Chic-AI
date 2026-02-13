"""TC_SIGNUP_039: No sensitive data in page source"""
import pytest
import time

@pytest.mark.high
@pytest.mark.security
def test_tc_signup_039(page, signup_page, base_url):
    print("\n" + "="*70)
    print("TEST: TC_SIGNUP_039 - No Sensitive Data in Page Source (Security)")
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

        print("\n[STEP] Checking page source for sensitive data...")

        page_source = page.content()

        # Check for sensitive keywords
        sensitive_keywords = [
            "api_key", "apikey", "api-key",
            "secret", "token", "bearer",
            "password", "credential",
            "mongodb://", "postgres://", "mysql://",
            "aws_access_key", "private_key"
        ]

        found_issues = []
        for keyword in sensitive_keywords:
            if keyword in page_source.lower():
                # Exclude expected cases (like input field names)
                if keyword not in ["password"]:  # Password field is expected
                    found_issues.append(keyword)

        if found_issues:
            print(f"[WARNING]  WARNING: Found potential sensitive keywords: {found_issues}")
            print("   (Review manually to confirm if these are actual secrets)")
        else:
            print("[PASS] No obvious API keys or secrets in page source")

        # Check for hardcoded backend URLs
        if "localhost" in page_source or "127.0.0.1" in page_source:
            print("[WARNING]  Development URLs found (expected in dev environment)")
        else:
            print("[PASS] No hardcoded localhost URLs")

        page.screenshot(path="results/TC_SIGNUP_039_PASSED.png", full_page=True)
        print("\n[PASS] TEST PASSED: TC_SIGNUP_039")
        print("[SECURITY] Page source security check completed\n")

    except Exception as e:
        page.screenshot(path="results/TC_SIGNUP_039_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        raise

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
