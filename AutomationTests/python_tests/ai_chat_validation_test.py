"""
AI Chat Model Validation Test
Tests AI responses, behavior, and requirement compliance
Uses: tim@gmail.com credentials
Created: February 13, 2026
"""

from playwright.sync_api import sync_playwright
import time
import json
from datetime import datetime

# Test credentials
TEST_EMAIL = "tim@gmail.com"
TEST_PASSWORD = "Qwerty@123"
BASE_URL = "https://app.digitalstylist.com"

# Define test scenarios with expected requirements
AI_TEST_SCENARIOS = [
    {
        "test_id": "AI_VAL_001",
        "category": "Event Styling",
        "user_query": "What should I wear to a wedding?",
        "requirements": {
            "response_time": "< 15 seconds",
            "must_contain": ["wedding", "dress", "outfit", "formal", "elegant"],
            "should_contain": ["color", "style", "accessories"],
            "must_not_contain": ["casual", "gym", "workout"],
            "personalization": "Should reference user's style preferences",
            "actionable": "Must provide specific outfit suggestions",
            "products": "Should show product recommendations"
        },
        "expected_behavior": [
            "AI understands wedding context",
            "Suggests formal/semi-formal attire",
            "Provides complete outfit suggestions",
            "Mentions appropriate colors",
            "May show product links"
        ]
    },
    {
        "test_id": "AI_VAL_002",
        "category": "Professional Styling",
        "user_query": "I have a job interview tomorrow. What should I wear?",
        "requirements": {
            "response_time": "< 15 seconds",
            "must_contain": ["interview", "professional", "business", "outfit"],
            "should_contain": ["confidence", "appropriate", "polished"],
            "must_not_contain": ["casual", "party", "beach"],
            "personalization": "Should align with user's style profile",
            "actionable": "Must provide specific clothing recommendations",
            "tone": "Professional and encouraging"
        },
        "expected_behavior": [
            "AI understands interview importance",
            "Suggests professional attire",
            "Considers confidence-building",
            "Provides reassurance",
            "May suggest colors that project confidence"
        ]
    },
    {
        "test_id": "AI_VAL_003",
        "category": "Color Advice - Personalization",
        "user_query": "What colors look good on me?",
        "requirements": {
            "response_time": "< 15 seconds",
            "must_contain": ["color", "colors"],
            "should_contain": ["body type", "skin tone", "preference"],
            "personalization": "CRITICAL - Must reference user's favorite colors from profile",
            "must_reference_profile": True,
            "actionable": "Specific color recommendations"
        },
        "expected_behavior": [
            "AI references user's favorite colors (from onboarding)",
            "Explains why certain colors work",
            "Suggests color combinations",
            "Personalized to user's profile",
            "May mention complementary colors"
        ]
    },
    {
        "test_id": "AI_VAL_004",
        "category": "Body Type Styling - Personalization",
        "user_query": "What styles suit my body type?",
        "requirements": {
            "response_time": "< 15 seconds",
            "must_contain": ["body type", "style", "suit"],
            "personalization": "CRITICAL - Must mention user's specific body type",
            "must_reference_profile": True,
            "actionable": "Body-type specific styling advice"
        },
        "expected_behavior": [
            "AI identifies user's body type (from profile)",
            "Provides body-type specific recommendations",
            "Mentions what to emphasize/avoid",
            "Suggests silhouettes that flatter",
            "References highlight/minimize areas"
        ]
    },
    {
        "test_id": "AI_VAL_005",
        "category": "Product Shopping",
        "user_query": "Show me some dress options for summer",
        "requirements": {
            "response_time": "< 15 seconds",
            "must_contain": ["dress", "summer"],
            "should_contain": ["options", "recommendations", "styles"],
            "products": "CRITICAL - Must show actual product recommendations",
            "actionable": "Clickable product links or visible products"
        },
        "expected_behavior": [
            "AI shows product recommendations",
            "Products are dresses (not pants/shoes)",
            "Appropriate for summer season",
            "Multiple options provided",
            "Products visible in UI or described"
        ]
    },
    {
        "test_id": "AI_VAL_006",
        "category": "Conversation Context",
        "user_query": ["I'm attending a wedding", "I prefer modest styles"],
        "requirements": {
            "response_time": "< 15 seconds each",
            "context_awareness": "CRITICAL - Second response must reference wedding from first message",
            "must_contain_second": ["modest", "wedding"],
            "personalization": "Adjust recommendations based on user feedback"
        },
        "expected_behavior": [
            "AI remembers wedding context",
            "Adjusts suggestions to modest styles",
            "Doesn't repeat same suggestions",
            "Shows understanding of refinement"
        ]
    },
    {
        "test_id": "AI_VAL_007",
        "category": "Wardrobe Building",
        "user_query": "What are essential pieces every wardrobe should have?",
        "requirements": {
            "response_time": "< 15 seconds",
            "must_contain": ["essential", "wardrobe", "pieces"],
            "should_contain": ["basics", "versatile", "must-have"],
            "structure": "Should provide organized list",
            "actionable": "Specific item suggestions"
        },
        "expected_behavior": [
            "AI provides structured list",
            "Mentions classic basics",
            "Suggests versatile pieces",
            "May personalize to user's style",
            "Practical and actionable"
        ]
    },
    {
        "test_id": "AI_VAL_008",
        "category": "Style Problem Solving",
        "user_query": "I always wear black. How can I add more color to my wardrobe?",
        "requirements": {
            "response_time": "< 15 seconds",
            "must_contain": ["color", "wardrobe"],
            "should_contain": ["gradually", "start", "options", "comfortable"],
            "tone": "Encouraging and supportive",
            "actionable": "Step-by-step or gradual approach"
        },
        "expected_behavior": [
            "AI acknowledges current style",
            "Suggests gradual transition",
            "Provides color options",
            "Makes it feel achievable",
            "Supportive tone"
        ]
    }
]


