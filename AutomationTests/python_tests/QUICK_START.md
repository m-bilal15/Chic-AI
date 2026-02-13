# 🚀 QUICK START - Run Critical Signup Tests

**All 13 critical tests are ready to run!**

---

## ⚡ Quick Commands

### 1. Activate Virtual Environment
```bash
cd "C:\Users\usman.GADGET\Downloads\Chic-AI\AutomationTests\python_tests"
venv\Scripts\activate
```

### 2. Run All Critical Tests
```bash
pytest -m critical -v -s
```

### 3. Run with HTML Report
```bash
pytest -m critical -v -s --html=results/critical_report.html
```

---

## 📋 Individual Test Commands

```bash
# Test 1: Page Load
pytest testcases/TC_SIGNUP_001/test_script.py -v -s

# Test 2: Valid Signup
pytest testcases/TC_SIGNUP_002/test_script.py -v -s

# Test 3: Empty Fields Validation
pytest testcases/TC_SIGNUP_013/test_script.py -v -s

# Test 4: Password Mismatch
pytest testcases/TC_SIGNUP_018/test_script.py -v -s

# Test 5: Password Too Short
pytest testcases/TC_SIGNUP_019/test_script.py -v -s

# Test 6: Duplicate Email
pytest testcases/TC_SIGNUP_022/test_script.py -v -s

# Test 7: Google Signup
pytest testcases/TC_SIGNUP_009/test_script.py -v -s

# Tests 8-13: Security Tests (SQL Injection & XSS)
pytest -m security -v -s
```

---

## 🎯 Run by Category

```bash
# Validation tests only
pytest -m validation -v -s

# Security tests only
pytest -m security -v -s

# Smoke tests
pytest -m smoke -v -s
```

---

## 📸 Check Results

After running tests, check:
- **Screenshots:** `results/TC_SIGNUP_XXX_PASSED.png`
- **HTML Report:** `results/critical_report.html`
- **Failure Screenshots:** `results/failures/`
- **Videos:** `results/videos/`

---

## ✅ What's Included

**13 Critical Tests:**
- ✅ TC_SIGNUP_001 - Page Load
- ✅ TC_SIGNUP_002 - Valid Signup
- ✅ TC_SIGNUP_009 - Google OAuth
- ✅ TC_SIGNUP_013 - Empty Fields
- ✅ TC_SIGNUP_018 - Password Mismatch
- ✅ TC_SIGNUP_019 - Short Password
- ✅ TC_SIGNUP_022 - Duplicate Email
- ✅ TC_SIGNUP_031 - SQL Injection (Name)
- ✅ TC_SIGNUP_032 - SQL Injection (Email)
- ✅ TC_SIGNUP_033 - XSS (Name)
- ✅ TC_SIGNUP_034 - XSS (Email)
- ✅ TC_SIGNUP_035 - XSS (Password)
- ✅ TC_SIGNUP_036 - HTTPS Security

---

## ⚠️ Before Running

1. Make sure app is running on: `http://localhost:5173`
2. Virtual environment is activated
3. If selectors fail, update `pages/signup_page.py`

---

**Ready to test!** 🎉
