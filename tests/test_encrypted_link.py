from page_forms.encrypted_page import EncryptedLink
from config import ENCRYPTED_URL


def test_encrypted_link(browser):
    page = EncryptedLink(browser, ENCRYPTED_URL)
    page.open()
    page.do_math_to_click_real_url()
    page.fill_form()
    page.handle_alert()
