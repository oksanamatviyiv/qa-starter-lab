from playwright.sync_api import expect  # type: ignore[import-not-found]

from .base_page import BasePage


class LoginPage(BasePage):
    URL = "https://the-internet.herokuapp.com/login"

    # Locators (selectors) stored in one place (POM rule)
    USERNAME = "#username"
    PASSWORD = "#password"
    LOGIN_BTN = "button[type='submit']"

    def open_login(self):
        # Avoid waiting on the demo site's external tracking script.
        self.page.route("**/js/vendor/298279967.js", lambda route: route.abort())
        self.page.goto(
        self.URL, wait_until="domcontentloaded", timeout=60_000
        )

    def login(self, username: str, password: str):
        self.page.locator(self.USERNAME).fill(username)
        self.page.locator(self.PASSWORD).fill(password)
        with self.page.expect_navigation(wait_until="commit", timeout=60_000):
            self.page.locator(self.LOGIN_BTN).click(no_wait_after=True)

    def assert_success_message(self):
        expect(self.page).to_have_url("https://the-internet.herokuapp.com/secure")

    def assert_invalid_password(self):
        expect(self.page.locator("#flash")).to_contain_text(
            "Your password is invalid!"
        )
