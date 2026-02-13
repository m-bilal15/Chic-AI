# AI Chat Model Validation Report

**Date:** 2026-02-13 17:50:39
**Account:** tim@gmail.com
**Pass Rate:** 0/8 (0.0%)

---

## Test Scenarios

### AI_VAL_001: Event Styling

**User Query:** "What should I wear to a wedding?"

**Overall Result:** FAIL

**Response Time:** 20.1s

**AI Response:**
> ...

**Validation Checks:**

- ❌ **Response Time:** FAIL
  - Expected: < 15 seconds
  - Actual: 20.1s
- ❌ **Must Contain Keywords:** FAIL
  - Expected: ['wedding', 'dress', 'outfit', 'formal', 'elegant']
  - Actual: Missing: ['wedding', 'dress', 'outfit', 'formal', 'elegant']
- ℹ️ **Should Contain Keywords:** INFO
  - Expected: ['color', 'style', 'accessories']
  - Actual: None found
- ✅ **Must NOT Contain:** PASS
  - Expected: Avoid: ['casual', 'gym', 'workout']
  - Actual: Clean
- ❌ **Response Length:** FAIL
  - Expected: > 50 chars
  - Actual: 0 chars

**Checks Passed:** 1/4

---

### AI_VAL_002: Professional Styling

**User Query:** "I have a job interview tomorrow. What should I wear?"

**Overall Result:** FAIL

**Response Time:** 20.1s

**AI Response:**
> ...

**Validation Checks:**

- ❌ **Response Time:** FAIL
  - Expected: < 15 seconds
  - Actual: 20.1s
- ❌ **Must Contain Keywords:** FAIL
  - Expected: ['interview', 'professional', 'business', 'outfit']
  - Actual: Missing: ['interview', 'professional', 'business', 'outfit']
- ℹ️ **Should Contain Keywords:** INFO
  - Expected: ['confidence', 'appropriate', 'polished']
  - Actual: None found
- ✅ **Must NOT Contain:** PASS
  - Expected: Avoid: ['casual', 'party', 'beach']
  - Actual: Clean
- ❌ **Response Length:** FAIL
  - Expected: > 50 chars
  - Actual: 0 chars

**Checks Passed:** 1/4

---

### AI_VAL_003: Color Advice - Personalization

**User Query:** "What colors look good on me?"

**Overall Result:** FAIL

**Response Time:** 20.1s

**AI Response:**
> ...

**Validation Checks:**

- ❌ **Response Time:** FAIL
  - Expected: < 15 seconds
  - Actual: 20.1s
- ❌ **Must Contain Keywords:** FAIL
  - Expected: ['color', 'colors']
  - Actual: Missing: ['color', 'colors']
- ℹ️ **Should Contain Keywords:** INFO
  - Expected: ['body type', 'skin tone', 'preference']
  - Actual: None found
- ❌ **Response Length:** FAIL
  - Expected: > 50 chars
  - Actual: 0 chars

**Checks Passed:** 0/3

---

### AI_VAL_004: Body Type Styling - Personalization

**User Query:** "What styles suit my body type?"

**Overall Result:** FAIL

**Response Time:** 20.2s

**AI Response:**
> ...

**Validation Checks:**

- ❌ **Response Time:** FAIL
  - Expected: < 15 seconds
  - Actual: 20.2s
- ❌ **Must Contain Keywords:** FAIL
  - Expected: ['body type', 'style', 'suit']
  - Actual: Missing: ['body type', 'style', 'suit']
- ❌ **Response Length:** FAIL
  - Expected: > 50 chars
  - Actual: 0 chars

**Checks Passed:** 0/3

---

### AI_VAL_005: Product Shopping

**User Query:** "Show me some dress options for summer"

**Overall Result:** FAIL

**Response Time:** 20.1s

**AI Response:**
> ...

**Validation Checks:**

- ❌ **Response Time:** FAIL
  - Expected: < 15 seconds
  - Actual: 20.1s
- ❌ **Must Contain Keywords:** FAIL
  - Expected: ['dress', 'summer']
  - Actual: Missing: ['dress', 'summer']
- ℹ️ **Should Contain Keywords:** INFO
  - Expected: ['options', 'recommendations', 'styles']
  - Actual: None found
- ❌ **Response Length:** FAIL
  - Expected: > 50 chars
  - Actual: 0 chars

**Checks Passed:** 0/3

---

### AI_VAL_006: Conversation Context

**User Query:** "["I'm attending a wedding", 'I prefer modest styles']"

**Overall Result:** FAIL

**Response Time:** 20.1s

**AI Response:**
> ...

**Validation Checks:**

- ❌ **Response Time:** FAIL
  - Expected: < 15 seconds each
  - Actual: 20.1s
- ❌ **Response Length:** FAIL
  - Expected: > 50 chars
  - Actual: 0 chars

**Checks Passed:** 0/2

---

### AI_VAL_007: Wardrobe Building

**User Query:** "What are essential pieces every wardrobe should have?"

**Overall Result:** FAIL

**Response Time:** 20.1s

**AI Response:**
> ...

**Validation Checks:**

- ❌ **Response Time:** FAIL
  - Expected: < 15 seconds
  - Actual: 20.1s
- ❌ **Must Contain Keywords:** FAIL
  - Expected: ['essential', 'wardrobe', 'pieces']
  - Actual: Missing: ['essential', 'wardrobe', 'pieces']
- ℹ️ **Should Contain Keywords:** INFO
  - Expected: ['basics', 'versatile', 'must-have']
  - Actual: None found
- ❌ **Response Length:** FAIL
  - Expected: > 50 chars
  - Actual: 0 chars

**Checks Passed:** 0/3

---

### AI_VAL_008: Style Problem Solving

**User Query:** "I always wear black. How can I add more color to my wardrobe?"

**Overall Result:** FAIL

**Response Time:** 20.1s

**AI Response:**
> ...

**Validation Checks:**

- ❌ **Response Time:** FAIL
  - Expected: < 15 seconds
  - Actual: 20.1s
- ❌ **Must Contain Keywords:** FAIL
  - Expected: ['color', 'wardrobe']
  - Actual: Missing: ['color', 'wardrobe']
- ℹ️ **Should Contain Keywords:** INFO
  - Expected: ['gradually', 'start', 'options', 'comfortable']
  - Actual: None found
- ❌ **Response Length:** FAIL
  - Expected: > 50 chars
  - Actual: 0 chars

**Checks Passed:** 0/3

---

