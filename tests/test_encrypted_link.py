from page_forms.encrypted_page import EncryptedLink
from configuration import ENCRYPTED_URL


def test_encrypted_link(browser):
    encrypted_page = EncryptedLink(browser, ENCRYPTED_URL)
    encrypted_page.open()
    encrypted_page.do_math_to_click_real_url()
    encrypted_page.fill_form("Ivan","Petrov", "Smolensk", "Russia")
    encrypted_page.handle_alert()
