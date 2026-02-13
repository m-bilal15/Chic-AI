"""
Remove all emoji characters from test files for Windows compatibility
Replaces emojis with text equivalents
"""

import re
from pathlib import Path


def remove_emojis_from_file(file_path):
    """Remove emojis and replace with text equivalents"""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Emoji replacements
    replacements = {
        '✅': '[PASS]',
        '❌': '[FAIL]',
        '⚠️': '[WARNING]',
        '📸': '[SCREENSHOT]',
        '📊': '[RESULT]',
        '📝': '[NOTE]',
        '📧': '[EMAIL]',
        '🔒': '[SECURITY]',
        '🔑': '[PASSWORD]',
        '📏': '[BOUNDARY]',
        '🎨': '[UI]',
        '⌨️': '[KEYBOARD]',
        '👁': '[EYE]',
        '♿': '[A11Y]',
        '📋': '[CLIPBOARD]',
        '⏳': '[LOADING]',
        '🎯': '[TARGET]',
        '🎬': '[ANIMATION]',
        '🔧': '[CONFIG]',
        '🏷️': '[LABEL]',
        '⚡': '[PERFORMANCE]',
        '📱': '[RESPONSIVE]',
        '👁️': '[VISIBILITY]',
        '🔄': '[RESET]',
    }

    for emoji, replacement in replacements.items():
        content = content.replace(emoji, replacement)

    # Remove any remaining emojis (broad Unicode emoji range)
    # This regex removes most emoji characters
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "\U00002702-\U000027B0"
        "\U000024C2-\U0001F251"
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        "\U0001FA00-\U0001FA6F"  # Chess Symbols
        "\U00002600-\U000026FF"  # Miscellaneous Symbols
        "]+",
        flags=re.UNICODE
    )

    content = emoji_pattern.sub('', content)

    # Write back if changed
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def remove_emojis_from_all_tests():
    """Remove emojis from all test files"""

    testcases_dir = Path("testcases")

    if not testcases_dir.exists():
        print("ERROR: testcases directory not found!")
        return

    print("\n" + "="*70)
    print("REMOVING EMOJIS FROM ALL TEST FILES")
    print("="*70)

    cleaned_count = 0
    total_count = 0

    # Process all test_script.py files
    for test_dir in sorted(testcases_dir.iterdir()):
        if test_dir.is_dir() and test_dir.name.startswith("TC_SIGNUP"):
            test_file = test_dir / "test_script.py"

            if test_file.exists():
                total_count += 1
                print(f"Processing {test_dir.name}/test_script.py...", end=" ")

                try:
                    if remove_emojis_from_file(test_file):
                        print("[CLEANED]")
                        cleaned_count += 1
                    else:
                        print("[NO CHANGES]")
                except Exception as e:
                    print(f"[ERROR: {e}]")

    print("\n" + "="*70)
    print("EMOJI REMOVAL COMPLETE")
    print("="*70)
    print(f"Total files processed: {total_count}")
    print(f"Files cleaned: {cleaned_count}")
    print(f"No changes needed: {total_count - cleaned_count}")
    print("="*70)

    print("\n[NEXT STEPS]")
    print("1. Start your application on http://localhost:5173")
    print("2. Run: python run_critical_tests.py")
    print("3. Or run individual test: python testcases/TC_SIGNUP_001/test_script.py")
    print("\n")


if __name__ == "__main__":
    remove_emojis_from_all_tests()
