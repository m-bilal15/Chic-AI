# CHIC-AI Test Automation Guidelines

**Project:** CHIC Login Page Test Automation
**Framework:** Python + Playwright + Pytest
**QA Lead:** Bilal
**Last Updated:** February 12, 2026 (v2.0 - Production-Ready)
**Framework Version:** 2.0

---

## 📚 Quick Links to Documentation

- **SETUP_GUIDE.md** - Installation, setup, and troubleshooting
- **STRUCTURE_ANALYSIS_AND_IMPROVEMENTS.md** - Framework analysis and improvements
- **IMPLEMENTATION_STATUS.md** - Current status and next steps
- **This file (CLAUDE.md)** - Testing standards and guidelines

---

## 🎯 CRITICAL RULE: Evidence-Based Test Validation

**BEFORE marking any test as PASSED or FAILED, you MUST:**

1. **Review ALL evidence files:**
   - Screenshots (.png files)
   - Screen recordings (.webm/.mp4 files)
   - Test output logs

2. **Analyze what actually happened in the UI:**
   - Don't rely solely on automated test assertions
   - Check if validation messages are displayed (including native HTML5 tooltips)
   - Verify actual vs expected behavior visually
   - Look for both custom error messages AND native browser validation

3. **Make informed decisions:**
   - Automated tests can have false negatives (test fails but feature works)
   - If screenshots show validation working, the test should PASS
   - If evidence contradicts the test result, investigate the test script logic

**Example:** Native HTML5 validation tooltips (like "Please fill out this field") are valid validation - don't mark as failed just because custom error divs weren't found.

---

## 1. 📝 Test Script Writing Rules

### 1.1 Location & Structure
```
Chic-AI/
├── .gitignore                      ✨ Version control rules
├── CLAUDE.md                       ✨ This file
└── AutomationTests/
    ├── SETUP_GUIDE.md              ✨ Installation guide
    ├── STRUCTURE_ANALYSIS_AND_IMPROVEMENTS.md
    ├── IMPLEMENTATION_STATUS.md
    └── python_tests/
        ├── requirements.txt        ✨ Python dependencies
        ├── pytest.ini              ✨ Pytest configuration
        ├── conftest.py             ✨ Pytest fixtures
        ├── .env.example            ✨ Environment template
        ├── .env                    ✨ Your config (gitignored)
        ├── config/
        │   ├── config.ini          ✨ Multi-environment config
        │   └── selectors.json
        ├── test_data/              ✨ Test data files
        │   ├── valid_credentials.json
        │   └── invalid_credentials.json
        ├── pages/                  ✨ Page Object Model
        │   ├── base_page.py
        │   └── login_page.py
        ├── utils/                  ✨ Helper functions
        │   ├── config_reader.py
        │   ├── logger.py
        │   └── helpers.py
        ├── testcases/              ✨ Test scripts
        │   ├── TC_LOGIN_001/
        │   │   └── test_script.py
        │   └── TC_LOGIN_XXX/
        └── results/
            ├── Passed/
            ├── Failed/
            ├── failures/           ✨ Auto-screenshots
            ├── logs/               ✨ Log files
            ├── report.html         ✨ HTML report
            ├── SUMMARY.md
            └── SUMMARY.json
```

### 1.2 Naming Conventions
- **Test files:** `TC_LOGIN_XXX.py` (where XXX is 001-999)
- **Test function:** `def test_login_XXX():` inside each file
- **One test case per file** - NO combined tests
- **Result folders:** `TC_LOGIN_XXX/` (no .py extension)

### 1.3 Test Script Templates

