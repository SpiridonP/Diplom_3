from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
import allure
import data
import time


class Tape(BasePage):
    ORDER_TAPE = (By.XPATH, './/p[text()="Лента Заказов"]')
    SOME_ORDER = (By.XPATH, ".//ul[@class='OrderFeed_list__OLh59']/li[2]")
    EMAIL_INPUT = (By.NAME, 'name')
    PASSWORD_INPUT = (By.NAME, "Пароль")
    LOG_IN_BUTTON = (By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')
    ACCOUNT = (By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")





    def order_window_check(self):
        tape_button = self.wait_and_find(self.ORDER_TAPE)
        tape_button.click()
        order = self.wait_and_find(self.SOME_ORDER)
        order.click()

    def check_order_window_text(self):
        self.check(data.ASSERTS.done)

    def check_users_order(self):
        button_go_to_account = self.wait_and_find(self.ACCOUNT)
        button_go_to_account.click()
        email = self.wait_and_find(self.EMAIL_INPUT)
        email.send_keys(data.HELPERS.email_for_test)
        password = self.wait_and_find(self.PASSWORD_INPUT)
        password.send_keys(data.HELPERS.password)
        button_log_in = self.wait_and_find(self.LOG_IN_BUTTON)
        button_log_in.click()
        tape_button = self.wait_and_find(self.ORDER_TAPE)
        tape_button.click()

    def check_order_number(self):
        self.check(data.ASSERTS.number)



