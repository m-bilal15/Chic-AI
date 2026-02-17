# CHIC-AI Test Automation Framework

> **CHIC Login Page Test Automation Framework**
> Python + Playwright + Pytest

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-Latest-green.svg)](https://playwright.dev/)
[![Pytest](https://img.shields.io/badge/Pytest-Latest-orange.svg)](https://docs.pytest.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running Tests](#running-tests)
- [Test Results](#test-results)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [Contact](#contact)

## 🎯 Overview

CHIC-AI is a production-ready test automation framework designed for testing the CHIC Login Page. Built with industry-standard tools (Python, Playwright, Pytest), this framework provides comprehensive test coverage with evidence-based validation.

**Key Highlights:**
- ✅ 50 comprehensive test cases
- ✅ 100% test pass rate achieved
- ✅ Evidence-based validation (screenshots + videos)
- ✅ Multi-environment support (dev, staging, production)
- ✅ Page Object Model architecture
- ✅ HTML reporting with pytest-html
- ✅ Auto-screenshots on test failure

## ✨ Features

### Testing Capabilities
- **Functional Testing** - Complete login flow validation
- **Validation Testing** - Input field validation (email, password)
- **Error Handling** - Error message verification
- **Security Testing** - Authentication and session management
- **Cross-browser Testing** - Chromium, Firefox, WebKit support

### Framework Features
- **Page Object Model** - Maintainable and reusable page objects
- **Pytest Fixtures** - Clean test code with reusable fixtures
- **Configuration Management** - .env and config.ini for multi-environment
- **Auto Screenshots** - Automatic evidence capture on failures
- **Video Recording** - Full test execution recordings
- **HTML Reports** - Detailed test execution reports
- **Parallel Execution** - Run tests in parallel for faster execution
- **Custom Markers** - Categorize tests (smoke, regression, critical, etc.)

## 📁 Project Structure

```
Chic-AI/
├── .gitignore                          # Version control rules
├── README.md                           # This file
├── CLAUDE.md                           # Testing guidelines and standards
└── AutomationTests/
    └── python_tests/
        ├── requirements.txt            # Python dependencies
        ├── pytest.ini                  # Pytest configuration
        ├── conftest.py                 # Pytest fixtures & hooks
        ├── .env.example                # Environment template
        ├── .env                        # Your configuration (gitignored)
        ├── config/
        │   ├── config.ini              # Multi-environment config
        │   └── selectors.json          # UI selectors
        ├── test_data/                  # Test data files
        │   ├── valid_credentials.json
        │   └── invalid_credentials.json
        ├── pages/                      # Page Object Model
        │   ├── base_page.py
        │   └── login_page.py
        ├── utils/                      # Helper utilities
        │   ├── config_reader.py
        │   ├── logger.py
        │   └── helpers.py
        ├── testcases/                  # Test scripts
        │   ├── TC_LOGIN_001/
        │   │   └── test_script.py
        │   └── TC_LOGIN_XXX/
        └── results/                    # Test results
            ├── Passed/                 # Passed test evidence
            ├── Failed/                 # Failed test evidence
            ├── failures/               # Auto-screenshots
            ├── logs/                   # Log files
            ├── report.html             # HTML report
            └── SUMMARY.md              # Test summary
```

## 🔧 Prerequisites

- **Python 3.8+** - [Download Python](https://www.python.org/downloads/)
- **Git** - [Download Git](https://git-scm.com/downloads)
- **pip** - Comes with Python
- **Virtual Environment** - Recommended for isolation

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/m-bilal15/Chic-AI.git
cd Chic-AI/AutomationTests/python_tests
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright Browsers

```bash
playwright install chromium
```

### 5. Configure Environment

```bash
# Copy example environment file
cp .env.example .env

# Edit .env with your configuration
# Set TEST_EMAIL, TEST_PASSWORD, BASE_URL, etc.
```

## ⚙️ Configuration

### Environment Variables (.env)

```bash
# Environment
ENVIRONMENT=dev

# Test Credentials
TEST_EMAIL=bilal@test.com
TEST_PASSWORD=ValidPass@123

# Application
BASE_URL=http://localhost:5173

# Browser Settings
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
# Via .env file
ENVIRONMENT=staging

# Or via command line
export ENVIRONMENT=staging  # Mac/Linux
set ENVIRONMENT=staging     # Windows
```

## 🧪 Running Tests

### Run All Tests

```bash
# Activate virtual environment first
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

# Run all tests with verbose output
pytest -v

# Run with HTML report
pytest --html=results/report.html
```

### Run Specific Tests

```bash
# Run single test
pytest testcases/TC_LOGIN_001/test_script.py

# Run by marker
pytest -m smoke           # Smoke tests only
pytest -m critical        # Critical tests only
pytest -m validation      # Validation tests only

# Run specific test function
pytest testcases/TC_LOGIN_001/test_script.py::test_tc_login_001
```

### Run in Parallel

```bash
# Auto-detect CPU cores
pytest -n auto

# Use specific number of workers
pytest -n 4
```

### Additional Options

```bash
# Stop on first failure
pytest -x

# Show available markers
pytest --markers

# Verbose output with logs
pytest -v -s

# Run and open HTML report
pytest --html=results/report.html && start results/report.html
```

## 📊 Test Results

### Result Organization

After test execution, results are organized as:

```
results/
├── Passed/
│   └── TC_LOGIN_XXX/
│       ├── screenshot.png
│       ├── video.webm
│       └── TEST_REPORT.md
├── Failed/
│   └── TC_LOGIN_XXX/
│       ├── screenshot.png
│       ├── video.webm
│       └── BUG_REPORT.md
├── failures/                # Auto-screenshots
├── logs/                    # Log files
├── report.html              # HTML report
└── SUMMARY.md               # Test summary
```

### View Reports

```bash
# Open HTML report
start results/report.html      # Windows
open results/report.html       # Mac
xdg-open results/report.html   # Linux

# View summary
cat results/SUMMARY.md
```

## 📚 Documentation

Comprehensive documentation is available in the repository:

- **[SETUP_GUIDE.md](AutomationTests/python_tests/SETUP_GUIDE.md)** - Detailed installation and setup guide
- **[CLAUDE.md](CLAUDE.md)** - Testing standards, guidelines, and best practices
- **[STRUCTURE_ANALYSIS_AND_IMPROVEMENTS.md](AutomationTests/python_tests/STRUCTURE_ANALYSIS_AND_IMPROVEMENTS.md)** - Framework analysis
- **[IMPLEMENTATION_STATUS.md](AutomationTests/python_tests/IMPLEMENTATION_STATUS.md)** - Current status and roadmap

## 🏗️ Framework Architecture

### Page Object Model

```python
# pages/login_page.py
class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def login(self, email, password):
        self.fill_email(email)
        self.fill_password(password)
        self.click_login()
```

### Test Structure (Pytest Fixtures)

```python
# testcases/TC_LOGIN_001/test_script.py
import pytest

@pytest.mark.smoke
@pytest.mark.critical
def test_valid_login(page, login_page, base_url):
    """Test valid login with correct credentials"""
    page.goto(base_url)
    login_page.login("valid@email.com", "ValidPass@123")
    assert login_page.is_logged_in()
```

## 🎯 Test Coverage

- **50 Test Cases** covering:
  - Valid login scenarios (10 tests)
  - Validation tests (20 tests)
  - Error handling (10 tests)
  - Security tests (5 tests)
  - UI/UX tests (5 tests)

**Pass Rate:** 100% ✅

## 🔍 Key Features

### Evidence-Based Validation
Every test captures:
- Screenshots (pass/fail)
- Video recordings
- Detailed logs

### Configuration Management
- Multi-environment support
- Secure credential handling
- Environment-specific settings

### Modern Pytest Features
- Fixtures for clean code
- Markers for test categorization
- Parallel execution support
- Auto-retry on failure (optional)

## 🛠️ Troubleshooting

### Common Issues

**1. Import Errors**
```bash
# Ensure virtual environment is activated
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

**2. Playwright Browsers Not Found**
```bash
# Reinstall browsers
playwright install chromium
```

**3. Tests Failing**
```bash
# Check evidence files first
# View screenshots in results/failures/
# Watch videos in results/TC_LOGIN_XXX/
```

For more help, see [SETUP_GUIDE.md](AutomationTests/python_tests/SETUP_GUIDE.md)

## 👥 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Follow the coding standards in [CLAUDE.md](CLAUDE.md)
4. Commit your changes (`git commit -m 'Add AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

## 📞 Contact

**QA Lead:** Bilal
**Framework Version:** 2.0 (Production-Ready)
**Repository:** [https://github.com/m-bilal15/Chic-AI](https://github.com/m-bilal15/Chic-AI)

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Playwright](https://playwright.dev/) - Modern web testing framework
- Powered by [Pytest](https://docs.pytest.org/) - Python testing framework
- Inspired by industry best practices and Page Object Model pattern

---

**Made with ❤️ by Bilal - SQA Lead**

**⭐ Star this repository if you find it helpful!**
