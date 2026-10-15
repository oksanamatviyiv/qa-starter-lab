from src.ui.pages.login_page import LoginPage


def test_login_success(page):
    login = LoginPage(page)
    login.open_login()
    login.login("tomsmith", "SuperSecretPassword!")
    login.assert_success_message()


def test_login_invalid_password(page):
    login = LoginPage(page)
    login.open_login()
    login.login("tomsmith", "wrong-password")
    login.assert_invalid_password()
