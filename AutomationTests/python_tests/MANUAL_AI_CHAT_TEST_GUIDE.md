# AI Chat Model - Manual Testing Guide

**Application:** CHIC Concierge AI Chat
**Environment:** https://app.digitalstylist.com/chat
**Login:** tim@gmail.com / Qwerty@123
**Date:** February 13, 2026

---

## 📋 **MANUAL TESTING INSTRUCTIONS**

### **Setup:**
1. Open browser (Chrome recommended)
2. Go to: https://app.digitalstylist.com/login
3. Login with: **tim@gmail.com** / **Qwerty@123**
4. Navigate to chat page
5. Complete/skip any welcome tour if appears
6. Start testing!

---

## 🎯 **TEST SCENARIOS - 15 Tests**

### **CATEGORY 1: EVENT-BASED STYLING (5 scenarios)**

---

#### **TEST 1: Wedding Guest Outfit**

**Test ID:** AI_MANUAL_001
**Priority:** Critical
**Category:** Event Styling

**User Query:**
```
"I'm attending a wedding next month. What should I wear?"
```

**Expected AI Response Should Include:**
✅ Acknowledge wedding event
✅ Suggest formal/semi-formal dress options
✅ Mention appropriate colors
✅ Consider user's body type (if known from profile)
✅ Suggest complete outfit (dress + accessories)
✅ May show product recommendations

**Validation Checklist:**
- [ ] AI responded within 15 seconds
- [ ] Response mentions "wedding" or "formal event"
- [ ] Suggests dresses or formal attire
- [ ] Provides specific outfit suggestions
- [ ] Response is helpful and actionable
- [ ] Appropriate tone (professional, helpful)

**Keywords to Look For:**
- Must have: wedding, dress, outfit, formal
- Good to have: elegant, color, accessories, style
- Must NOT have: casual, gym, workout, beach

**Pass Criteria:** At least 4/6 validation points checked

**Your Observations:**
```
AI Response Time: ___ seconds
AI Response:
[Write the actual AI response here]

Keywords Found: ________________
Overall Assessment: PASS / FAIL
Notes: ___________________________
```

---

#### **TEST 2: Job Interview Outfit**

**Test ID:** AI_MANUAL_002
**Priority:** Critical
**Category:** Professional Styling

**User Query:**
```
"I have a job interview tomorrow. What should I wear?"
```

**Expected AI Response Should Include:**
✅ Acknowledge interview importance
✅ Suggest professional/business attire
✅ Mention confidence-building
✅ Provide specific clothing items
✅ Appropriate colors (conservative or power colors)
✅ May mention grooming/presentation tips

**Validation Checklist:**
- [ ] AI responded within 15 seconds
- [ ] Response mentions "interview" or "professional"
- [ ] Suggests business appropriate attire
- [ ] Provides confidence/encouragement
- [ ] Specific actionable advice
- [ ] Professional and supportive tone

**Keywords to Look For:**
- Must have: interview, professional, business, outfit
- Good to have: confidence, appropriate, polished, suit/blazer
- Must NOT have: casual, party, revealing

**Pass Criteria:** At least 4/6 validation points checked

**Your Observations:**
```
AI Response Time: ___ seconds
AI Response:
[Write actual response]

Assessment: PASS / FAIL
```

---

#### **TEST 3: Date Night Outfit**

**Test ID:** AI_MANUAL_003
**Priority:** High
**Category:** Event Styling

**User Query:**
```
"I'm going on a date tonight. Help me choose what to wear!"
```

**Expected AI Response Should Include:**
✅ Acknowledge date context
✅ Suggest stylish yet comfortable options
✅ Confidence-boosting advice
✅ Balance between impressive and authentic
✅ Multiple options or style directions
✅ Accessories or finishing touches

**Validation Checklist:**
- [ ] Response time < 15 seconds
- [ ] Mentions "date" or understands context
- [ ] Suggests appropriate date attire
- [ ] Encouraging and confidence-building
- [ ] Specific outfit suggestions
- [ ] Helpful tone

**Pass Criteria:** 4/6 checks

