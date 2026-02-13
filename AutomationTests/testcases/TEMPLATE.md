# Test Case Template

Use this template to create your test cases. Copy and fill in the details.

---

## Test Case: [TC-ID] - [Test Name]

**Module:** [e.g., Authentication, Products, Profile]
**Priority:** [High / Medium / Low]
**Type:** [Functional / UI / API / Integration]
**Status:** [New / In Progress / Automated / Failed]

---

### Pre-conditions:
- [List any setup required before test execution]
- [e.g., User must be registered]
- [e.g., Application must be running]

---

### Test Data:
| Field | Value |
|-------|-------|
| Email | test@example.com |
| Password | Test@123456 |
| [Add more as needed] | |

---

### Test Steps:

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to [page] | [Page loads successfully] |
| 2 | Enter [data] in [field] | [Data is entered correctly] |
| 3 | Click [button] | [Action is performed] |
| 4 | Verify [element] | [Element is visible/contains text] |

---

### Expected Results:
- [ ] [Primary expected outcome]
- [ ] [Secondary expected outcome]
- [ ] [Any UI changes expected]
- [ ] [Any API responses expected]

---

### Post-conditions:
- [State of system after test]
- [Any cleanup required]

---

### Notes:
- [Any additional information]
- [Known issues]
- [Dependencies on other tests]

---

## Example Usage:

---

## Test Case: TC001 - Verify User Login with Valid Credentials

**Module:** Authentication
**Priority:** High
**Type:** Functional
**Status:** New

---

### Pre-conditions:
- User account exists in the system
- User is on the login page
- Browser is open

---

### Test Data:
| Field | Value |
|-------|-------|
| Email | test@example.com |
| Password | Test@123456 |

---

### Test Steps:

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to login page (/) | Login page loads with email and password fields |
| 2 | Enter "test@example.com" in email field | Email is entered correctly |
| 3 | Enter "Test@123456" in password field | Password is masked and entered correctly |
| 4 | Click "Login" button | Login is processed |
| 5 | Wait for redirection | User is redirected to dashboard |
| 6 | Verify welcome message | "Welcome" message is displayed |

---

### Expected Results:
- [x] User successfully logs in
- [x] User is redirected to dashboard page
- [x] Welcome message displays user name
- [x] Navigation menu shows logout option

---

### Post-conditions:
- User session is created
- User remains logged in until logout

---

### Notes:
- This test should run on all browsers (Chrome, Firefox, Safari)
- Mobile responsive testing required
- Test should complete within 10 seconds