#### Option 1: Legacy Template (Still Supported)
```python
# testcases/TC_LOGIN_XXX/test_script.py
from playwright.sync_api import sync_playwright
import time

def test_tc_login_XXX():
    """
    Test Case: TC_LOGIN_XXX
    Description: [Clear description]
    Priority: [Critical/High/Medium/Low]
    Type: [Positive/Negative]
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            record_video_dir="results/TC_LOGIN_XXX/"
        )
        page = context.new_page()

        try:
            page.goto("http://localhost:5173")
            page.wait_for_load_state("networkidle")

            # Test logic here

            page.screenshot(path="results/TC_LOGIN_XXX_PASSED.png")
            print("✅ Test PASSED")

        except Exception as e:
            page.screenshot(path="results/TC_LOGIN_XXX_FAILED.png")
            print(f"❌ Test FAILED: {e}")
            raise
        finally:
            context.close()
            browser.close()

if __name__ == "__main__":
    test_tc_login_XXX()
```

#### Option 2: Modern Pytest Fixture Template (RECOMMENDED) ✨
```python
# testcases/TC_LOGIN_XXX/test_script.py
import pytest
from pages.login_page import LoginPage

@pytest.mark.critical          # Add appropriate markers
@pytest.mark.validation
def test_tc_login_XXX(page, login_page, base_url):
    """
    Test Case: TC_LOGIN_XXX
    Description: [Clear description]
    Priority: Critical
    Type: Negative - Validation
    """
    # Navigate to login page
    page.goto(base_url)
    page.wait_for_load_state("networkidle")

    # Test logic using page object
    login_page.navigate()

    # Assertions
    assert login_page.is_visible()

    print("✅ Test PASSED")

# Markers available:
# @pytest.mark.smoke
# @pytest.mark.regression
# @pytest.mark.validation
# @pytest.mark.security
# @pytest.mark.critical
# @pytest.mark.high
# @pytest.mark.medium
# @pytest.mark.low
```

**Key Differences:**
- ✅ **Fixtures auto-handle** browser/page setup (no manual code needed)
- ✅ **Auto-screenshots** on failure (via conftest.py hooks)
- ✅ **Markers** for test categorization
- ✅ **Cleaner, shorter** test code
- ✅ **Page objects** integrated
- ✅ **Config from .env** and config.ini

### 1.4 Best Practices
- ✅ **Use pytest fixtures** (modern approach - recommended)
- ✅ **Add pytest markers** (@pytest.mark.smoke, @pytest.mark.critical)
- ✅ **Use page objects** from pages/ folder
- ✅ **Always capture screenshots** (auto-captured on failure via conftest.py)
- ✅ **Always record videos** using `record_video_dir` or fixtures
- ✅ **Use explicit waits** (`page.wait_for_load_state()`, `page.wait_for_selector()`)
- ✅ **Add descriptive print statements** or use logger
- ✅ **Test one scenario per file** - don't combine multiple test cases
- ✅ **Read configs from .env** and config.ini (never hardcode)
- ❌ **Never hardcode URLs** - use `base_url` fixture or config
- ❌ **Never hardcode credentials** - use .env variables
- ❌ **Never use generic names** like `test_login.py`
- ❌ **Never skip evidence capture** (screenshots/videos)
- ❌ **Never commit .env** or sensitive data to git

---

## 2. 🚀 Test Execution Rules

### 2.0 Setup (First Time Only)

**Before running tests for the first time:**
```bash
# 1. Navigate to project
cd AutomationTests/python_tests

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Install Playwright browsers
playwright install chromium

# 6. Configure environment
cp .env.example .env
# Edit .env with your credentials

# 7. Verify setup
pytest --collect-only
```

**See SETUP_GUIDE.md for detailed instructions.**

### 2.1 Running Tests

**Using Pytest (RECOMMENDED):**
```bash
# Activate virtual environment first
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

# Run all tests
pytest

# Run with verbose output
pytest -v

# Run with HTML report
pytest --html=results/report.html

# Run specific test
pytest testcases/TC_LOGIN_001/test_script.py

# Run by marker
pytest -m smoke           # Smoke tests only
pytest -m critical        # Critical tests only
pytest -m validation      # Validation tests only

# Run in parallel
pytest -n auto            # Auto-detect CPU cores
pytest -n 4               # Use 4 workers

# Stop on first failure
pytest -x

# View available markers
pytest --markers
```

**Using run_all_tests.py (Legacy):**
```bash
cd AutomationTests/python_tests
python run_all_tests.py
```