def login_to_chat(page):
    """Login and navigate to chat page"""

    print("\n[SETUP] Logging in to chat...")
    print(f"  Account: {TEST_EMAIL}")

    # Login
    page.goto(f"{BASE_URL}/login")
    time.sleep(2)

    page.fill('input[type="email"]', TEST_EMAIL)
    page.fill('input[type="password"]', TEST_PASSWORD)
    page.click('button:has-text("Sign In"), button[type="submit"]')
    time.sleep(5)

    # Navigate to chat
    page.goto(f"{BASE_URL}/chat")
    time.sleep(5)

    # Handle modals
    for _ in range(15):
        modal_btn = page.locator('button:has-text("Next"), button:has-text("Get Started"), button:has-text("Start Trial"), [aria-label*="close" i]')
        if modal_btn.count() > 0:
            try:
                modal_btn.first.click(timeout=2000)
                time.sleep(2)
            except:
                break
        else:
            break

    print("[OK] Logged in and ready\n")


def send_message_and_get_response(page, message):
    """Send message and capture AI response"""

    print(f"\n[USER] {message}")

    # Get initial message count
    initial_count = page.locator('[class*="message"]').count()

    # Type message
    chat_input = page.locator('textarea, input[placeholder*="style" i]').first
    chat_input.fill(message)
    time.sleep(1)

    # Send
    send_btn = page.locator('button[type="submit"], button svg, button:has-text("Send")').first
    send_btn.click()

    print(f"  [SENT] Message sent")
    time.sleep(2)

    # Wait for AI response (max 20 seconds)
    print(f"  [WAIT] Waiting for AI response...")

    response_received = False
    start_time = time.time()
    timeout = 20  # seconds

    while (time.time() - start_time) < timeout:
        current_count = page.locator('[class*="message"]').count()
        if current_count > initial_count + 1:  # User message + AI response
            response_received = True
            break
        time.sleep(1)

    response_time = time.time() - start_time

    # Capture AI response
    ai_response = ""
    if response_received:
        try:
            all_msgs = page.locator('[class*="message"]').all()
            if len(all_msgs) >= 2:
                # Get last message (AI response)
                ai_response = all_msgs[-1].text_content() or ""
                print(f"  [AI] Response received in {response_time:.1f}s")
                print(f"  [AI] {ai_response[:150]}...")
        except:
            ai_response = "Could not capture response text"
    else:
        print(f"  [WARNING] No AI response within {timeout}s")

    return {
        "response_time": response_time,
        "response_received": response_received,
        "ai_response": ai_response
    }


