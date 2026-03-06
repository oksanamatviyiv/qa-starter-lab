import pytest
from src.ui.pages.login_page import LoginPage


@pytest.mark.ui
@pytest.mark.smoke
def test_login_success(page):
    login = LoginPage(page)
    login.open_login()
    login.login("tomsmith", "SuperSecretPassword!")
    login.assert_success_message()


@pytest.mark.ui
def test_login_invalid_password(page):
    login = LoginPage(page)
    login.open_login()
    login.login("tomsmith", "wrong-password")
    login.assert_invalid_password()
