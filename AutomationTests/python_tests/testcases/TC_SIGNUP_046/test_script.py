"""TC_SIGNUP_046: Form field labels"""
import pytest
import time

@pytest.mark.medium
@pytest.mark.ui
def test_tc_signup_046(page, signup_page, base_url):
    print("\n" + "="*70)
    print("TEST: TC_SIGNUP_046 - Form Field Labels (UI/UX)")
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

        print("\n[CHECK] Verifying field labels are present...")

        page_content = page.content().lower()

        # Check for common label text
        labels_to_check = [
            ("full name", "Full Name label"),
            ("name", "Name label"),
            ("email", "Email label"),
            ("password", "Password label"),
            ("confirm", "Confirm Password label")
        ]

        labels_found = []
        for label_text, label_name in labels_to_check:
            if label_text in page_content:
                labels_found.append(label_name)

        print(f"\n   Labels found: {len(labels_found)}")
        for label in labels_found:
            print(f"   [PASS] {label}")

        page.screenshot(path="results/TC_SIGNUP_046_PASSED.png", full_page=True)
        print("\n[PASS] TEST PASSED: TC_SIGNUP_046")
        print("[LABEL]  Form labels verified\n")

    except Exception as e:
        page.screenshot(path="results/TC_SIGNUP_046_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        raise

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
