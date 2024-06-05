from pages.personal_account_page import Account
from data import URLS
import allure


class TestForLogIn:

    def test_log_in(self, driver):
        value = Account(driver)
        value.open_page(URLS.url)
        value.log_in()
        value.check_text_profile()

    def test_log_out(self, driver):
        value = Account(driver)
        value.open_page(URLS.url)
        value.log_out()
        value.check_page()

    def test_history_orders(self, driver):
        value = Account(driver)
        value.open_page(URLS.url)
        value.orders_history()
        value.check_url()





