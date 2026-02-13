# Comprehensive AI Chat Test Scenarios - Bug Discovery

**Purpose:** Test AI chat thoroughly to identify bugs and issues
**Account:** tim@gmail.com / Qwerty@123
**Date:** February 13, 2026
**Tester:** QA Lead - Bilal

---

## 🎯 **TESTING APPROACH**

**Goal:** Find bugs and issues in AI chat functionality

**Focus Areas:**
1. **Personalization** (Does AI use profile data?)
2. **Context Awareness** (Does AI remember conversation?)
3. **Response Quality** (Is advice helpful and accurate?)
4. **Feature Completeness** (Do all features work?)
5. **Error Handling** (How does AI handle edge cases?)

---

## 📋 **30 TEST CONVERSATIONS**

### **CATEGORY 1: PERSONALIZATION BUGS (10 tests)**

---

#### **TEST 1: Body Shape Recognition**

**Test ID:** CONV_PERS_001
**Bug Check:** Does AI know user's body shape?

**Conversation:**
```
User: "What styles suit my body type?"
```

**Profile Data:** Body Shape = Rectangle

**Expected:**
> "For your Rectangle body shape, I recommend..."

**Actual:** ________________

**Bug?**
- ☐ YES - AI asks what body type is
- ☐ NO - AI mentions Rectangle
- ☐ PARTIAL - AI gives generic advice

**Notes:** ________________

---

#### **TEST 2: Favorite Colors**

**Test ID:** CONV_PERS_002
**Bug Check:** Does AI know favorite colors?
**Status:** ✅ Already tested - BUG CONFIRMED

**Result:** AI asks for colors instead of using Black, Pink, etc.

---

#### **TEST 3: Highlight Areas**

**Test ID:** CONV_PERS_003
**Bug Check:** Does AI use highlight areas?

**Conversation:**
```
User: "How can I accentuate my best features?"
```

**Profile Data:** Highlight = Waist, Arms (+2 more)

**Expected:**
> "To highlight your waist and arms, try..."

**Actual:** ________________

**Bug?**
- ☐ YES - Doesn't mention waist/arms
- ☐ NO - References highlight areas
- ☐ ASKS - Asks which features to highlight

---

#### **TEST 4: Minimize Areas**

**Test ID:** CONV_PERS_004
**Bug Check:** Does AI respect minimize preferences?

**Conversation:**
```
User: "What should I avoid wearing to balance my figure?"
```

**Profile Data:** Minimize = Shoulders, Legs (+2 more)

**Expected:**
> "To balance your shoulders and legs, avoid..."

**Actual:** ________________

**Bug?**
- ☐ YES - Doesn't consider minimize areas
- ☐ NO - Mentions shoulders/legs
- ☐ ASKS - Asks what to minimize

---

#### **TEST 5: Style Preferences**

**Test ID:** CONV_PERS_005
**Bug Check:** Does AI know style words?

**Conversation:**
```
User: "Recommend outfits that match my personal style"
```

**Profile Data:** Style = Chic, Classic, Romantic

**Expected:**
> "Based on your Chic, Classic, and Romantic style, I suggest..."

**Actual:** ________________

**Bug?**
- ☐ YES - Asks for style preferences
- ☐ NO - Uses Chic/Classic/Romantic
- ☐ GENERIC - Generic suggestions

---

#### **TEST 6: Height Consideration**

**Test ID:** CONV_PERS_006
**Bug Check:** Does AI consider height?

**Conversation:**
```
User: "What dress lengths work best for me?"
```

**Profile Data:** Height = 5 feet 5 inches

**Expected:**
> "At 5'5", midi and knee-length dresses work well..."

**Actual:** ________________

**Bug?**
- ☐ YES - Asks for height
- ☐ NO - References 5'5"
- ☐ GENERIC - Generic length advice

---

#### **TEST 7: Size Information**

**Test ID:** CONV_PERS_007
**Bug Check:** Does AI know user's sizes?

**Conversation:**
```
User: "What size should I order in this dress?"
```

**Profile Data:** Dress size = M, Top = L, Bottom = L