---

#### **TEST 4: Cocktail Party**

**Test ID:** AI_MANUAL_004
**Priority:** Medium
**Category:** Event Styling

**User Query:**
```
"What should I wear to a cocktail party this weekend?"
```

**Expected:**
✅ Semi-formal dress suggestions
✅ Cocktail attire appropriate recommendations
✅ Mention of elegant/sophisticated style
✅ Accessories (heels, clutch, jewelry)

**Validation:**
- [ ] Understands cocktail party context
- [ ] Suggests semi-formal attire
- [ ] Specific recommendations
- [ ] Helpful and appropriate

---

#### **TEST 5: Casual Brunch**

**Test ID:** AI_MANUAL_005
**Priority:** Medium
**Category:** Event Styling

**User Query:**
```
"I'm meeting friends for brunch. Outfit ideas?"
```

**Expected:**
✅ Casual yet put-together suggestions
✅ Comfortable but stylish options
✅ Relaxed tone
✅ Easy outfit combinations

**Validation:**
- [ ] Understands casual context
- [ ] Appropriate level of formality
- [ ] Practical suggestions
- [ ] Friendly tone

---

### **CATEGORY 2: PERSONALIZATION TESTING (5 scenarios)**

---

#### **TEST 6: Color Recommendations - PERSONALIZATION**

**Test ID:** AI_MANUAL_006
**Priority:** CRITICAL (Personalization Test)
**Category:** Personal Color Advice

**User Query:**
```
"What colors would look best on me?"
```

**CRITICAL REQUIREMENT:**
✅ **MUST reference user's favorite colors from profile**
✅ **MUST be personalized** (not generic advice)

**Expected AI Response Should:**
✅ Mention specific colors
✅ Reference user's preferences (if in profile)
✅ Explain why certain colors work
✅ Suggest color combinations
✅ Be specific to the user, not generic

**Validation Checklist:**
- [ ] Response time < 15 seconds
- [ ] Mentions specific colors
- [ ] References user's profile/preferences ⭐ CRITICAL
- [ ] Explains reasoning
- [ ] Provides actionable color advice
- [ ] Personalized (not generic)

**What to Check:**
- Does AI say "Based on your preferences..." or similar?
- Does AI mention colors you selected in onboarding?
- Is response personalized or generic?

**Pass Criteria:** MUST be personalized (5/6 checks)

---

#### **TEST 7: Body Type Styling - PERSONALIZATION**

**Test ID:** AI_MANUAL_007
**Priority:** CRITICAL (Personalization Test)
**Category:** Body Type Advice

**User Query:**
```
"What styles suit my body type?"
```

**CRITICAL REQUIREMENT:**
✅ **MUST mention user's specific body type**
✅ **MUST provide body-type specific advice**

**Expected AI Response Should:**
✅ Identify user's body type (from profile)
✅ Provide body-type specific styling advice
✅ Mention what to emphasize (highlight areas)
✅ Mention what to avoid or minimize
✅ Suggest specific silhouettes/styles
✅ Explain why certain styles flatter

**Validation Checklist:**
- [ ] Response time < 15 seconds
- [ ] Mentions user's body type (Hourglass, Pear, etc.) ⭐ CRITICAL
- [ ] Provides body-specific advice
- [ ] References highlight/minimize areas
- [ ] Specific style recommendations
- [ ] Personalized and detailed

**What to Check:**
- Does AI say "For your [body type]..." ?
- Does AI reference areas to highlight?
- Is advice specific to body type or generic?

**Pass Criteria:** MUST mention body type (5/6 checks)

---

#### **TEST 8: Highlight Features**

**Test ID:** AI_MANUAL_008
**Priority:** High (Personalization)
**Category:** Feature Enhancement

**User Query:**
```
"How can I accentuate my best features?"
```

**Expected:**
✅ Reference user's highlight areas from profile
✅ Specific styling tips for those areas
✅ Clothing cuts/styles that emphasize

---

#### **TEST 9: What to Avoid**

**Test ID:** AI_MANUAL_009
**Priority:** High (Personalization)
**Category:** Minimize Areas

