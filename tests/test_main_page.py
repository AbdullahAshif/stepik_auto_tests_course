from configs.constants import AlertMessages
from page_forms.main_page import MainPage
import pytest


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    main_page = MainPage(browser)
    main_page.open()
    basket_page = main_page.go_to_basket()
    basket_page.is_basket_empty()
    basket_page.check_basket_alert_message(AlertMessages.BASKET_EMPTY.value)


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        main_page = MainPage(browser)
        main_page.open()
        login_page = main_page.go_to_login_page()
        login_page.login_page_is_present()

    def test_guest_should_see_login_link(self, browser):
        main_page = MainPage(browser)
        main_page.open()
        main_page.login_link_is_present()
