"""
CHIC-AI Test Automation - Pytest Configuration & Fixtures
Created: February 12, 2026

This file contains pytest fixtures and hooks for test setup/teardown.
"""

import pytest
import os
import sys
from datetime import datetime
from pathlib import Path
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from pages.login_page import LoginPage


# ====================
# Pytest Hooks
# ====================

def pytest_configure(config):
    """Called before test run starts"""
    # Create results directories
    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)
    (results_dir / "failures").mkdir(exist_ok=True)
    (results_dir / "logs").mkdir(exist_ok=True)
    (results_dir / "videos").mkdir(exist_ok=True)

    print("\n" + "="*70)
    print("CHIC-AI Test Automation - Starting Test Execution")
    print("="*70)
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Results: {results_dir.absolute()}")
    print("="*70 + "\n")


def pytest_collection_finish(session):
    """Called after test collection"""
    print(f"\nCollected {len(session.items)} test(s)\n")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture test results and take screenshots on failure
    """
    outcome = yield
    report = outcome.get_result()

    # Only process during test call phase (not setup/teardown)
    if report.when == "call":
        # Get the page fixture if it exists
        page = item.funcargs.get("page")

        if report.failed and page:
            # Take screenshot on failure
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = item.nodeid.replace("::", "_").replace("/", "_")
            screenshot_path = f"results/failures/{test_name}_{timestamp}.png"

            try:
                page.screenshot(path=screenshot_path)
                print(f"\n[SCREENSHOT] Failure screenshot saved: {screenshot_path}")
            except Exception as e:
                print(f"\n[WARNING] Could not save screenshot: {e}")


# ====================
# Session-Scoped Fixtures
# ====================

@pytest.fixture(scope="session")
def browser_type_launch_args():
    """Browser launch arguments"""
    return {
        "headless": False,
        "slow_mo": 2000,  # Slow down by 2 seconds for visibility
        "args": [
            "--disable-dev-shm-usage",
            "--no-sandbox"
        ]
    }


@pytest.fixture(scope="session")
def browser_context_args():
    """Browser context arguments"""
    return {
        "viewport": {"width": 1280, "height": 720},
        "record_video_dir": "results/videos/",
        "record_video_size": {"width": 1280, "height": 720}
    }


# ====================
# Function-Scoped Fixtures
# ====================

@pytest.fixture(scope="function")
def playwright():
    """Playwright instance"""
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="function")
def browser(playwright, browser_type_launch_args):
    """Browser instance"""
    browser = playwright.chromium.launch(**browser_type_launch_args)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def context(browser, browser_context_args):
    """Browser context"""
    context = browser.new_context(**browser_context_args)
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context):
    """Page instance"""
    page = context.new_page()
    yield page
    page.close()


@pytest.fixture(scope="function")
def login_page(page):
    """Login page object"""
    from pages.login_page import LoginPage
    return LoginPage(page)


@pytest.fixture(scope="function")
def signup_page(page):
    """Signup page object"""
    from pages.signup_page import SignupPage
    return SignupPage(page)


@pytest.fixture(scope="function")
def onboarding_page(page):
    """Onboarding flow object"""
    from pages.onboarding_page import OnboardingFlow
    return OnboardingFlow(page)


# ====================
# Utility Fixtures
# ====================

@pytest.fixture(scope="session")
def base_url():
    """Base URL for application"""
    # Can be overridden with environment variable
    return os.getenv("BASE_URL", "http://localhost:5173")


@pytest.fixture(scope="function")
def test_data():
    """Load test data"""
    return {
        "valid_email": os.getenv("TEST_EMAIL", "bilal@test.com"),
        "valid_password": os.getenv("TEST_PASSWORD", "ValidPass@123"),
        "invalid_email": "invalid@test.com",
        "invalid_password": "WrongPassword123"
    }


# ====================
# Markers
# ====================

def pytest_collection_modifyitems(config, items):
    """
    Modify test collection to add markers automatically
    """
    for item in items:
        # Auto-mark validation tests
        if "validation" in item.nodeid.lower():
            item.add_marker(pytest.mark.validation)

        # Auto-mark by test ID
        if "LOGIN_011" in item.nodeid or "LOGIN_012" in item.nodeid or \
           "LOGIN_013" in item.nodeid or "LOGIN_014" in item.nodeid:
            item.add_marker(pytest.mark.validation)
            item.add_marker(pytest.mark.critical)


# ====================
# Session Teardown
# ====================

def pytest_sessionfinish(session, exitstatus):
    """Called after whole test run"""
    print("\n" + "="*70)
    print("Test Execution Complete")
    print("="*70)
    print(f"Results saved in: results/")
    print(f"HTML Report: results/report.html")
    print("="*70 + "\n")