**Expected:**
> "Based on your profile, you typically wear size M in dresses..."

**Actual:** ________________

**Bug?**
- ☐ YES - Asks for size
- ☐ NO - References size M
- ☐ N/A - Can't answer without specific dress

---

#### **TEST 8: Professional Context**

**Test ID:** CONV_PERS_008
**Bug Check:** Does AI know user's profession?

**Conversation:**
```
User: "What should I wear to work?"
```

**Profile Data:** Profession = Sales Officer, Environment = Office

**Expected:**
> "For your role as a Sales Officer in an office environment..."

**Actual:** ________________

**Bug?**
- ☐ YES - Asks about job
- ☐ NO - References Sales Officer
- ☐ GENERIC - Generic office advice

---

#### **TEST 9: Budget Awareness**

**Test ID:** CONV_PERS_009
**Bug Check:** Does AI consider budget?

**Conversation:**
```
User: "Show me some dresses I can buy"
```

**Profile Data:** Budget = Moderate

**Expected:**
AI shows moderately priced items or mentions budget consideration

**Actual:** ________________

**Bug?**
- ☐ YES - Shows very expensive items
- ☐ NO - Appropriate price range
- ☐ UNCLEAR - Can't determine

---

#### **TEST 10: Complete Profile Awareness**

**Test ID:** CONV_PERS_010
**Bug Check:** Holistic profile usage

**Conversation:**
```
User: "Give me your best outfit recommendation for me"
```

**Expected:**
AI should use: Body shape + Colors + Style + Profession + Budget

**Actual:** ________________

**Profile Data Used:**
- ☐ Body shape
- ☐ Colors
- ☐ Style words
- ☐ Profession
- ☐ Budget
- ☐ None (generic)

---

### **CATEGORY 2: CONTEXT & MEMORY BUGS (8 tests)**

---

#### **TEST 11: Short-Term Memory**

**Test ID:** CONV_CTX_001
**Bug Check:** Does AI remember within conversation?

**Conversation:**
```
1. User: "I'm going to a wedding"
2. [Wait for AI response]
3. User: "What shoes should I wear?"
```

**Expected:** AI references wedding from message 1

**Actual Message 2:** ________________

**Bug?**
- ☐ YES - Doesn't remember wedding
- ☐ NO - Says "for the wedding..."
- ☐ ASKS - "For what occasion?"

---

#### **TEST 12: Refinement Memory**

**Test ID:** CONV_CTX_002
**Bug Check:** Does AI adapt to feedback?

**Conversation:**
```
1. User: "Show me dress options"
2. [AI shows dresses]
3. User: "I prefer something more modest"
```

**Expected:** AI adjusts suggestions, doesn't repeat same dresses

**Actual:** ________________

**Bug?**
- ☐ YES - Shows same dresses
- ☐ YES - Ignores "modest" feedback
- ☐ NO - Adjusts appropriately

---

#### **TEST 13: Previous Product Reference**

**Test ID:** CONV_CTX_003
**Bug Check:** Can AI reference shown products?

**Conversation:**
```
1. User: "Show me black dresses"
2. [AI shows products]
3. User: "I like the first one, what would go with it?"
```

**Expected:** AI references the specific dress from its previous response

**Actual:** ________________

**Bug?**
- ☐ YES - Can't reference previous product
- ☐ NO - Coordinates accessories for that dress

---

#### **TEST 14: Multiple Item Coordination**

**Test ID:** CONV_CTX_004
**Bug Check:** Building complete outfit

**Conversation:**
```
1. User: "I need a dress for a party"
2. [AI responds]
3. User: "What shoes?"
4. [AI responds]
5. User: "And accessories?"
```

**Expected:** Each response builds on previous (dress → shoes that match → accessories that complete look)

**Actual:** ________________

**Bug?**
- ☐ YES - Each response is disconnected
- ☐ NO - Builds cohesive outfit
- ☐ PARTIAL - Some context, not all

---

#### **TEST 15: Topic Change Handling**

**Test ID:** CONV_CTX_005
**Bug Check:** Can AI handle topic switches?

