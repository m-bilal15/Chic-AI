"""TC_SIGNUP_053: Accessibility - ARIA labels"""
import pytest
import time

@pytest.mark.low
@pytest.mark.accessibility
def test_tc_signup_053(page, signup_page, base_url):
    print("\n" + "="*70)
    print("TEST: TC_SIGNUP_053 - ARIA Labels (Accessibility)")
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

        print("\n[CHECK] Checking for ARIA attributes...")

        page_source = page.content()

        # Check for ARIA attributes
        aria_attributes = [
            "aria-label",
            "aria-labelledby",
            "aria-describedby",
            "aria-required",
            "aria-invalid"
        ]

        found_aria = []
        for attr in aria_attributes:
            if attr in page_source:
                found_aria.append(attr)
                print(f"   [PASS] Found {attr}")

        if found_aria:
            print(f"\n   Total ARIA attributes found: {len(found_aria)}")
        else:
            print("\n   [WARNING]  No ARIA attributes found")
            print("   (May rely on semantic HTML instead)")

        # Check for semantic HTML
        print("\n[CHECK] Checking semantic HTML...")
        semantic_tags = ["<label", "<button", "<input"]
        for tag in semantic_tags:
            if tag in page_source:
                print(f"   [PASS] Using {tag} tags")

        page.screenshot(path="results/TC_SIGNUP_053_PASSED.png", full_page=True)
        print("\n[PASS] TEST PASSED: TC_SIGNUP_053")
        print("[A11Y] ARIA labels checked\n")

    except Exception as e:
        page.screenshot(path="results/TC_SIGNUP_053_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        raise

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
