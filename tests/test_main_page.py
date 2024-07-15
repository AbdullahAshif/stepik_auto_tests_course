from page_forms.main_page import MainPage
from page_forms.basket_page import BasketPage
from page_forms.login_page import LoginPage
from utils.constants import BASE_URL
import pytest


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, BASE_URL)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_basket_empty()
    basket_page.check_basket_alert_message('basket is empty')


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(sef, browser):
        page = MainPage(browser, BASE_URL)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.login_page_is_present()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, BASE_URL)
        page.open()
        page.login_link_is_present()