**Conversation:**
```
1. User: "I need formal wear"
2. [AI responds about formal]
3. User: "Actually, show me casual outfits instead"
```

**Expected:** AI switches to casual, doesn't insist on formal

**Actual:** ________________

**Bug?**
- ☐ YES - Confused or continues formal
- ☐ NO - Smoothly switches to casual

---

#### **TEST 16: Return to Previous Topic**

**Test ID:** CONV_CTX_006
**Bug Check:** Can AI recall earlier conversation?

**Conversation:**
```
1. User: "I need a wedding outfit"
2. [AI suggests outfits]
3. User: "Show me casual clothes"
4. [AI shows casual]
5. User: "Back to the wedding outfit, which dress was best?"
```

**Expected:** AI recalls wedding suggestions

**Actual:** ________________

**Bug?**
- ☐ YES - Can't remember earlier part
- ☐ NO - References wedding dresses

---

#### **TEST 17: Negation Handling**

**Test ID:** CONV_CTX_007
**Bug Check:** Understanding "not" and "don't"

**Conversation:**
```
User: "I need a dress but NOT in red and NOT too formal"
```

**Expected:** Shows dresses that are: (not red) AND (not formal)

**Actual:** ________________

**Bug?**
- ☐ YES - Shows red dresses
- ☐ YES - Shows formal dresses
- ☐ NO - Respects both constraints

---

#### **TEST 18: Comparison Request**

**Test ID:** CONV_CTX_008
**Bug Check:** Can AI compare options?

**Conversation:**
```
1. User: "Show me two dress options for a party"
2. [AI shows options]
3. User: "Which one is better for my body type?"
```

**Expected:** AI compares both dresses against user's body shape

**Actual:** ________________

**Bug?**
- ☐ YES - Can't compare or reference previous
- ☐ NO - Provides comparison

---

### **CATEGORY 3: RESPONSE QUALITY BUGS (6 tests)**

---

#### **TEST 19: Vague Question Handling**

**Test ID:** CONV_QUAL_001
**Bug Check:** How does AI handle unclear questions?

**Conversation:**
```
User: "Help me"
```

**Expected:** AI asks clarifying questions
> "I'd be happy to help! What are you looking for - outfit advice, shopping recommendations, or styling tips?"

**Actual:** ________________

**Bug?**
- ☐ YES - Makes assumptions
- ☐ YES - Generic unhelpful response
- ☐ NO - Asks clarifying questions

---

#### **TEST 20: Contradictory Request**

**Test ID:** CONV_QUAL_002
**Bug Check:** Handling impossible requests

**Conversation:**
```
User: "I want formal professional outfit that's also very casual"
```

**Expected:** AI clarifies contradiction or suggests business casual middle ground

**Actual:** ________________

**Bug?**
- ☐ YES - Confused or nonsensical response
- ☐ NO - Addresses contradiction gracefully

---

#### **TEST 21: Non-Fashion Question**

**Test ID:** CONV_QUAL_003
**Bug Check:** Staying on topic

**Conversation:**
```
User: "What's the weather today?"
```

**Expected:** AI politely redirects to fashion/styling

**Actual:** ________________

**Bug?**
- ☐ YES - Tries to answer weather
- ☐ NO - Redirects to styling topic

---

#### **TEST 22: Inappropriate Request**

**Test ID:** CONV_QUAL_004
**Bug Check:** Content moderation

**Conversation:**
```
User: "Show me revealing outfits"
```

**Expected:** AI provides tasteful suggestions or declines

**Actual:** ________________

**Bug?**
- ☐ YES - Inappropriate suggestions
- ☐ NO - Professional handling

---

#### **TEST 23: Price Range Request**

**Test ID:** CONV_QUAL_005
**Bug Check:** Budget constraints

**Conversation:**
```
User: "Show me dresses under $50"
```

**Expected:** Products shown are under $50

**Actual:** Products shown: $____, $____, $____

**Bug?**
- ☐ YES - Shows expensive items over budget
- ☐ NO - All within $50 range

---

#### **TEST 24: Seasonal Appropriateness**

**Test ID:** CONV_QUAL_006
**Bug Check:** Season awareness

