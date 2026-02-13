# CHIC Login Page - Python Test Automation

## Overview

**Test Framework:** Playwright + Python
**Total Test Cases:** 50 (Each in separate folder with individual test_script.py)
**Execution:** Visible browser with 2-second delays
**QA Lead:** Bilal

---

## Folder Structure

```
python_tests/
├── pages/
│   ├── base_page.py           # Base page object
│   └── login_page.py          # Login page object
│
├── testcases/
│   ├── TC_LOGIN_001/
│   │   └── test_script.py     # Individual test script
│   ├── TC_LOGIN_002/
│   │   └── test_script.py
│   ├── TC_LOGIN_003/
│   │   └── test_script.py
│   ... (50 folders total)
│   └── TC_LOGIN_050/
│       └── test_script.py
│
├── results/
│   ├── Passed/                # Passed tests with artifacts
│   ├── Failed/                # Failed tests with artifacts
│   └── SUMMARY.json           # Overall summary
│
├── run_all_tests.py           # Runs all 50 tests
└── generate_test_scripts.py   # Generator script
```

---

## Prerequisites

1. **Install Dependencies:**
```bash
pip install playwright pytest pytest-playwright
python -m playwright install chromium
```

2. **Start CHIC Application:**
```bash
# In a separate terminal
cd C:\Users\usman.GADGET\Downloads\Chic-AI\chich
npm run dev
```
App must be running on: http://localhost:5173

---

## Running Tests

### Run Individual Test
```bash
cd python_tests/testcases/TC_LOGIN_001
python test_script.py
```

**You will see:**
- Browser opens (visible)
- Actions happen with 2-second delays
- Console logs showing each step
- Video recording saved automatically

### Run All 50 Tests
```bash
cd python_tests
python run_all_tests.py
```

**This will:**
- Execute all 50 tests one by one
- Show browser for each test
- Organize results into Passed/Failed folders
- Generate summary report

---

## Test Execution Features

### What You'll See:
1. **Browser Opens** - Chromium window visible
2. **Slow Motion** - 2 seconds between actions
3. **Console Logs:**
   ```
   ================================================================================
   Test Case: TC_LOGIN_001
   Description: Verify Login page loads successfully
   Priority: Critical | Type: Positive
   ================================================================================

   Launching browser...

   Starting test execution...

   [STEP] Navigating to login page...
   [DONE] Page loaded
   [CHECK] Verifying login page elements...
   [PASS] Login page elements found
   [PASS] Logo is visible
   [PASS] Welcome heading visible
   [PASS] Sign up button visible

   ================================================================================
   PASSED: TC_LOGIN_001
   ================================================================================
   ```

4. **Automatic Recording:**
   - Screenshots saved
   - Video recorded
   - Results organized

---

## Results Structure

After running tests:

```
results/
├── Passed/
│   ├── TC_LOGIN_001/
│   │   ├── test_output.txt      # Console output
│   │   ├── TEST_REPORT.md       # Readable report
│   │   ├── video.webm           # Video recording
│   │   └── screenshot.png       # Screenshots
│   ├── TC_LOGIN_002/
│   └── ... (all passed tests)
│
├── Failed/
│   ├── TC_LOGIN_XXX/
│   │   ├── test_output.txt
│   │   ├── TEST_REPORT.md
│   │   ├── video.webm
│   │   └── TC_LOGIN_XXX_FAILED.png
│   └── ... (all failed tests)
│
└── SUMMARY.json                 # Overall summary
```

---

## Test Case Example

### TC_LOGIN_001 Test Script:
```python
def test_tc_login_001():
    with sync_playwright() as p:
        # Launch browser (VISIBLE, SLOW)
        browser = p.chromium.launch(
            headless=False,      # Browser visible
            slow_mo=2000         # 2-second delays
        )

        # Create page
        context = browser.new_context(
            viewport={"width": 1280, "height": 720},
            record_video_dir="../../results/TC_LOGIN_001/"
        )
        page = context.new_page()
        login_page = LoginPage(page)

        # Execute test
        login_page.navigate_to_login()
        assert login_page.is_login_page_displayed()
        assert login_page.is_logo_visible()
        # ... more assertions
```

---

## Quick Commands

### Run Specific Test:
```bash
cd python_tests/testcases/TC_LOGIN_001
python test_script.py
```

### Run All Tests:
```bash
cd python_tests
python run_all_tests.py
```

### Run Multiple Specific Tests:
```bash
cd python_tests
# Edit run_all_tests.py to filter specific test IDs
```

---

## Configuration

### Slow Motion:
Change `slow_mo=2000` in test_script.py to adjust delay:
- `slow_mo=1000` - 1 second delay
- `slow_mo=3000` - 3 second delay

### Headless Mode:
Change `headless=False` to `headless=True` to run without visible browser

### Viewport:
Change `viewport` in test_script.py:
- Desktop: `{"width": 1280, "height": 720}`
- Mobile: `{"width": 375, "height": 812}`
- Tablet: `{"width": 768, "height": 1024}`

---

## Troubleshooting

### Error: Connection Refused
- **Cause:** Application not running
- **Solution:** Start app: `cd chich && npm run dev`

### Error: Module not found
- **Cause:** Playwright not installed
- **Solution:** `pip install playwright && python -m playwright install chromium`

### Error: Selector not found
- **Cause:** UI changed
- **Solution:** Update selectors in `pages/login_page.py`

---

## Next Steps

1. **Start Application** (if not running)
2. **Run One Test** to see it work
3. **Run All Tests** using run_all_tests.py
4. **Review Results** in Passed/Failed folders
5. **Add More Tests** - Create new folders and test_script.py files

---

**Framework Status:** READY ✅
**Total Test Scripts:** 50
**Execution Mode:** Visible + Slow Motion
**Results:** Auto-organized into Passed/Failed

---

**Created by:** Bilal - SQA Lead
**Date:** February 2026
