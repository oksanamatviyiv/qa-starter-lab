from playwright.sync_api import expect
from .base_page import BasePage


class LoginPage(BasePage):
    URL = "https://the-internet.herokuapp.com/login"

    # Locators (selectors) stored in one place (POM rule)
    USERNAME = "#username"
    PASSWORD = "#password"
    LOGIN_BTN = "button[type='submit']"
    FLASH = "#flash"

    def open_login(self):
        self.open(self.URL)

    def login(self, username: str, password: str):
        self.page.locator(self.USERNAME).fill(username)
        self.page.locator(self.PASSWORD).fill(password)
        self.page.locator(self.LOGIN_BTN).click()

    def assert_success_message(self):
        expect(self.page.locator(self.FLASH)).to_contain_text(
            "You logged into a secure area!"
        )

    def assert_invalid_password(self):
        expect(self.page.locator(self.FLASH)).to_contain_text(
            "Your password is invalid!"
        )
