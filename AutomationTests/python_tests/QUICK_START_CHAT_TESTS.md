# Quick Start - Chat Tests on Production

**Date:** February 12, 2026
**Environment:** https://app.digitalstylist.com/chat
**Status:** ✅ READY TO RUN

---

## ⚡ **30-Second Quick Start**

```bash
# 1. Navigate to test directory
cd C:\Users\usman.GADGET\Downloads\Chic-AI\AutomationTests\python_tests

# 2. Run first test
pytest testcases/TC_CHAT_001/test_script.py -v -s
```

**That's it!** The test will:
- Open browser (Chromium)
- Navigate to production chat
- Verify redirect to login
- Take screenshots
- Show PASS/FAIL

---

## 📋 **What You Have**

✅ **20 Test Scripts** - Ready to run
✅ **Chat Page Object** - 85+ methods
✅ **Test Data** - Comprehensive messages
✅ **.env Configured** - Production settings
✅ **Documentation** - Complete guides

---

## 🎯 **Recommended Test Sequence**

### **Test 1: Authentication (30 sec)**
```bash
pytest testcases/TC_CHAT_001/test_script.py -v -s
```
**Tests:** Unauthenticated access redirects to login
**Creates account:** No
**Duration:** ~30 seconds

---

### **Test 2: Access with Auth (90 sec)**
```bash
pytest testcases/TC_CHAT_002/test_script.py -v -s
```
**Tests:** Authenticated users can access chat
**Creates account:** Yes (auto-generated)
**Duration:** ~90 seconds
**Email:** chat_test_TIMESTAMP_RANDOM@test.com
**Password:** ChatTest@2026

---

### **Test 3: Chat Input Visible (90 sec)**
```bash
pytest testcases/TC_CHAT_013/test_script.py -v -s
```
**Tests:** Chat input field is visible
**Creates account:** Yes
**Duration:** ~90 seconds

---

## 📁 **All Available Tests**

### **Authentication (3 tests)**
```bash
# TC_CHAT_001: Access without auth
pytest testcases/TC_CHAT_001/test_script.py -v -s

# TC_CHAT_002: Access with auth
pytest testcases/TC_CHAT_002/test_script.py -v -s

# TC_CHAT_003: Verify URL
pytest testcases/TC_CHAT_003/test_script.py -v -s
```

### **UI Elements (10 tests)**
```bash
# Run all UI tests
pytest testcases/TC_CHAT_01*/test_script.py -v

# Or individually:
pytest testcases/TC_CHAT_011/test_script.py -v  # Sidebar
pytest testcases/TC_CHAT_012/test_script.py -v  # New Conversation
pytest testcases/TC_CHAT_013/test_script.py -v  # Chat Input
pytest testcases/TC_CHAT_014/test_script.py -v  # Header
pytest testcases/TC_CHAT_015/test_script.py -v  # Upload Outfit
# ... etc
```

### **Welcome Tour (7 tests)**
```bash
# Run all tour tests
pytest testcases/TC_CHAT_02*/test_script.py -v

# Or individually:
pytest testcases/TC_CHAT_021/test_script.py -v  # Tour appears
pytest testcases/TC_CHAT_023/test_script.py -v  # Navigate tour
pytest testcases/TC_CHAT_025/test_script.py -v  # Close tour
# ... etc
```

### **Run ALL Tests**
```bash
# All 20 tests (takes ~40 minutes)
pytest testcases/TC_CHAT_*/test_script.py -v

# With HTML report
pytest testcases/TC_CHAT_*/test_script.py --html=results/chat_report.html
```

---

## 🔧 **Configuration Settings**

Your `.env` file is configured with:

```bash
# Environment
ENVIRONMENT=production
BASE_URL=https://app.digitalstylist.com

# Browser
HEADLESS=false          # Browser visible
BROWSER=chromium        # Chrome browser
SLOW_MO=1000           # 1 second delay between actions

# Features
SKIP_WELCOME_TOUR=true              # Auto-skip tour
AUTO_COMPLETE_ONBOARDING=true       # Auto-complete onboarding
SCREENSHOT_ON_FAILURE=true          # Capture on fail
SCREENSHOT_ON_PASS=true             # Capture on pass
```

**To change settings:** Edit `.env` file

---

## 📊 **Understanding Test Output**

When you run a test, you'll see:

```
================================================================================
TEST: TC_CHAT_001 - Access chat without authentication
================================================================================

[STEP 1] Navigating to chat without authentication...
[INFO] Current URL: https://app.digitalstylist.com/login

[VALIDATION] Checking redirect to login...
[SCREENSHOT] Screenshot saved: results/TC_CHAT_001_PASSED.png

[PASS] Test passed: Unauthenticated access redirected to login

================================================================================
TEST TC_CHAT_001 COMPLETE
================================================================================
```

**Screenshots saved in:** `results/TC_CHAT_001_*.png`

---

## 🎓 **What Tests Do**

