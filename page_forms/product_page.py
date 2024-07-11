import math
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from page_forms.base_page import BasePage


class ProductPage(BasePage):
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    ALERT = (By.CSS_SELECTOR, "div.alertinner")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")

    def __init__(self, browser, url):
        super().__init__(browser, url)

    def get_product_name(self):
        return self.get_element_text(*self.PRODUCT_NAME)

    def get_price(self):
        return self.get_element_text(*self.PRODUCT_PRICE)

    def check_alert_product_added(self, product_name):
        expected_alert = product_name + ' has been added to your basket.'
        alert = self.find_elements(*self.ALERT)[0].text
        assert expected_alert in alert, f"Should be '{expected_alert}' in alert:'{alert}'"

    def check_alert_sum_in_basket(self, price):
        expected_alert = 'Your basket total is now ' + price
        alert = self.find_elements(*self.ALERT)[2].text
        assert expected_alert in alert, f"Should be '{expected_alert}' in alert:'{alert}'"

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*self.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            self.handle_alert()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*self.SUCCESS_MESSAGE), \
            "Success message should not disappear"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*self.SUCCESS_MESSAGE), \
            "Success message should disappear"