**Conversation:**
```
User: "I need summer outfits"
```

**Expected:** Light fabrics, summer-appropriate styles

**Actual:** ________________

**Bug?**
- ☐ YES - Suggests winter clothes
- ☐ NO - Appropriate summer items

---

### **CATEGORY 4: FEATURE COMPLETENESS BUGS (6 tests)**

---

#### **TEST 25: Product Recommendations**

**Test ID:** CONV_FEAT_001
**Bug Check:** Are products actually shown?

**Conversation:**
```
User: "Show me black dresses"
```

**Expected:** Actual product cards/images visible in UI

**Actual:** ________________

**Bug?**
- ☐ YES - AI mentions products but nothing shows
- ☐ NO - Products visible in UI
- ☐ PARTIAL - Text description only, no images

---

#### **TEST 26: Shopping Links**

**Test ID:** CONV_FEAT_002
**Bug Check:** Can user actually shop?

**Conversation:**
```
1. User: "Show me a specific dress"
2. [AI shows product]
3. Click "Shop Now" button
```

**Expected:** Opens product page or shopping link

**Actual:** ________________

**Bug?**
- ☐ YES - Link broken or doesn't work
- ☐ NO - Shopping link works
- ☐ N/A - No shop button available

---

#### **TEST 27: Image Upload**

**Test ID:** CONV_FEAT_003
**Bug Check:** Can user upload outfit images?

**Conversation:**
```
1. Click "Upload Outfit" button
2. Select an image file
3. Ask: "What do you think of this outfit?"
```

**Expected:** AI analyzes uploaded image and provides feedback

**Actual:** ________________

**Bug?**
- ☐ YES - Upload doesn't work
- ☐ YES - Image uploads but AI doesn't analyze
- ☐ NO - AI provides outfit analysis

---

#### **TEST 28: Wardrobe Integration**

**Test ID:** CONV_FEAT_004
**Bug Check:** Does "My Wardrobe" integrate with chat?

**Conversation:**
```
User: "Show me outfits from my wardrobe"
```

**Expected:** AI references items from My Wardrobe section

**Actual:** ________________

**Bug?**
- ☐ YES - Can't access wardrobe
- ☐ NO - Shows wardrobe items
- ☐ EMPTY - No items in wardrobe

---

#### **TEST 29: Conversation History**

**Test ID:** CONV_FEAT_005
**Bug Check:** Can user access previous conversations?

**Action:**
```
1. Click on "Recent Conversations" in sidebar
2. Select a previous conversation
3. Check if messages are preserved
```

**Expected:** Previous conversation loads with full history

**Actual:** ________________

**Bug?**
- ☐ YES - History lost or incomplete
- ☐ NO - Conversation preserved
- ☐ YES - Can't access old conversations

---

#### **TEST 30: New Conversation**

**Test ID:** CONV_FEAT_006
**Bug Check:** Does new conversation work?

**Action:**
```
1. Click "+ New Conversation"
2. Send a message
```

**Expected:** Fresh conversation starts, no previous messages

**Actual:** ________________

**Bug?**
- ☐ YES - Previous messages still showing
- ☐ NO - Clean new conversation

---

### **CATEGORY 5: EDGE CASES & ERRORS (6 tests)**

---

#### **TEST 31: Very Long Message**

**Test ID:** CONV_EDGE_001
**Bug Check:** Character limit handling

**Conversation:**
```
User: [Type 500+ characters]
"I need help with my style for work. I'm a sales officer and I attend many meetings... [continue to 500+ chars]"
```

**Expected:** Message truncated at 500 or error shown

**Actual:** ________________

**Bug?**
- ☐ YES - Accepts >500 chars (limit not enforced)
- ☐ NO - Enforces 500 char limit

---

#### **TEST 32: Rapid Messages**

**Test ID:** CONV_EDGE_002
**Bug Check:** Can AI handle quick succession?

**Conversation:**
```
Send 3 messages quickly (within 10 seconds):
1. "Hello"
2. "I need help"
3. "Show me dresses"
```

**Expected:** AI responds to all 3 appropriately

**Actual:** ________________

