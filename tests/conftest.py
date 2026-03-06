import os  # for environment variable handling
import pathlib  # for file path handling
import pytest, pytest_html  # for embedding screenshots in test reports

from config import API_BASE_URL, UI_BASE_URL, DEFAULT_TIMEOUT
from src.api.client import APIClient
from playwright.sync_api import sync_playwright


# ---------- API fixture ----------
@pytest.fixture(scope="session")
# Session-scoped fixture to create a single API client instance for all API tests.
def api_client():
    return APIClient(API_BASE_URL, timeout=DEFAULT_TIMEOUT)


# ---------- UI fixtures ----------
@pytest.fixture(scope="session")
def browser():
    # Use HEADLESS env var to control whether tests run in headless mode; default to headless for CI.
    headless = os.getenv("HEADLESS", "1") == "1"
    with sync_playwright() as p:
        b = p.chromium.launch(headless=headless)
        yield b
        b.close()


@pytest.fixture
def page(browser):
    context = browser.new_context(
        base_url=UI_BASE_URL, viewport={"width": 1280, "height": 720}
    )
    page = context.new_page()
    yield page
    context.close()


# ---------- Screenshot on UI failure ----------
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture Playwright page screenshot on test failure and embed in HTML report."""
    outcome = yield
    rep = outcome.get_result()

    # Only capture during test execution ("call" stage)
    if rep.when == "call" and rep.failed:
        # Try to get Playwright page fixture
        page = item.funcargs.get("page")
        if page is not None:
            try:
                png = page.screenshot()
                extra = getattr(rep, "extra", [])
                extra.append(pytest_html.extras.png(png))
                rep.extra = extra
            except Exception as e:
                # Silent fail if screenshot can't be taken
                pass