**User Query:**
```
"What should I avoid wearing?"
```

**Expected:**
✅ Reference user's minimize areas from profile
✅ Gentle, positive framing
✅ Alternative suggestions

---

#### **TEST 10: Overall Style Match**

**Test ID:** AI_MANUAL_010
**Priority:** High (Personalization)
**Category:** Style Personality

**User Query:**
```
"Recommend outfits that match my style"
```

**Expected:**
✅ Reference user's style descriptions (Chic, Elegant, etc.)
✅ Outfit suggestions matching personality
✅ Complete looks that align with preferences

---

### **CATEGORY 3: CONVERSATION QUALITY (3 scenarios)**

---

#### **TEST 11: Multi-Turn Conversation**

**Test ID:** AI_MANUAL_011
**Priority:** Critical
**Category:** Context Awareness

**Conversation Flow:**
```
User: "I need an outfit for a wedding"
[Wait for AI response]

User: "I prefer something more modest"
[Wait for AI response]

User: "What shoes would go with that?"
[Wait for AI response]
```

**Expected AI Behavior:**
✅ First response: Wedding outfit suggestions
✅ Second response: Adjusts to modest styles, remembers wedding
✅ Third response: Suggests shoes matching previous outfit

**Validation:**
- [ ] AI provides wedding outfit first
- [ ] AI adjusts based on "modest" feedback
- [ ] AI remembers previous outfit in shoe suggestion ⭐ CRITICAL
- [ ] Conversation feels natural
- [ ] AI maintains context throughout

**Pass Criteria:** MUST maintain context (4/5 checks)

---

#### **TEST 12: Clarification Handling**

**Test ID:** AI_MANUAL_012
**Priority:** Medium
**Category:** AI Intelligence

**User Query:**
```
"Help me with my style"
```
(Intentionally vague)

**Expected:**
✅ AI asks clarifying questions
✅ "What occasion?" or "What are you looking for?"
✅ Helpful guidance to narrow down need

**Validation:**
- [ ] AI asks questions
- [ ] Helps user clarify needs
- [ ] Doesn't make assumptions

---

#### **TEST 13: Follow-Up Question**

**Test ID:** AI_MANUAL_013
**Priority:** High
**Category:** Context Awareness

**Conversation:**
```
User: "I love the dress you suggested"
```

**Expected:**
✅ AI acknowledges (even without seeing previous suggestion)
✅ May ask which dress or offer more options
✅ Continues conversation naturally

---

### **CATEGORY 4: PRODUCT & SHOPPING (2 scenarios)**

---

#### **TEST 14: Product Recommendations**

**Test ID:** AI_MANUAL_014
**Priority:** High
**Category:** Shopping Assistance

**User Query:**
```
"Show me some dress options for summer"
```

**Expected:**
✅ AI shows/mentions product recommendations
✅ Dresses appropriate for summer
✅ Multiple options
✅ Products visible in UI or described
✅ "Shop Now" buttons or links work

**Validation:**
- [ ] Products shown in UI
- [ ] Products are dresses (not other items)
- [ ] Appropriate for summer
- [ ] Clickable/actionable
- [ ] Matches user's style

---

#### **TEST 15: Budget-Conscious Shopping**

**Test ID:** AI_MANUAL_015
**Priority:** Medium
**Category:** Shopping Assistance

**User Query:**
```
"I have a $100 budget. What can I get?"
```

**Expected:**
✅ AI acknowledges budget
✅ Suggests items within budget
✅ May suggest how to mix pieces
✅ Realistic expectations

---

## 📊 **VALIDATION CRITERIA**

### **For Each Test, Check:**

**1. Response Time:**
- ⭐⭐⭐ Excellent: < 10 seconds
- ⭐⭐ Good: 10-20 seconds
- ⭐ Acceptable: 20-30 seconds
- ❌ Poor: > 30 seconds

**2. Relevance:**
- Does AI understand the question?
- Is response on-topic?
- Contains relevant keywords?