**Individual test (Legacy):**
```bash
cd AutomationTests/python_tests
python testcases/TC_LOGIN_001/test_script.py
```

### 2.2 Result Organization

**AFTER each test execution:**

1. **Check evidence files FIRST:**
   - View `results/TC_LOGIN_XXX_FAILED.png` or `TC_LOGIN_XXX_PASSED.png`
   - Watch `results/TC_LOGIN_XXX/video.webm` if needed
   - Read `results/TC_LOGIN_XXX/test_output.txt`

2. **Make evidence-based decision:**
   - If screenshots show expected behavior = PASS
   - If screenshots show unexpected behavior = FAIL
   - Don't blindly trust automation assertions

3. **Organize into folders:**

**For PASSED tests:**
```bash
mkdir -p results/Passed/TC_LOGIN_XXX
mv results/TC_LOGIN_XXX_PASSED.png results/Passed/TC_LOGIN_XXX/
mv results/TC_LOGIN_XXX/video.webm results/Passed/TC_LOGIN_XXX/
# Create TEST_REPORT.md in Passed/TC_LOGIN_XXX/
```

**For FAILED tests:**
```bash
mkdir -p results/Failed/TC_LOGIN_XXX
mv results/TC_LOGIN_XXX_FAILED.png results/Failed/TC_LOGIN_XXX/
mv results/TC_LOGIN_XXX/video.webm results/Failed/TC_LOGIN_XXX/
# Create BUG_REPORT.md in Failed/TC_LOGIN_XXX/
```

### 2.3 Folder Structure After Execution
```
results/
├── Passed/
│   ├── TC_LOGIN_001/
│   │   ├── TC_LOGIN_001_PASSED.png
│   │   ├── video.webm
│   │   ├── test_output.txt
│   │   └── TEST_REPORT.md
│   └── TC_LOGIN_002/
│       └── [same structure]
├── Failed/
│   ├── TC_LOGIN_XXX/
│   │   ├── TC_LOGIN_XXX_FAILED.png
│   │   ├── video.webm
│   │   ├── test_output.txt
│   │   └── BUG_REPORT.md
│   ├── README.md
│   └── MASTER_BUG_REPORT_ARCHIVED.md
├── failures/                    ✨ Auto-screenshots from conftest.py
│   └── test_tc_login_XXX_timestamp.png
├── logs/                        ✨ Log files
│   └── pytest.log
├── videos/                      ✨ Video recordings
├── report.html                  ✨ HTML report (pytest-html)
├── SUMMARY.md
├── SUMMARY.json
└── FOLDER_STRUCTURE_VERIFIED.md
```

---

## 2.4 Configuration Management ✨

### Environment Variables (.env)
```bash
# Never commit .env to git!
# Use .env.example as template

ENVIRONMENT=dev
TEST_EMAIL=bilal@test.com
TEST_PASSWORD=ValidPass@123
BASE_URL=http://localhost:5173
HEADLESS=false
BROWSER=chromium
```

### Multi-Environment Config (config/config.ini)
```ini
[dev]
base_url = http://localhost:5173
headless = false
timeout = 30000

[staging]
base_url = https://staging.chic-ai.com
headless = true

[production]
base_url = https://chic-ai.com
headless = true
```

**Switch environments:**
```bash
# Set in .env
ENVIRONMENT=staging

# Or via command line
export ENVIRONMENT=staging  # Mac/Linux
set ENVIRONMENT=staging     # Windows
pytest
```

---

## 3. 📋 Test Case Creation Rules

### 3.1 One Test = One File Rule

**ALWAYS create a separate Python file for each test case:**

✅ **CORRECT:**
```
test_cases/TC_LOGIN_001.py  → Tests valid login only
test_cases/TC_LOGIN_002.py  → Tests invalid email only
test_cases/TC_LOGIN_003.py  → Tests invalid password only
```

❌ **WRONG:**
```
test_cases/login_tests.py   → Contains all login tests (NO!)
```

### 3.2 Test Case Numbering

