from page_forms.main_page import MainPage
from page_forms.basket_page import BasketPage
from page_forms.login_page import LoginPage
import pytest


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    url = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, url)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_should_be_empty()
    basket_page.text_basket_is_empty_should_be_present()


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(sef, browser):
        url = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, url)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        url = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, url)
        page.open()
        page.should_be_login_link()