def validate_response(scenario, actual_result):
    """Validate AI response against requirements"""

    print(f"\n[VALIDATION] Checking against requirements...")
    print("-" * 80)

    requirements = scenario["requirements"]
    ai_response = actual_result["ai_response"].lower()

    validation_results = {
        "test_id": scenario["test_id"],
        "category": scenario["category"],
        "user_query": scenario["user_query"],
        "checks": [],
        "passed": 0,
        "failed": 0,
        "overall": "UNKNOWN"
    }

    # Check 1: Response Time
    response_time = actual_result["response_time"]
    time_requirement = requirements.get("response_time", "< 15 seconds")
    time_limit = 15  # seconds

    if response_time < time_limit:
        print(f"  [PASS] Response time: {response_time:.1f}s (requirement: {time_requirement})")
        validation_results["checks"].append({
            "check": "Response Time",
            "result": "PASS",
            "actual": f"{response_time:.1f}s",
            "expected": time_requirement
        })
        validation_results["passed"] += 1
    else:
        print(f"  [FAIL] Response time: {response_time:.1f}s (requirement: {time_requirement})")
        validation_results["checks"].append({
            "check": "Response Time",
            "result": "FAIL",
            "actual": f"{response_time:.1f}s",
            "expected": time_requirement
        })
        validation_results["failed"] += 1

    # Check 2: Must Contain Keywords
    if "must_contain" in requirements:
        must_keywords = requirements["must_contain"]
        found_keywords = [kw for kw in must_keywords if kw.lower() in ai_response]
        missing_keywords = [kw for kw in must_keywords if kw.lower() not in ai_response]

        if len(found_keywords) > 0:
            print(f"  [PASS] Must-have keywords found: {found_keywords}")
            validation_results["checks"].append({
                "check": "Must Contain Keywords",
                "result": "PASS",
                "actual": f"Found: {found_keywords}",
                "expected": must_keywords
            })
            validation_results["passed"] += 1
        else:
            print(f"  [FAIL] Missing required keywords: {missing_keywords}")
            validation_results["checks"].append({
                "check": "Must Contain Keywords",
                "result": "FAIL",
                "actual": f"Missing: {missing_keywords}",
                "expected": must_keywords
            })
            validation_results["failed"] += 1

    # Check 3: Should Contain (Optional but good)
    if "should_contain" in requirements:
        should_keywords = requirements["should_contain"]
        found = [kw for kw in should_keywords if kw.lower() in ai_response]

        if len(found) > 0:
            print(f"  [PASS] Recommended keywords found: {found}")
            validation_results["checks"].append({
                "check": "Should Contain Keywords",
                "result": "PASS",
                "actual": f"Found: {found}",
                "expected": should_keywords
            })
            validation_results["passed"] += 1
        else:
            print(f"  [INFO] Recommended keywords not found: {should_keywords}")
            validation_results["checks"].append({
                "check": "Should Contain Keywords",
                "result": "INFO",
                "actual": "None found",
                "expected": should_keywords
            })

    # Check 4: Must NOT Contain
    if "must_not_contain" in requirements:
        forbidden = requirements["must_not_contain"]
        found_forbidden = [kw for kw in forbidden if kw.lower() in ai_response]

        if len(found_forbidden) == 0:
            print(f"  [PASS] No forbidden keywords found")
            validation_results["checks"].append({
                "check": "Must NOT Contain",
                "result": "PASS",
                "actual": "Clean",
                "expected": f"Avoid: {forbidden}"
            })
            validation_results["passed"] += 1
        else:
            print(f"  [FAIL] Forbidden keywords found: {found_forbidden}")
            validation_results["checks"].append({
                "check": "Must NOT Contain",
                "result": "FAIL",
                "actual": f"Found: {found_forbidden}",
                "expected": f"Should not contain: {forbidden}"
            })
            validation_results["failed"] += 1

    # Check 5: Response Quality
    if len(ai_response) > 50:
        print(f"  [PASS] Response is substantial ({len(ai_response)} characters)")
        validation_results["checks"].append({
            "check": "Response Length",
            "result": "PASS",
            "actual": f"{len(ai_response)} chars",
            "expected": "> 50 chars (helpful response)"
        })
        validation_results["passed"] += 1
    else:
        print(f"  [FAIL] Response too short ({len(ai_response)} characters)")
        validation_results["checks"].append({
            "check": "Response Length",
            "result": "FAIL",
            "actual": f"{len(ai_response)} chars",
            "expected": "> 50 chars"
        })
        validation_results["failed"] += 1

    # Overall result
    total_checks = validation_results["passed"] + validation_results["failed"]
    pass_rate = (validation_results["passed"] / total_checks * 100) if total_checks > 0 else 0

    if pass_rate >= 80:
        validation_results["overall"] = "PASS"
        print(f"\n  [OVERALL] PASS ({validation_results['passed']}/{total_checks} checks passed - {pass_rate:.0f}%)")
    else:
        validation_results["overall"] = "FAIL"
        print(f"\n  [OVERALL] FAIL ({validation_results['passed']}/{total_checks} checks passed - {pass_rate:.0f}%)")

    return validation_results


