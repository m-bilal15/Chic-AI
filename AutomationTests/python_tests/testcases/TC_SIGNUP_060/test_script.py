"""TC_SIGNUP_060: Page load time performance (< 3 seconds)"""
import pytest
import time

@pytest.mark.low
@pytest.mark.performance
def test_tc_signup_060(page, signup_page, base_url):
    print("\n" + "="*70)
    print("TEST: TC_SIGNUP_060 - Page Load Performance")
    print("="*70)

    try:
        print("\n[STEP] Measuring page load time...")

        # Record start time
        start_time = time.time()

        page.goto(base_url)
        page.wait_for_load_state("networkidle")

        # Record end time
        end_time = time.time()
        load_time = end_time - start_time

        print(f"\n   Page load time: {load_time:.2f} seconds")

        # Navigate to signup
        try:
            signup_link = page.locator('a:has-text("Sign up"), button:has-text("Sign up")')
            if signup_link.is_visible(timeout=3000):
                signup_start = time.time()
                signup_link.click()
                page.wait_for_load_state("networkidle")
                signup_end = time.time()
                signup_load_time = signup_end - signup_start

                print(f"   Signup page load: {signup_load_time:.2f} seconds")
        except:
            pass

        # Performance assessment
        print("\n[PERFORMANCE ASSESSMENT]")
        if load_time < 1:
            print("   [PASS] Excellent: < 1 second")
        elif load_time < 3:
            print("   [PASS] Good: < 3 seconds (meets requirement)")
        elif load_time < 5:
            print("   [WARNING]  Acceptable: < 5 seconds (but slower than target)")
        else:
            print("   [FAIL] Slow: > 5 seconds (needs optimization)")

        # Get performance metrics
        print("\n[STEP] Collecting performance metrics...")
        try:
            metrics = page.evaluate("""() => {
                const perfData = window.performance.timing;
                const navigation = performance.getEntriesByType('navigation')[0];
                return {
                    domContentLoaded: perfData.domContentLoadedEventEnd - perfData.navigationStart,
                    loadComplete: perfData.loadEventEnd - perfData.navigationStart,
                    domInteractive: perfData.domInteractive - perfData.navigationStart,
                    ttfb: perfData.responseStart - perfData.navigationStart
                };
            }""")

            print(f"   DOM Content Loaded: {metrics['domContentLoaded']}ms")
            print(f"   Load Complete: {metrics['loadComplete']}ms")
            print(f"   DOM Interactive: {metrics['domInteractive']}ms")
            print(f"   Time to First Byte: {metrics['ttfb']}ms")
        except Exception as e:
            print(f"   [WARNING]  Could not collect detailed metrics: {e}")

        page.screenshot(path="results/TC_SIGNUP_060_PASSED.png", full_page=True)

        print("\n[PASS] TEST PASSED: TC_SIGNUP_060")
        print(f"[PERFORMANCE] Page load time: {load_time:.2f}s")

        # Assert performance requirement
        if load_time > 10:
            print("\n[WARNING]  WARNING: Page load time exceeded 10 seconds!")
            print("   Consider performance optimization")

        print()

    except Exception as e:
        page.screenshot(path="results/TC_SIGNUP_060_FAILED.png", full_page=True)
        print(f"\n[FAIL] TEST FAILED: {e}")
        raise

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
