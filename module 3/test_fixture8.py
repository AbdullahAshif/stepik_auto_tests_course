import pytest
from selenium.webdriver.common.by import By

url = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1():
    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(url)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(url)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