def run_ai_validation_tests():
    """Run all AI validation test scenarios"""

    print("\n" + "=" * 80)
    print("AI CHAT MODEL VALIDATION TEST SUITE")
    print("=" * 80)
    print(f"Test Scenarios: {len(AI_TEST_SCENARIOS)}")
    print(f"Account: {TEST_EMAIL}")
    print(f"Focus: Response quality, behavior, requirement compliance")
    print("=" * 80 + "\n")

    all_results = {
        "test_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "account": TEST_EMAIL,
        "total_scenarios": len(AI_TEST_SCENARIOS),
        "passed": 0,
        "failed": 0,
        "scenarios": []
    }

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        try:
            # Login
            login_to_chat(page)

            page.screenshot(path="results/ai_validation_initial.png", full_page=True)

            # Run each scenario
            for i, scenario in enumerate(AI_TEST_SCENARIOS, 1):
                print("\n" + "=" * 80)
                print(f"TEST SCENARIO {i}/{len(AI_TEST_SCENARIOS)}: {scenario['test_id']}")
                print("=" * 80)
                print(f"Category: {scenario['category']}")
                print(f"Query: {scenario['user_query']}")
                print("=" * 80)

                # Handle multi-turn conversations
                if isinstance(scenario['user_query'], list):
                    # Multi-turn conversation
                    responses = []
                    for msg in scenario['user_query']:
                        result = send_message_and_get_response(page, msg)
                        responses.append(result)
                    # Use last response for validation
                    actual_result = responses[-1]
                    actual_result['conversation'] = responses
                else:
                    # Single message
                    actual_result = send_message_and_get_response(page, scenario['user_query'])

                page.screenshot(path=f"results/ai_validation_{scenario['test_id']}.png", full_page=True)

                # Validate response
                validation = validate_response(scenario, actual_result)
                validation['actual_response'] = actual_result['ai_response']
                validation['response_time'] = actual_result['response_time']

                all_results['scenarios'].append(validation)

                if validation['overall'] == "PASS":
                    all_results['passed'] += 1
                else:
                    all_results['failed'] += 1

                # Small delay between scenarios
                time.sleep(3)

            # Final screenshot
            page.screenshot(path="results/ai_validation_complete.png", full_page=True)

            # Keep browser open for review
            print("\n" + "=" * 80)
            print("Browser will stay open for 20 seconds for review...")
            print("=" * 80)
            time.sleep(20)

        except Exception as e:
            print(f"\n[ERROR] Test suite failed: {e}")
            page.screenshot(path="results/ai_validation_error.png", full_page=True)
            import traceback
            traceback.print_exc()

        finally:
            browser.close()

    # ==========================================
    # GENERATE REPORT
    # ==========================================
    print("\n\n" + "=" * 80)
    print("AI VALIDATION TEST RESULTS")
    print("=" * 80)
    print(f"Total Scenarios:  {all_results['total_scenarios']}")
    print(f"Passed:           {all_results['passed']}")
    print(f"Failed:           {all_results['failed']}")
    print(f"Pass Rate:        {all_results['passed']/all_results['total_scenarios']*100:.1f}%")
    print("=" * 80)

    # Print individual results
    print("\nIndividual Scenario Results:")
    print("-" * 80)
    for scenario in all_results['scenarios']:
        status = "PASS" if scenario['overall'] == "PASS" else "FAIL"
        symbol = "[OK]" if status == "PASS" else "[FAIL]"
        print(f"{symbol} {scenario['test_id']}: {scenario['category']} - {status}")
        print(f"     Query: {scenario['user_query']}")
        print(f"     Checks: {scenario['passed']}/{scenario['passed']+scenario['failed']} passed")

    # Save detailed results
    output_file = f"results/AI_VALIDATION_REPORT_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_file, "w", encoding='utf-8') as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)

    print(f"\n[SAVED] Detailed results: {output_file}")

    # Generate markdown report
    generate_markdown_report(all_results)

    print("\n" + "=" * 80)
    print("AI VALIDATION TEST COMPLETE")
    print("=" * 80 + "\n")

    return all_results