- Use sequential numbering: 001, 002, 003, etc.
- Group by feature:
  - 001-010: Valid login scenarios
  - 011-020: Validation tests
  - 021-030: Error handling
  - etc.

### 3.3 Test Independence

Each test MUST:
- ✅ Be runnable independently
- ✅ Have its own setup and teardown
- ✅ Not depend on other tests
- ✅ Clean up after itself
- ❌ Never share state with other tests
- ❌ Never assume execution order

---

## 4. 🐛 Bug Report Creation Rules

### 4.1 When to Create Bug Reports

**Create BUG_REPORT.md ONLY when:**
1. ✅ You've reviewed the evidence (screenshots/videos)
2. ✅ The evidence confirms the bug exists
3. ✅ The actual behavior differs from expected behavior
4. ❌ **DO NOT create if automated test failed but evidence shows feature works!**

### 4.2 Bug Report Template

Save as `results/Failed/TC_LOGIN_XXX/BUG_REPORT.md`:

```markdown
# Bug Report - TC_LOGIN_XXX

## 1. SUMMARY

**Bug ID:** BUG-LOGIN-XXX
**Test Case ID:** TC_LOGIN_XXX
**Title:** [Clear, concise bug title]
**Severity:** [CRITICAL/HIGH/MEDIUM/LOW]
**Priority:** [Critical/High/Medium/Low]
**Status:** Open
**Found By:** Bilal - SQA Lead
**Date:** [Date]

### Description:
[Clear description of what went wrong]

---

## 2. STEPS TO REPRODUCE

1. [Step 1]
2. [Step 2]
3. [Step 3]
...

**Expected Result:**
- [What should happen]

**Actual Result:**
- [What actually happened]

---

## 3. SCREENSHOT

**Location:** `TC_LOGIN_XXX_FAILED.png`

**Evidence:** [Description of what the screenshot shows]

---

## 4. SCREEN RECORDING

**Location:** `TC_LOGIN_XXX/video.webm`

**Video Evidence:**
- [What the video shows]

**Duration:** [X seconds]

---

## 5. PLATFORM

**Operating System:** Windows 11 Pro 10.0.26200
**Browser:** Chromium (Playwright)
**Browser Version:** [Version]
**Screen Resolution:** 1280 x 720
**Application URL:** http://localhost:5173
**Environment:** Development/Local

---

## 6. TEST TYPE

**Category:** [Functional/Validation/Integration/etc.]
**Type:** [Positive/Negative]
**Priority:** [Critical/High/Medium/Low]
**Test Automation:** Python + Playwright

---

## ADDITIONAL INFORMATION

### Error Message:
```
[Actual error from test]
```

### Test Data:
- **Email:** [value]
- **Password:** [value]

### Impact:
- **User Impact:** [How this affects users]
- **Security Impact:** [Any security concerns]
- **Workaround:** [If any]

### Root Cause:
[Technical explanation of why this failed]

### Recommendation:
1. [Fix suggestion 1]
2. [Fix suggestion 2]

---

**Reported By:** Bilal - SQA Lead
**Test Automation Framework:** Python + Playwright
**Report Date:** [Date]
```

### 4.3 Bug Severity Guidelines

