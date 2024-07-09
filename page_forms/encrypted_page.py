import math
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_forms.base_page import BasePage
from resource.locators import Module1Locators


class EncryptedLink(BasePage):
    def do_math_to_click_real_url(self):
        Math = str(math.ceil(math.pow(math.pi, math.e) * 10000))
        partial_link = self.browser.find_element(By.PARTIAL_LINK_TEXT, Math)
        partial_link.click()

    def fill_form(self):
        input1 = self.browser.find_element(*Module1Locators.FIRST_NAME)
        input1.send_keys("Ivan")
        input2 = self.browser.find_element(*Module1Locators.LAST_NAME)
        input2.send_keys("Petrov")
        input3 = self.browser.find_element(*Module1Locators.CITY_NAME)
        input3.send_keys("Smolensk")
        input4 = self.browser.find_element(*Module1Locators.COUNTRY_NAME)
        input4.send_keys("Russia")
        button = self.browser.find_element(*Module1Locators.SUBMIT_BUTTON)
        button.click()

        # Wait for the alert to appear
        try:
            WebDriverWait(self.browser, 10).until(EC.alert_is_present())
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            alert.accept()
            print(f"Alert Text: {alert_text}")
        except TimeoutException:
            print("No alert present after form submission.")