**3. Personalization (for tests 6-10):**
- Does AI use profile data?
- Mentions body type, colors, or style?
- Personalized or generic?

**4. Actionability:**
- Are suggestions specific?
- Can user act on the advice?
- Clear next steps?

**5. Quality:**
- Response is substantial (not too short)?
- Well-structured?
- Helpful and valuable?

**6. Behavior:**
- Appropriate tone?
- Professional yet friendly?
- Encouraging and supportive?

---

## 📝 **TESTING TEMPLATE**

For each test, document:

```
TEST ID: AI_MANUAL_XXX
Date: ___________
Time: ___________

USER QUESTION:
[Your question here]

AI RESPONSE TIME: ___ seconds

AI RESPONSE (Full text):
[Copy/paste or type the complete AI response]

VALIDATION:
[ ] Response Time: ___s (< 15s expected)
[ ] Relevant Keywords Found: __________
[ ] Personalization: YES / NO / N/A
[ ] Actionable Advice: YES / NO
[ ] Response Quality: Excellent / Good / Poor
[ ] Appropriate Behavior: YES / NO

OVERALL RESULT: PASS / FAIL

NOTES:
[Any additional observations]

SCREENSHOT: [File name if captured]
```

---

## 🎯 **TESTING PRIORITIES**

### **MUST TEST (Critical):**
1. ✅ TEST 1: Wedding outfit (event styling)
2. ✅ TEST 2: Job interview (professional styling)
3. ✅ TEST 6: Color advice (personalization) ⭐
4. ✅ TEST 7: Body type styling (personalization) ⭐
5. ✅ TEST 11: Multi-turn conversation (context) ⭐

### **SHOULD TEST (High Priority):**
6. ✅ TEST 3: Date night
7. ✅ TEST 8: Highlight features
8. ✅ TEST 14: Product recommendations

### **NICE TO TEST (Medium Priority):**
9. ✅ TEST 4: Cocktail party
10. ✅ TEST 9: What to avoid
11. ✅ TEST 12: Clarification handling
12. ✅ TEST 15: Budget shopping

### **OPTIONAL (Low Priority):**
13. ✅ TEST 5: Casual brunch
14. ✅ TEST 10: Overall style match
15. ✅ TEST 13: Follow-up question

---

## 📊 **RESULTS TRACKING SHEET**

| Test ID | Scenario | Status | Response Time | Personalized? | Quality | Notes |
|---------|----------|--------|---------------|---------------|---------|-------|
| AI_MANUAL_001 | Wedding outfit | [ ] | ___s | N/A | [ ] | |
| AI_MANUAL_002 | Job interview | [ ] | ___s | N/A | [ ] | |
| AI_MANUAL_003 | Date night | [ ] | ___s | N/A | [ ] | |
| AI_MANUAL_004 | Cocktail party | [ ] | ___s | N/A | [ ] | |
| AI_MANUAL_005 | Casual brunch | [ ] | ___s | N/A | [ ] | |
| AI_MANUAL_006 | Color advice | [ ] | ___s | [ ] | [ ] | **Must be personalized** |
| AI_MANUAL_007 | Body type | [ ] | ___s | [ ] | [ ] | **Must mention body type** |
| AI_MANUAL_008 | Highlight features | [ ] | ___s | [ ] | [ ] | |
| AI_MANUAL_009 | What to avoid | [ ] | ___s | [ ] | [ ] | |
| AI_MANUAL_010 | Style match | [ ] | ___s | [ ] | [ ] | |
| AI_MANUAL_011 | Multi-turn conv | [ ] | ___s | N/A | [ ] | **Must maintain context** |
| AI_MANUAL_012 | Clarification | [ ] | ___s | N/A | [ ] | |
| AI_MANUAL_013 | Follow-up | [ ] | ___s | N/A | [ ] | |
| AI_MANUAL_014 | Products | [ ] | ___s | N/A | [ ] | |
| AI_MANUAL_015 | Budget | [ ] | ___s | N/A | [ ] | |

**Summary:**
- Total Tests: 15
- Passed: ___
- Failed: ___
- Pass Rate: ___%