- **CRITICAL:** Blocks core functionality (e.g., can't login at all)
- **HIGH:** Major feature broken (e.g., validation completely missing)
- **MEDIUM:** Feature works but has issues (e.g., wrong error message)
- **LOW:** Minor cosmetic issues (e.g., typo in error message)

### 4.4 Master Bug Report

Update `results/Failed/MASTER_BUG_REPORT.md` with:
- List of all active bugs
- Summary by severity
- Common patterns/root causes
- Overall recommendations

---

## 5. 📊 Summary & Reporting Rules

### 5.1 Update SUMMARY.md After Each Test Run

Include:
- Total tests executed
- Passed count
- Failed count
- Pass rate percentage
- Links to Passed and Failed folders
- Timestamp

### 5.2 Update SUMMARY.json

Maintain machine-readable summary:
```json
{
  "total_tests": 50,
  "passed": 46,
  "failed": 4,
  "pass_rate": 92.0,
  "last_updated": "2026-02-12 00:15:00",
  "failed_tests": ["TC_LOGIN_011", "TC_LOGIN_012"],
  "environment": "http://localhost:5173"
}
```

---

## 6. 🔄 Re-testing Failed Tests

When re-testing a failed test after a fix:

1. **Run the test again**
2. **Check new evidence** (screenshots/videos)
3. **If now passing:**
   ```bash
   mv results/Failed/TC_LOGIN_XXX results/Passed/
   rm results/Passed/TC_LOGIN_XXX/BUG_REPORT.md
   # Create TEST_REPORT.md instead
   ```
4. **Update SUMMARY.md** with new counts
5. **Update MASTER_BUG_REPORT.md** to mark bug as resolved

---

## 7. ⚠️ Common Pitfalls to Avoid

### Testing Practices:
1. ❌ **Ignoring evidence files** - Always check screenshots/videos first
2. ❌ **Trusting automation blindly** - Tests can have false positives/negatives
3. ❌ **Missing native validation** - HTML5 tooltips are valid validation
4. ❌ **Creating bug reports without reviewing evidence**
5. ❌ **Combining multiple tests in one file**
6. ❌ **Not capturing screenshots on both pass and fail**
7. ❌ **Skipping video recording** - Videos provide crucial evidence

### Configuration & Setup:
8. ❌ **Hardcoding URLs/credentials** - Use .env and config.ini
9. ❌ **Committing .env to git** - Always gitignored
10. ❌ **Committing results/screenshots** - Always gitignored
11. ❌ **Running without virtual environment** - Always activate venv
12. ❌ **Skipping requirements.txt update** - Keep dependencies current

### Code Quality:
13. ❌ **Not using page objects** - Use pages/ folder for maintainability
14. ❌ **Not using pytest fixtures** - Modern approach, cleaner code
15. ❌ **Not adding markers** - Use @pytest.mark for categorization
16. ❌ **Not using logger** - Use structured logging, not print statements

---

## 8. ✅ Quality Checklist

### Before Marking Tests as Complete:

**Test Quality:**
- [ ] All test files follow naming convention `TC_LOGIN_XXX/test_script.py`
- [ ] Each test has screenshot evidence
- [ ] Each test has video recording
- [ ] Evidence has been manually reviewed ✨ CRITICAL
- [ ] Results are organized in Passed/Failed folders
- [ ] Bug reports created only for real bugs (verified via evidence)
- [ ] Test scripts are independent and rerunnable
- [ ] All assertions have clear error messages

**Configuration:**
- [ ] No hardcoded URLs (using base_url or config)
- [ ] No hardcoded credentials (using .env)
- [ ] .env not committed to git
- [ ] Virtual environment activated

**Modern Practices:**
- [ ] Using pytest fixtures (recommended)
- [ ] Using page objects from pages/ folder
- [ ] Added pytest markers (@pytest.mark.smoke, etc.)
- [ ] Tests run successfully with `pytest`
- [ ] HTML report generated successfully

**Documentation:**
- [ ] SUMMARY.md updated with accurate counts
- [ ] SUMMARY.json updated
- [ ] TEST_REPORT.md or BUG_REPORT.md created
- [ ] Comments added for complex logic

**Framework Health:**
- [ ] `pytest --collect-only` shows all tests
- [ ] `pytest -m smoke` runs successfully
- [ ] No import errors or missing dependencies
- [ ] All fixtures working correctly

---

## 9. 🎓 Learning from This Project

### Key Lesson 1: Evidence-Based Validation
Always verify automated test results with visual evidence. In this project, 5 tests were incorrectly marked as FAILED because the automation looked for custom error messages in the DOM, but the application correctly used native HTML5 validation (browser tooltips). The screenshots proved validation was working perfectly.

**Result:** 50/50 tests PASSED (100% pass rate) after evidence review!

**Takeaway:**
- ✅ Automation helps, but human verification is crucial
- ✅ Evidence (screenshots/videos) is the source of truth
- ✅ Different validation implementations (native vs custom) are both valid
- ✅ Always review screenshots before reporting bugs

### Key Lesson 2: Framework Evolution
This framework evolved from basic scripts to a production-ready system:

**Phase 1 (Initial):**
- Manual setup
- Hardcoded values
- No configuration management
- Basic reporting

**Phase 2 (Current - v2.0):**
- ✅ requirements.txt for easy setup
- ✅ pytest fixtures for clean code
- ✅ Configuration management (.env, config.ini)
- ✅ Version control (.gitignore)
- ✅ HTML reporting
- ✅ Auto-screenshots on failure
- ✅ Comprehensive documentation

**Takeaway:**
- Start simple, improve iteratively
- Document as you go
- Prioritize maintainability
- Use industry-standard tools

---

## 10. 📚 Additional Resources

### Documentation Files:
1. **CLAUDE.md** (This file) - Testing standards and guidelines
2. **SETUP_GUIDE.md** - Installation, setup, troubleshooting
3. **STRUCTURE_ANALYSIS_AND_IMPROVEMENTS.md** - Framework analysis
4. **IMPLEMENTATION_STATUS.md** - Current status and roadmap
5. **FOLDER_STRUCTURE_VERIFIED.md** - Structure verification report

### Configuration Files:
- **requirements.txt** - Python dependencies
- **pytest.ini** - Pytest configuration
- **conftest.py** - Pytest fixtures and hooks
- **.env.example** - Environment variables template
- **config/config.ini** - Multi-environment configuration

### External Resources:
- [Playwright Python Docs](https://playwright.dev/python/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Python Dotenv Guide](https://pypi.org/project/python-dotenv/)
- [Pytest Fixtures Guide](https://docs.pytest.org/en/stable/fixture.html)

---

## 11. 🚀 Quick Start Guide

**For New Team Members:**

```bash
# 1. Clone repo and navigate
cd Chic-AI/AutomationTests/python_tests

# 2. Setup environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
playwright install chromium

# 3. Configure
cp .env.example .env
# Edit .env with credentials

# 4. Run tests
pytest -v

# 5. View results
start results/report.html  # Windows
open results/report.html   # Mac
```

**See SETUP_GUIDE.md for detailed instructions.**

---

## 12. 📞 Contact & Support

**QA Lead:** Bilal
**Framework:** Python + Playwright + Pytest (v2.0)
**Framework Status:** 70% Production-Ready (see IMPLEMENTATION_STATUS.md)
**Documentation:** See section 10 for all docs

### Getting Help:
1. Check **SETUP_GUIDE.md** for installation issues
2. Check **STRUCTURE_ANALYSIS_AND_IMPROVEMENTS.md** for framework questions
3. Check **IMPLEMENTATION_STATUS.md** for current status
4. Review pytest fixtures in **conftest.py**
5. Contact QA Lead Bilal

---

## 🎯 Framework Version History

**v2.0 (February 12, 2026) - Production Foundation:**
- ✅ Added requirements.txt
- ✅ Added .gitignore
- ✅ Added pytest.ini and conftest.py
- ✅ Added configuration management (.env, config.ini)
- ✅ Added comprehensive documentation
- ✅ 100% test pass rate achieved
- ✅ Evidence-based validation established
- ✅ 70% production-ready

**v1.0 (February 11, 2026) - Initial:**
- Basic test scripts
- Manual execution
- 50 test cases created

---

**Remember:** This file serves as the single source of truth for test automation standards in this project. Follow these guidelines in every session to maintain consistency and quality.

**Framework Philosophy:**
1. **Evidence First** - Always review screenshots/videos
2. **Configuration Over Hardcoding** - Use .env and config.ini
3. **Fixtures Over Boilerplate** - Use pytest fixtures
4. **Documentation Always** - Document as you code
5. **Security First** - Never commit sensitive data
6. **Quality Over Quantity** - Better to have 10 good tests than 100 flaky ones
