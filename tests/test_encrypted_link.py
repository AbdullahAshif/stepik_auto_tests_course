from page_forms.encrypted_page import EncryptedLink
from utils.constants import ENCRYPTED_URL


def test_encrypted_link(browser):
    page = EncryptedLink(browser, ENCRYPTED_URL)
    page.open()
    page.do_math_to_click_real_url()
    page.fill_form("Ivan","Petrov", "Smolensk", "Russia")
    page.handle_alert()
