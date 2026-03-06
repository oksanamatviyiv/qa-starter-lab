from playwright.sync_api import Page, expect 


class BasePage:
    # Base page object to be inherited by all specific page objects. OOP helps keep common page interactions in one place and promotes code reuse.
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)

    def screenshot(self, path: str):
        self.page.screenshot(path=path, full_page=True)