def generate_markdown_report(results):
    """Generate human-readable markdown report"""

    report_file = f"results/AI_VALIDATION_REPORT_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"

    with open(report_file, "w", encoding='utf-8') as f:
        f.write("# AI Chat Model Validation Report\n\n")
        f.write(f"**Date:** {results['test_date']}\n")
        f.write(f"**Account:** {results['account']}\n")
        f.write(f"**Pass Rate:** {results['passed']}/{results['total_scenarios']} ({results['passed']/results['total_scenarios']*100:.1f}%)\n\n")
        f.write("---\n\n")

        f.write("## Test Scenarios\n\n")

        for scenario in results['scenarios']:
            f.write(f"### {scenario['test_id']}: {scenario['category']}\n\n")
            f.write(f"**User Query:** \"{scenario['user_query']}\"\n\n")
            f.write(f"**Overall Result:** {scenario['overall']}\n\n")
            f.write(f"**Response Time:** {scenario['response_time']:.1f}s\n\n")

            f.write("**AI Response:**\n")
            f.write(f"> {scenario['actual_response'][:300]}...\n\n")

            f.write("**Validation Checks:**\n\n")
            for check in scenario['checks']:
                symbol = "✅" if check['result'] == "PASS" else ("❌" if check['result'] == "FAIL" else "ℹ️")
                f.write(f"- {symbol} **{check['check']}:** {check['result']}\n")
                f.write(f"  - Expected: {check['expected']}\n")
                f.write(f"  - Actual: {check['actual']}\n")

            f.write(f"\n**Checks Passed:** {scenario['passed']}/{scenario['passed']+scenario['failed']}\n\n")
            f.write("---\n\n")

    print(f"[SAVED] Markdown report: {report_file}")


if __name__ == "__main__":
    run_ai_validation_tests()
