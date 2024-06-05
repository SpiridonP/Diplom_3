from pages.tape_page import Tape
from data import URLS
import allure

class TestTapeOrder:

    def test_check_order_window(self, driver):
        value = Tape(driver)
        value.open_page(URLS.url)
        value.order_window_check()
        value.check_order_window_text()

    def test_check_users_order(self, driver):
        value = Tape(driver)
        value.open_page(URLS.url)
        value.check_users_order()
        value.check_order_number()