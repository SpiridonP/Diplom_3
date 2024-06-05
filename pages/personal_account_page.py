from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import allure
import data
import time


class Account(BasePage):
    ACCOUNT = (By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    LK = (By.LINK_TEXT, "Личный Кабинет")
    EMAIL_INPUT = (By.NAME, 'name')
    PASSWORD_INPUT = (By.NAME, "Пароль")
    LOG_IN_BUTTON = (By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')
    ORDERS_HISTORY = (By.XPATH, ".//a[text()='История заказов']")
    LOG_OUT = (By.XPATH, ".//button[text()='Выход']")




    def log_in(self):
        button_go_to_account = self.wait_and_find(self.ACCOUNT)
        button_go_to_account.click()
        email = self.wait_and_find(self.EMAIL_INPUT)
        email.send_keys(data.HELPERS.email_for_test)
        password = self.wait_and_find(self.PASSWORD_INPUT)
        password.send_keys(data.HELPERS.password)
        button_log_in = self.wait_and_find(self.LOG_IN_BUTTON)
        button_log_in.click()
        button_personal_account = self.wait_and_find(self.LK)
        button_personal_account.click()
        time.sleep(3)

    def check_text_profile(self):
        self.check(data.ASSERTS.profile)

    def log_out(self):
        button_go_to_account = self.wait_and_find(self.ACCOUNT)
        button_go_to_account.click()
        email = self.wait_and_find(self.EMAIL_INPUT)
        email.send_keys(data.HELPERS.email_for_test)
        password = self.wait_and_find(self.PASSWORD_INPUT)
        password.send_keys(data.HELPERS.password)
        button_log_in = self.wait_and_find(self.LOG_IN_BUTTON)
        button_log_in.click()
        button_personal_account = self.wait_and_find(self.LK)
        button_personal_account.click()
        history_orders_button = self.wait_and_find(self.LOG_OUT)
        history_orders_button.click()
        time.sleep(3)



    def check_page(self):
        self.check(data.ASSERTS.enter)


    def orders_history(self):
        button_go_to_account = self.wait_and_find(self.ACCOUNT)
        button_go_to_account.click()
        email = self.wait_and_find(self.EMAIL_INPUT)
        email.send_keys(data.HELPERS.email_for_test)
        password = self.wait_and_find(self.PASSWORD_INPUT)
        password.send_keys(data.HELPERS.password)
        button_log_in = self.wait_and_find(self.LOG_IN_BUTTON)
        button_log_in.click()
        button_personal_account = self.wait_and_find(self.LK)
        button_personal_account.click()
        history_orders_button = self.wait_and_find(self.ORDERS_HISTORY)
        history_orders_button.click()
        time.sleep(3)


    def check_url_page(self):
        self.check_url()

