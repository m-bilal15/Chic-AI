# CHIC-AI Test Automation - Setup Guide

**Created:** February 12, 2026
**For:** New team members, CI/CD setup, fresh installations

---

## 📋 Prerequisites

### Required Software:
- **Python 3.9+** ([Download](https://www.python.org/downloads/))
- **Git** ([Download](https://git-scm.com/downloads))
- **Node.js** (for running the app) ([Download](https://nodejs.org/))
- **Code Editor** (VS Code recommended)

### Verify Installation:
```bash
python --version    # Should be 3.9 or higher
git --version
node --version
```

---

## 🚀 Quick Start (5 Minutes)

### 1. Clone Repository
```bash
git clone <repository-url>
cd Chic-AI
```

### 2. Set Up Python Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
cd AutomationTests/python_tests
pip install -r requirements.txt
```

### 4. Install Playwright Browsers
```bash
playwright install chromium
```

### 5. Configure Environment
```bash
# Copy example .env file
cp .env.example .env

# Edit .env and add your credentials
# Windows: notepad .env
# Mac/Linux: nano .env
```

### 6. Run Tests
```bash
# Run all tests
python run_all_tests.py

# Or use pytest
pytest

# Run specific test
pytest testcases/TC_LOGIN_001/test_script.py
```

**✅ You're ready to go!**

---

## 📁 Project Structure

```
Chic-AI/
├── .gitignore              # Git ignore rules
├── CLAUDE.md               # Testing standards
├── AutomationTests/
│   ├── SETUP_GUIDE.md      # This file
│   ├── STRUCTURE_ANALYSIS_AND_IMPROVEMENTS.md
│   └── python_tests/
│       ├── requirements.txt     # Python dependencies
│       ├── pytest.ini           # Pytest configuration
│       ├── conftest.py          # Pytest fixtures
│       ├── .env.example         # Environment template
│       ├── .env                 # Your config (gitignored)
│       ├── config/
│       │   └── config.ini       # Multi-environment config
│       ├── pages/               # Page Object Model
│       ├── utils/               # Helper functions
│       ├── test_data/           # Test data files
│       ├── testcases/           # Test scripts
│       └── results/             # Test results
```

---

## 🔧 Detailed Setup

### Step 1: Python Virtual Environment

**Why?** Isolates project dependencies from system Python.

```bash
# Create
python -m venv venv

# Activate
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

# Verify
which python               # Should show venv path

# Deactivate (when done)
deactivate
```

---

### Step 2: Install Dependencies

```bash
cd AutomationTests/python_tests

# Install all dependencies
pip install -r requirements.txt

# Verify installation
pip list

# Install Playwright browsers
playwright install chromium

# Optional: Install all browsers
playwright install
```

**Dependencies Installed:**
- ✅ Pytest (testing framework)
- ✅ Playwright (browser automation)
- ✅ pytest-html (HTML reports)
- ✅ pytest-xdist (parallel execution)
- ✅ python-dotenv (environment variables)
- ✅ And more...

---

### Step 3: Configuration

#### 3.1 Environment Variables (.env)

```bash
# Copy example file
cp .env.example .env

# Edit with your values
```

**Important Variables:**
```env
ENVIRONMENT=dev
TEST_EMAIL=bilal@test.com
TEST_PASSWORD=ValidPass@123
BASE_URL=http://localhost:5173
HEADLESS=false
```

#### 3.2 Config File (config/config.ini)

Supports multiple environments:
- **dev** - Local development
- **staging** - Staging server
- **production** - Production (read-only tests)
- **ci** - CI/CD pipeline

**Switch environments:**
```bash
# Set in .env
ENVIRONMENT=staging
```

---

### Step 4: Running Tests

#### 4.1 Run All Tests
```bash
# Using run_all_tests.py
python run_all_tests.py

# Using pytest
pytest

# Verbose mode
pytest -v

# With HTML report
pytest --html=results/report.html
```

#### 4.2 Run Specific Tests
```bash
# Single test file
pytest testcases/TC_LOGIN_001/test_script.py

# Tests by marker
pytest -m smoke              # Smoke tests only
pytest -m critical           # Critical tests only
pytest -m "smoke or critical"  # Smoke OR critical

# Tests by name
pytest -k "login"            # All tests with "login" in name
pytest -k "TC_LOGIN_001"     # Specific test case
```

#### 4.3 Parallel Execution
```bash
# Run tests in parallel (4 workers)
pytest -n 4

# Auto-detect number of CPUs
pytest -n auto
```

#### 4.4 Stop on First Failure
```bash
pytest -x                    # Stop on first failure
pytest --maxfail=3           # Stop after 3 failures
```

---

## 📊 Viewing Results

### Test Reports
```
results/
├── report.html              # Open in browser
├── SUMMARY.md               # Markdown summary
├── SUMMARY.json             # JSON summary
├── Passed/                  # Passed tests
├── Failed/                  # Failed tests
├── failures/                # Auto-screenshots
└── logs/                    # Log files
```

**View HTML Report:**
```bash
# Open in browser
start results/report.html           # Windows
open results/report.html            # Mac
xdg-open results/report.html        # Linux
```

---

## 🐛 Troubleshooting

### Issue: "playwright: command not found"
**Solution:**
```bash
# Ensure you're in virtual environment
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

# Reinstall playwright
pip install playwright
playwright install chromium
```

---

### Issue: "ModuleNotFoundError: No module named 'xyz'"
**Solution:**
```bash
# Activate virtual environment first
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

### Issue: Tests fail with "Cannot find page"
**Solution:**
```bash
# 1. Check if app is running
# Navigate to http://localhost:5173

# 2. Start the app
cd <app-directory>
npm install
npm run dev

# 3. Update BASE_URL in .env if different port
```

---

### Issue: "Permission denied" on Linux/Mac
**Solution:**
```bash
# Make scripts executable
chmod +x run_all_tests.py
chmod +x venv/bin/activate
```

---

## 🎯 Best Practices

### 1. **Always Use Virtual Environment**
```bash
# Activate before working
source venv/bin/activate
```

### 2. **Pull Latest Code**
```bash
git pull origin main
pip install -r requirements.txt  # Update dependencies
```

### 3. **Check Evidence Before Reporting**
- Always review screenshots in `results/failures/`
- Watch videos in `results/videos/`
- Read test reports in `results/Passed/` or `results/Failed/`

### 4. **Keep .env Private**
- ❌ NEVER commit .env to git
- ✅ Use .env.example as template
- ✅ Share credentials securely (password manager)

### 5. **Clean Results Periodically**
```bash
# Results can get large - clean old results
rm -rf results/Passed/*
rm -rf results/Failed/*
rm -rf results/failures/*
```

---

## 🔐 Security Notes

### Sensitive Files (Never Commit):
- ❌ `.env` (contains credentials)
- ❌ `auth.json` (authentication tokens)
- ❌ `results/` (may contain PII in screenshots)
- ❌ `*.log` (may contain sensitive data)

**These are automatically ignored by `.gitignore`**

---

## 📚 Additional Resources

### Documentation:
- **CLAUDE.md** - Testing standards and guidelines
- **STRUCTURE_ANALYSIS_AND_IMPROVEMENTS.md** - Framework improvements
- **README.md** - Project overview

### External Links:
- [Playwright Docs](https://playwright.dev/python/)
- [Pytest Docs](https://docs.pytest.org/)
- [Python Dotenv](https://pypi.org/project/python-dotenv/)

---

## 🆘 Getting Help

### Common Commands Reference:
```bash
# Setup
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install chromium

# Run Tests
pytest                          # All tests
pytest -v                       # Verbose
pytest -m smoke                 # Smoke tests
pytest -n auto                  # Parallel
pytest --html=results/report.html  # HTML report

# Debug
pytest -v --tb=long            # Full traceback
pytest -s                      # Show print statements
pytest --pdb                   # Enter debugger on failure

# Clean Up
deactivate                     # Exit virtual environment
rm -rf results/Passed/*        # Clean results
```

---

## ✅ Verification Checklist

After setup, verify everything works:

- [ ] Virtual environment activated
- [ ] `pip list` shows playwright, pytest
- [ ] `playwright --version` works
- [ ] `.env` file created with credentials
- [ ] App running on http://localhost:5173
- [ ] `pytest --collect-only` shows 50 tests
- [ ] `pytest -m smoke` runs successfully
- [ ] HTML report generated in `results/report.html`

---

**Setup Complete!** 🎉

**Next Steps:**
1. Read **CLAUDE.md** for testing standards
2. Review **STRUCTURE_ANALYSIS_AND_IMPROVEMENTS.md** for framework details
3. Start running tests!

---

**Questions?** Contact QA Lead Bilal or check documentation.
