from selenium import webdriver

def test_chrome_launches():
    driver = webdriver.Chrome()

    try:
        driver.get("https://example.com")
        assert "Example Domain" in driver.title
    finally:
        driver.quit()