### **Tests WITHOUT Account Creation (Fast - 30 sec):**
- TC_CHAT_001 ← Start here!

### **Tests WITH Account Creation (Slower - 90 sec):**
- All others (TC_CHAT_002 onwards)

**Each test with account creation:**
1. Opens browser
2. Navigates to app.digitalstylist.com
3. Creates new account (unique email)
4. Completes signup form
5. Completes 5-step onboarding
6. Skips 7-step welcome tour
7. Accesses chat page
8. Tests specific feature
9. Takes screenshots
10. Shows PASS/FAIL

---

## 💡 **Tips**

### **Run Tests Faster:**
Edit `.env`:
```bash
HEADLESS=true       # No browser window
SLOW_MO=0          # No delays
```

### **Debug Test Failures:**
Edit `.env`:
```bash
HEADLESS=false     # See browser
SLOW_MO=2000       # Slow down actions
LOG_LEVEL=DEBUG    # Verbose logging
```

### **Avoid Rate Limiting:**
```bash
# Don't run all tests at once on production
# Run in small batches (5-10 tests)
# Wait 5-10 minutes between batches
```

---

## 📂 **Where Results Are Saved**

```
results/
├── TC_CHAT_001_PASSED.png         # Test screenshots
├── TC_CHAT_001_navigation.png
├── chat_report.html               # HTML report (if generated)
├── logs/
│   └── chat_tests.log            # Test logs
└── Passed/                        # Organized results (manual)
    └── TC_CHAT_001/
```

---

## ⚠️ **Important Notes**

### **Production Testing:**
- ✅ Tests create REAL accounts on production
- ✅ Each run = 1+ new accounts in database
- ⚠️ Don't spam the production server
- ⚠️ Space out test runs

### **Account Format:**
- **Email:** chat_test_1770906578_5744@test.com (unique)
- **Password:** ChatTest@2026 (same for all)
- **Name:** Chat Test User

### **Test Duration:**
- **Single test:** 30-90 seconds
- **All 20 tests:** ~40 minutes
- **With auth:** +60 seconds per test

---

## 🚀 **Start Testing Now!**

### **Recommended First Steps:**

#### **Step 1: Quick Test**
```bash
cd AutomationTests/python_tests
pytest testcases/TC_CHAT_001/test_script.py -v -s
```
**Time:** 30 seconds
**Creates account:** No
**Result:** Should PASS ✅

#### **Step 2: Full Flow Test**
```bash
pytest testcases/TC_CHAT_002/test_script.py -v -s
```
**Time:** 90 seconds
**Creates account:** Yes
**Result:** Should PASS ✅ (creates account, accesses chat)

#### **Step 3: Run Multiple Tests**
```bash
# Run first 5 tests
pytest testcases/TC_CHAT_001/test_script.py testcases/TC_CHAT_002/test_script.py testcases/TC_CHAT_003/test_script.py -v
```

#### **Step 4: Generate Report**
```bash
# Run all tests with report
pytest testcases/TC_CHAT_*/test_script.py --html=results/chat_report.html --self-contained-html
```

---

## 🎯 **Next Steps After First Test**

Once your first test passes:

1. **✅ Run more tests** - Try TC_CHAT_002, TC_CHAT_013
2. **📊 Generate reports** - Create HTML reports
3. **📁 Organize results** - Move to Passed/Failed folders
4. **🔄 Create more tests** - Messaging, AI responses (ask me!)
5. **⚙️ CI/CD integration** - Automate test runs

---

## ❓ **Troubleshooting**

### **Test fails with "Connection Error":**
- Check internet connection
- Verify app.digitalstylist.com is accessible
- Check if production app is down

### **Test fails with "Timeout":**
- Increase timeout in .env: `DEFAULT_TIMEOUT=60000`
- Check network speed
- Try with `SLOW_MO=0` for faster execution

### **Browser doesn't open:**
- Make sure `HEADLESS=false` in .env
- Check Playwright is installed: `playwright install chromium`

### **Import errors:**
- Activate virtual environment
- Run: `pip install -r requirements.txt`

---

## 📞 **Need Help?**

**Documentation:**
- CHAT_TESTS_READY.md - Complete guide
- CHAT_PAGE_ANALYSIS.md - Analysis
- CHAT_TEST_CASES_PLAN.md - Full test plan (100 tests)

**Key Files:**
- `.env` - Configuration
- `pages/chat_page.py` - Chat page object
- `test_data/chat_test_data.json` - Test data

---

## ✅ **YOU'RE READY!**

Everything is configured and ready to go.

**Run your first test now:**
```bash
cd C:\Users\usman.GADGET\Downloads\Chic-AI\AutomationTests\python_tests
pytest testcases/TC_CHAT_001/test_script.py -v -s
```

**Good luck! 🚀**

---

**Created:** February 12, 2026
**Framework:** Python + Playwright + Pytest
**Environment:** Production (app.digitalstylist.com)
