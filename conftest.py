import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from utils.constants import Browser


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default=Browser.CHROME.value,
                     help="Choose browser: chrome or firefox")
    parser.addoption("--language", action="store", default="en",
                     help="Choose language: en or other")


@pytest.fixture(scope="session")
def browser(request):
    def browser(request):
        browser_name = request.config.getoption("browser_name")
        user_language = request.config.getoption("language")

        if browser_name == Browser.CHROME.value:
            options = ChromeOptions()
            options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
            driver = webdriver.Chrome(options=options)
        elif browser_name == Browser.FIREFOX.value:
            options = FirefoxOptions()
            options.set_preference("intl.accept_languages", user_language)
            driver = webdriver.Firefox(options=options)
        else:
            raise pytest.UsageError("--browser_name should be chrome or firefox")

        yield driver
        driver.quit()
