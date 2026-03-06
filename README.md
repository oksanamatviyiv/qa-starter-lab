# QA Starter Lab

A modern test automation framework using Pytest for both API and UI testing with Playwright.

## Project Structure

```
qa-starter-lab/
├── src/
│   ├── api/           # API client and utilities
│   │   └── client.py
│   └── ui/
│       └── pages/     # Page Object Models for UI tests
├── tests/
│   ├── api/           # API test cases
│   ├── ui/            # UI test cases (Playwright)
│   └── conftest.py    # Pytest fixtures and hooks
├── config.py          # Configuration (base URLs, timeouts, etc.)
├── pytest.ini         # Pytest configuration with markers
├── requirements.txt   # Python dependencies
└── reports/           # Generated test reports (HTML, XML)
```

## Setup Instructions

### 1. Create and Activate Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
playwright install  # Install browser binaries for Playwright
```

### 3. Verify Installation
```bash
pytest --version
playwright --version
```

## Running Tests

### Run All Tests
```bash
pytest
```

### Run Tests by Marker
```bash
# API tests only
pytest -m api

# UI tests only
pytest -m ui

# Smoke tests
pytest -m smoke
```

### Run with HTML Report
```bash
pytest --html=reports/report.html --self-contained-html
```

### Run with Verbose Output
```bash
pytest -v
```

### Run Specific Test File
```bash
pytest tests/api/test_health.py
pytest tests/ui/test_login_ui.py
```

## Framework Features

### API Testing
- **Client**: `src/api/client.py` provides an HTTP client wrapper using `requests`
- **Tests**: Located in `tests/api/`
- **Base URL**: Configured in `config.py` (JSONPlaceholder by default)

### UI Testing
- **Framework**: Playwright (sync API)
- **Pattern**: Page Object Model (POM) for maintainability
- **Pages**: UI page classes in `src/ui/pages/`
- **Features**:
  - Screenshots on test failure (auto-embedded in HTML report)
  - Configurable headless/headed mode via `HEADLESS` env var
  - Customizable viewport and timeouts

### Fixtures (conftest.py)
- `api_client`: Session-scoped API client
- `browser`: Session-scoped Playwright browser instance
- `page`: Browser page context with viewport settings
- `pytest_runtest_makereport`: Hook to capture screenshots on failure

### Configuration (config.py)
- `API_BASE_URL`: API testing endpoint
- `UI_BASE_URL`: Web application under test
- `DEFAULT_TIMEOUT`: Default wait timeout for tests

## Markers

Tests are organized using pytest markers:
```bash
@pytest.mark.api      # API tests
@pytest.mark.ui       # UI tests
@pytest.mark.smoke    # Smoke/critical path tests
```

## Environment Variables

- `HEADLESS=0`: Run browser in headed mode (default: headless)
- `UI_BASE_URL`: Override base URL for UI tests
- `API_BASE_URL`: Override base URL for API tests

Example:
```bash
HEADLESS=0 pytest tests/ui/test_login_ui.py -v -s
```

## Implementation Status

- ✅ API test framework with client and fixtures
- ✅ UI test framework using Playwright with POM
- ✅ Automated screenshot capture on test failures
- ✅ HTML and XML report generation
- ✅ Pytest markers and fixture organization
- ✅ Configuration management
- ✅ Virtual environment setup