---

## 🔍 **WHAT TO LOOK FOR**

### **Good AI Response Examples:**

✅ **Personalized:**
> "For your hourglass body type, I recommend A-line dresses that emphasize your waist..."

✅ **Specific:**
> "Try a navy blue midi dress with nude heels and a statement necklace"

✅ **Contextual:**
> "Since it's a wedding, avoid wearing white or anything that might outshine the bride..."

✅ **Actionable:**
> "Here are some options: [shows products] Click to shop these looks"

### **Poor AI Response Examples:**

❌ **Generic:**
> "Wear something nice that makes you feel comfortable"

❌ **Too Vague:**
> "Dresses are good for weddings"

❌ **Not Personalized:**
> "Most people look good in blue" (when user has specific color preferences)

❌ **Not Actionable:**
> "Wear formal clothes" (no specific suggestions)

---

## 💡 **TIPS FOR MANUAL TESTING**

1. **Take Your Time:**
   - Send one question
   - Wait for complete AI response
   - Read and analyze the response
   - Document before moving to next

2. **Screenshot Everything:**
   - Use Windows Snipping Tool (Win + Shift + S)
   - Save as: AI_MANUAL_001.png, etc.
   - Capture both question and response

3. **Note Response Time:**
   - Start timer when you click Send
   - Stop when AI response appears
   - Document in seconds

4. **Check Personalization:**
   - For tests 6-10, actively look for profile data usage
   - Does AI mention YOUR body type, colors, styles?
   - Generic advice = FAIL for personalization tests

5. **Test Context Awareness:**
   - For test 11, check if AI remembers previous message
   - Should reference earlier suggestions

6. **Evaluate Quality:**
   - Is the advice actually helpful?
   - Would you follow this advice?
   - Does it add value?

---

## 📋 **EXPECTED vs ACTUAL REPORT**

After testing, create a summary:

```
TEST: AI_MANUAL_001 - Wedding Outfit
──────────────────────────────────────────────────

EXPECTED:
- Response time: < 15 seconds
- Must contain: wedding, dress, formal
- Should suggest: Complete outfit
- Tone: Professional and helpful

ACTUAL:
- Response time: [YOUR OBSERVATION]
- Keywords found: [LIST]
- Suggestions: [WHAT AI SAID]
- Tone: [YOUR ASSESSMENT]

RESULT: PASS / FAIL
REASON: [Why it passed or failed]

──────────────────────────────────────────────────
```

---

## 🎯 **SUCCESS CRITERIA**

### **Overall Test Suite:**
- Minimum 80% pass rate (12/15 tests pass)
- All CRITICAL tests must pass (Tests 1, 2, 6, 7, 11)
- No major quality issues

### **Per Test:**
- Response time acceptable (< 30s)
- Relevant to question
- Actionable advice
- Appropriate behavior

### **Personalization Tests (6, 7, 8, 9, 10):**
- **MUST use profile data**
- Failure to personalize = TEST FAILS

---

## 📁 **DELIVERABLE**

After completing manual testing, create:

**File:** `MANUAL_AI_TEST_RESULTS.md`

**Include:**
1. Each test's Expected vs Actual
2. Screenshots for each scenario
3. Overall pass/fail summary
4. Quality assessment
5. Issues found (if any)
6. Recommendations

---

## ⏱️ **TIME ESTIMATE**

- Per test: 2-3 minutes
- Total for 15 tests: 30-45 minutes
- With documentation: 60 minutes

**Recommended:** Test in batches
- Batch 1: Tests 1-5 (Events)
- Batch 2: Tests 6-10 (Personalization) ⭐ CRITICAL
- Batch 3: Tests 11-15 (Context & Shopping)

---

## 🎯 **START TESTING!**

**Quick Start:**
1. Login to https://app.digitalstylist.com/chat
2. Start with TEST 1 (Wedding outfit)
3. Ask the question
4. Wait for AI response
5. Document using the template
6. Take screenshot
7. Move to next test

**Good luck with manual testing!** 🚀

This approach will give you **real insights** into AI quality and behavior!
