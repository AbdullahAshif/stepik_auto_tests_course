from page_forms.product_page import ProductPage
from page_forms.login_page import LoginPage
from page_forms.basket_page import BasketPage
from utils.constants import LOGIN_URL, PROMO_URLS, PRODUCT_URL, LOGIN_TO_PRODUCT_URL
import time
import pytest


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        register_page = LoginPage(browser, LOGIN_URL)
        register_page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "kdoemo38hedk84"
        register_page.register_new_user(email, password)
        register_page.is_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        browser.delete_all_cookies()
        page = ProductPage(browser, PRODUCT_URL)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.check_alert_product_added(page.get_product_name())
        page.check_alert_sum_in_basket(page.get_price())

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, PRODUCT_URL)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.need_review
@pytest.mark.parametrize('link', PROMO_URLS)
def test_guest_can_add_product_to_basket(browser, link):
    browser.delete_all_cookies()
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_alert_product_added(page.get_product_name())
    page.check_alert_sum_in_basket(page.get_price())


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    browser.delete_all_cookies()
    page = ProductPage(browser, PRODUCT_URL)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_basket_empty()
    basket_page.check_basket_alert_message('basket is empty')


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, LOGIN_TO_PRODUCT_URL)
    page.open()
    page.go_to_login_page()


@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, PRODUCT_URL)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_URL)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_URL)
    page.open()
    page.add_to_basket()
    page.should_disappear_success_message()


@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, LOGIN_TO_PRODUCT_URL)
    page.open()
    page.login_link_is_present()
