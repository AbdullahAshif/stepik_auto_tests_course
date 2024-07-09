from page_forms.encrypted_page import EncryptedLink


def test_encrypted_link(browser):
    url = "http://suninjuly.github.io/find_link_text.html"
    page = EncryptedLink(browser, url)
    page.open()
    page.do_math_to_click_real_url()
    page.fill_form()
