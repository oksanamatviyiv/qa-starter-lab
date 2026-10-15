# QA Starter Lab

A small test automation project using Pytest for API tests and Playwright for UI
tests. The tests use the public JSONPlaceholder API and The Internet demo site,
so running them requires internet access and depends on those services being
available.

## Project Structure

```text
qa-starter-lab/
├── src/
│   ├── api/
│   │   └── client.py          # Requests-based API client
│   └── ui/pages/
│       ├── base_page.py       # Shared Playwright page behavior
│       └── login_page.py      # Login page object
├── tests/
│   ├── api/                   # API tests
│   ├── ui/                    # Browser UI tests
│   └── conftest.py            # Shared fixtures and failure-report hook
├── config.py                  # Service URLs and API request timeout
├── pytest.ini                 # Test discovery, markers, and report options
├── requirements.txt           # Python dependencies
└── .gitignore                 # Excludes local and generated files
```

Pytest creates `reports/report.html` and `reports/report.xml` when tests run.
These generated reports are ignored by Git.

## Setup

Create and activate a virtual environment, then install the project
dependencies and Chromium:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
playwright install chromium
```

On Windows, activate the environment with `.venv\Scripts\activate` instead.

Check the installation:

```bash
python -m pytest --version
playwright --version
```

## Running Tests

Run the full suite (HTML and JUnit XML reports are enabled in `pytest.ini`):

```bash
pytest
```

Run API or smoke tests by marker:

```bash
pytest -m api
pytest -m smoke
```

Run the UI tests by file:

```bash
pytest tests/ui/test_login_ui.py
```

The `ui` marker is registered in `pytest.ini`, but the current UI tests are not
tagged with it, so use the file path rather than `pytest -m ui`.

Useful options:

```bash
pytest -v
pytest tests/api/test_health.py
pytest --html=reports/report.html --self-contained-html
```

## Configuration

Edit `config.py` to change:

- `API_BASE_URL`: API test service URL (JSONPlaceholder by default).
- `UI_BASE_URL`: UI test site base URL (The Internet by default).
- `DEFAULT_TIMEOUT`: timeout, in seconds, for API requests.

The UI browser fixture launches Chromium headlessly by default. Set
`HEADLESS=0` to run it in headed mode:

```bash
HEADLESS=0 pytest tests/ui/test_login_ui.py
```

`API_BASE_URL` and `UI_BASE_URL` are Python constants, not environment-variable
overrides.

## Test Framework

- `api_client` is a session-scoped fixture that uses the configured API URL and
  request timeout.
- `browser` is a session-scoped Chromium instance.
- `page` creates a fresh browser context and page for each test, with a
  1280 x 720 viewport and the configured UI base URL.
- UI page objects live in `src/ui/pages/`.
- On a failed test call, `tests/conftest.py` attempts to attach a screenshot to
  the HTML report. If capture fails, pytest emits a warning.
- Pytest markers `api`, `ui`, and `smoke` are registered in `pytest.ini`.
