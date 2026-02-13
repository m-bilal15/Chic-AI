# CHIC Sign Up Page - Test Cases Analysis

**Document Created:** February 12, 2026
**Total Test Cases:** 60
**Source:** CHIC_SignUp_Page_Test_Cases.xlsx
**QA Lead:** Bilal

---

## 📊 Test Case Breakdown

### By Priority:
- **Critical:** 13 test cases (22%)
- **High:** 22 test cases (37%)
- **Medium:** 16 test cases (27%)
- **Low:** 9 test cases (15%)

### By Type:
- **Positive:** 14 test cases (23%) - Valid scenarios that should succeed
- **Negative:** 19 test cases (32%) - Invalid data/validation testing
- **UI/UX:** 16 test cases (27%) - Interface and user experience
- **Security:** 10 test cases (17%) - Security vulnerability testing
- **Performance:** 1 test case (2%) - Load time testing

---

## 📋 Test Case Categories

### 1. **Page Load & UI Elements (TC_SIGNUP_001)**
- Verify Sign Up page loads successfully
- Check all UI elements present (logo, heading, form fields, buttons)

### 2. **Positive Test Scenarios (TC_SIGNUP_002 to TC_SIGNUP_012)**
- Valid account creation with all correct data
- Full Name field accepts valid names
- Full Name with special characters (O'Brien, Jean-Pierre, María, Müller)
- Email field accepts valid formats
- Password field masks input
- Password visibility toggle (eye icon)
- Confirm Password visibility toggle
- Google Sign Up integration
- Navigation to Login page via "Sign in here" link
- Keyboard navigation (Tab + Enter)
- Password with exactly 8 characters (minimum boundary)

### 3. **Negative Test Scenarios - Empty Fields (TC_SIGNUP_013 to TC_SIGNUP_017)**
- All fields empty
- Empty Full Name only
- Empty Email only
- Empty Password only
- Empty Confirm Password only

### 4. **Negative Test Scenarios - Password Validation (TC_SIGNUP_018 to TC_SIGNUP_020)**
- Mismatched passwords
- Password less than 8 characters
- Password with exactly 7 characters (boundary -1)

### 5. **Negative Test Scenarios - Invalid Data (TC_SIGNUP_021 to TC_SIGNUP_030)**
- Invalid email formats (plaintext, user@, @domain, etc.)
- Already registered email (duplicate account)
- Only spaces in Full Name
- Numeric-only Full Name
- Special characters in Full Name (!@#$%)
- Extremely long Full Name (255+ chars)
- Extremely long Email (255+ chars)
- Password with only spaces
- Weak password (no special chars/numbers)
- Confirm Password case sensitivity

### 6. **Security Test Scenarios (TC_SIGNUP_031 to TC_SIGNUP_040)**
- **SQL Injection:** Full Name, Email fields
- **XSS (Cross-Site Scripting):** Full Name, Email, Password fields
- **HTTPS:** Password transmission security
- **HTML Injection:** Full Name field
- **Rate Limiting:** Multiple rapid submissions
- **Sensitive Data:** No secrets in page source
- **CAPTCHA:** Bot protection verification

### 7. **UI/UX Test Scenarios (TC_SIGNUP_041 to TC_SIGNUP_056)**
- Form field placeholders
- Field focus states and visual feedback
- Error message styling and placement
- Button states (default, hover, disabled, loading)
- Responsive design (mobile, tablet, desktop)
- Form field labels
- Accessibility (ARIA, keyboard navigation, screen readers)
- Auto-focus on first field
- Copy/paste in password fields
- Browser autofill compatibility
- Error message appearance/animations
- Field character limits
- Loading spinner during submission

### 8. **Performance Test (TC_SIGNUP_060)**
- Page load time under 3 seconds

---

## 🎯 Implementation Priority

### **Phase 1: Critical Test Cases (13 tests)**
High-priority tests that cover core functionality:
1. TC_SIGNUP_001 - Page loads successfully
2. TC_SIGNUP_002 - Successful account creation
3. TC_SIGNUP_013 - All fields empty validation
4. TC_SIGNUP_018 - Mismatched passwords
5. TC_SIGNUP_019 - Password less than 8 chars
6. TC_SIGNUP_022 - Already registered email
7. TC_SIGNUP_031 - SQL injection (Full Name)
8. TC_SIGNUP_032 - SQL injection (Email)
9. TC_SIGNUP_033 - XSS (Full Name)
10. TC_SIGNUP_034 - XSS (Email)
11. TC_SIGNUP_035 - XSS (Password)
12. TC_SIGNUP_036 - HTTPS password transmission
13. TC_SIGNUP_009 - Google Sign Up

### **Phase 2: High Priority Tests (22 tests)**
Important validation and functionality tests:
- TC_SIGNUP_003 to TC_SIGNUP_008 - Input field validations
- TC_SIGNUP_010 to TC_SIGNUP_012 - Navigation and boundary tests
- TC_SIGNUP_014 to TC_SIGNUP_017 - Individual empty field validations
- TC_SIGNUP_020 to TC_SIGNUP_021 - Boundary and format tests
- TC_SIGNUP_028 to TC_SIGNUP_030 - Password edge cases
- TC_SIGNUP_037 to TC_SIGNUP_038 - Additional security tests

### **Phase 3: Medium Priority Tests (16 tests)**
Edge cases and additional validation:
- TC_SIGNUP_004 - Names with special characters
- TC_SIGNUP_011 - Keyboard navigation
- TC_SIGNUP_023 to TC_SIGNUP_027 - Input edge cases
- TC_SIGNUP_041 to TC_SIGNUP_050 - UI/UX tests (partial)

### **Phase 4: Low Priority Tests (9 tests)**
Nice-to-have tests and refinements:
- Remaining UI/UX tests
- Accessibility tests
- Performance tests
- Additional edge cases

---

## 🏗️ Implementation Approach

### Following CLAUDE.md Guidelines:

1. **File Structure:**
   ```
   testcases/
   ├── TC_SIGNUP_001/
   │   └── test_script.py
   ├── TC_SIGNUP_002/
   │   └── test_script.py
   └── ... (60 total)
   ```

2. **Page Object Model:**
   ```
   pages/
   └── signup_page.py  (NEW - needs to be created)
   ```

3. **Test Data:**
   ```
   test_data/
   ├── valid_signup_data.json  (NEW)
   └── invalid_signup_data.json  (NEW)
   ```

4. **Configuration:**
   - Update `.env` with signup page URL
   - Update `config/selectors.json` with signup page selectors

---

## 🔧 Prerequisites

### Before Starting Implementation:

1. **Identify Signup Page URL:**
   - Is it a separate page or same as login with toggle?
   - Current assumption: https://app.digitalstylist.com/login (with sign up view)

2. **Identify Signup Form Selectors:**
   - Full Name field selector
   - Email field selector
   - Password field selector
   - Confirm Password field selector
   - Create Account button selector
   - Sign up with Google button selector
   - Sign in here link selector
   - Error message selectors

3. **Setup Test Environment:**
   - Ensure signup page is accessible
   - Verify Google OAuth is configured (for TC_SIGNUP_009)
   - Setup test email accounts for duplicate testing

---

## 📝 Next Steps

1. **Explore Signup Page:**
   - Navigate to signup page
   - Identify all selectors
   - Understand validation behavior
   - Document actual vs expected behavior

2. **Create Page Object:**
   - Create `pages/signup_page.py`
   - Add all signup methods (fill_name, fill_email, click_signup, etc.)

3. **Create Test Data Files:**
   - `test_data/valid_signup_data.json`
   - `test_data/invalid_signup_data.json`

4. **Update Selectors:**
   - Add signup selectors to `config/selectors.json`

5. **Implement Tests:**
   - Start with Phase 1 (Critical tests)
   - Follow CLAUDE.md guidelines
   - Use modern pytest fixture approach
   - Capture screenshots and videos
   - Follow evidence-based validation

---

## ⚠️ Important Considerations

### From CLAUDE.md Guidelines:

1. **Evidence-Based Testing:**
   - Always review screenshots/videos before marking pass/fail
   - Native HTML5 validation tooltips are valid validation
   - Don't trust automation blindly

2. **Test Independence:**
   - Each test must be runnable independently
   - No shared state between tests
   - Clean up after each test

3. **Configuration:**
   - No hardcoded URLs or credentials
   - Use .env and config.ini
   - Never commit .env to git

4. **Modern Pytest Approach:**
   - Use pytest fixtures from conftest.py
   - Add markers (@pytest.mark.critical, @pytest.mark.security)
   - Use page objects
   - Auto-screenshots on failure

5. **Security Tests:**
   - Exercise caution with SQL injection tests
   - Ensure XSS tests don't affect production
   - Document security findings properly

---

## 📊 Expected Outcomes

### After Complete Implementation:

- **Total Tests:** 60
- **Test Scripts:** 60 individual Python files
- **Page Objects:** 1 (SignupPage)
- **Test Data Files:** 2 (valid + invalid)
- **Result Folders:** 60 (Passed/Failed per test)
- **Evidence:** 60+ screenshots, 60+ videos
- **Reports:** SUMMARY.md, SUMMARY.json, TEST_REPORT.md/BUG_REPORT.md

### Success Criteria:

- ✅ All 60 test cases implemented
- ✅ All tests follow CLAUDE.md guidelines
- ✅ Evidence captured for every test
- ✅ Comprehensive bug reports for failures
- ✅ 100% test execution rate
- ✅ High pass rate (target: 85%+)
- ✅ Security vulnerabilities documented
- ✅ UI/UX issues identified

---

**Status:** Ready for implementation
**Next Action:** Explore signup page and create page object model
**Estimated Effort:** 60 test cases × ~30 min avg = ~30 hours total work