**Bug?**
- ☐ YES - AI confused or drops messages
- ☐ NO - Handles all messages

---

#### **TEST 33: Special Characters**

**Test ID:** CONV_EDGE_003
**Bug Check:** Input sanitization

**Conversation:**
```
User: "I need a dress & shoes, but not heels - I prefer flats!"
```

**Expected:** AI handles &, -, ! normally

**Actual:** ________________

**Bug?**
- ☐ YES - Encoding errors or broken
- ☐ NO - Works fine

---

#### **TEST 34: Empty/Incomplete Messages**

**Test ID:** CONV_EDGE_004
**Bug Check:** Validation

**Action:**
```
Try to send empty message (just spaces)
```

**Expected:** Cannot send or validation error

**Actual:** ________________

**Bug?**
- ☐ YES - Sends empty message
- ☐ NO - Prevents sending empty

---

#### **TEST 35: No AI Response**

**Test ID:** CONV_ERR_001
**Bug Check:** Timeout handling

**Conversation:**
```
User: "Help me with styling"
[Wait 60+ seconds]
```

**Expected:** Error message or "AI is thinking..." indicator

**Actual:** ________________

**Bug?**
- ☐ YES - Hangs forever, no feedback
- ☐ NO - Shows error or timeout message

---

#### **TEST 36: Network Interruption**

**Test ID:** CONV_ERR_002
**Bug Check:** Offline handling

**Action:**
```
1. Send message
2. Immediately disconnect WiFi
3. Reconnect after 10s
```

**Expected:** Error message, retry option, or queues message

**Actual:** ________________

**Bug?**
- ☐ YES - Message lost, no error
- ☐ NO - Graceful error handling

---

## 📊 **RESULTS SUMMARY TEMPLATE**

After completing all tests:

```
╔══════════════════════════════════════════════════════════╗
║  COMPREHENSIVE AI TESTING RESULTS                        ║
╠══════════════════════════════════════════════════════════╣
║  Total Tests:           36                               ║
║  Tests Completed:       __                               ║
║  Bugs Found:            __                               ║
║  Critical Bugs:         __                               ║
║  High Priority Bugs:    __                               ║
║  Medium/Low Bugs:       __                               ║
╠══════════════════════════════════════════════════════════╣
║  Category Breakdown:                                     ║
║    Personalization:     __/10 issues                     ║
║    Context/Memory:      __/8 issues                      ║
║    Quality:             __/6 issues                      ║
║    Features:            __/6 issues                      ║
║    Edge Cases:          __/6 issues                      ║
╚══════════════════════════════════════════════════════════╝
```

---

## 🐛 **BUGS TO DOCUMENT**

For each bug found, create bug report with:

**Bug ID:** BUG-AI-XXX-###
**Title:** [Clear description]
**Severity:** Critical / High / Medium / Low
**Steps to Reproduce:** [Exact conversation]
**Expected:** [What should happen]
**Actual:** [What actually happened]
**Profile Data:** [Relevant profile info]
**Screenshot:** [Filename]

---

## 🎯 **TESTING PRIORITIES**

### **START WITH (Critical):**
1. ✅ TEST 2 - Favorite Colors (ALREADY CONFIRMED BUG)
2. TEST 1 - Body Shape
3. TEST 5 - Style Preferences
4. TEST 11 - Short-term memory
5. TEST 25 - Product recommendations

### **THEN TEST (High):**
6-10. Remaining personalization tests
11-18. Context awareness tests

### **FINALLY (Medium):**
19-36. Quality, features, edge cases

---

## ⏱️ **TIME ESTIMATE**

- **Critical tests (5):** 15-20 minutes
- **All 36 tests:** 60-90 minutes
- **With documentation:** 2 hours

---

## 📁 **DELIVERABLES**

After testing, you should have:

1. **Completed test results** (this file filled out)
2. **Bug reports** (one per bug found)
3. **Screenshots** (evidence for each bug)
4. **Summary document** (overall findings)

---

**START TESTING WITH THE CRITICAL 5 TESTS FIRST!** 🚀

Document each result and we'll create bug reports for all issues found! 🎯
