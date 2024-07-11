from selenium.webdriver.common.by import By
from .base_page import BasePage


class BasketPage(BasePage):
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items .row")
    ALERT = (By.CSS_SELECTOR, "div#content_inner p")

    def __init__(self, browser, url):
        super().__init__(browser, url)

    def is_basket_empty(self):
        assert self.is_not_element_present(*self.BASKET_ITEM), \
            "There should be no items in the list"

    def check_basket_alert_message(self, expected_alert):
        alert = self.get_element_text(*self.ALERT)
        assert expected_alert in alert, f"Expected '{expected_alert}' in alert message, got '{alert}'"