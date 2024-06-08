from pages.base_page import BasePage
from page_locators import locators
import allure
import data
import time


class Account(BasePage):

    @allure.title('Проверка входа на сайт')
    @allure.step('Ввести данные и нажать на "Войти"')
    def log_in(self):
        button_go_to_account = self.wait_and_find(locators.AccountLocators.ACCOUNT)
        button_go_to_account.click()
        email = self.wait_and_find(locators.AccountLocators.EMAIL_INPUT)
        email.send_keys(data.HELPERS.email_for_test)
        password = self.wait_and_find(locators.AccountLocators.PASSWORD_INPUT)
        password.send_keys(data.HELPERS.password)
        button_log_in = self.wait_and_find(locators.AccountLocators.LOG_IN_BUTTON)
        button_log_in.click()
        button_personal_account = self.wait_and_find(locators.AccountLocators.LK)
        button_personal_account.click()
        self.wait_and_find(locators.AccountLocators.SAVE)

    @allure.title('Проверка текста в личном кабинете')
    def check_text_profile(self):
        self.check(data.ASSERTS.profile)

    @allure.title('Проверка выхода')
    @allure.step('В личном кабинете нажать на "Выйти"')
    def log_out(self):
        button_go_to_account = self.wait_and_find(locators.AccountLocators.ACCOUNT)
        button_go_to_account.click()
        email = self.wait_and_find(locators.AccountLocators.EMAIL_INPUT)
        email.send_keys(data.HELPERS.email_for_test)
        password = self.wait_and_find(locators.AccountLocators.PASSWORD_INPUT)
        password.send_keys(data.HELPERS.password)
        button_log_in = self.wait_and_find(locators.AccountLocators.LOG_IN_BUTTON)
        button_log_in.click()
        button_personal_account = self.wait_and_find(locators.AccountLocators.LK)
        button_personal_account.click()
        out = self.wait_and_find(locators.AccountLocators.LOG_OUT)
        out.click()
        self.wait_and_find(locators.AccountLocators.EMAIL_INPUT)

    @allure.title('Проверка текста страницы после выхода')
    def check_page(self):
        self.check(data.ASSERTS.enter)

    @allure.title('Проверка перехода на страницу истории заказов')
    @allure.step('В личном кабинете нажать на "История заказов"')
    def orders_history(self):
        button_go_to_account = self.wait_and_find(locators.AccountLocators.ACCOUNT)
        button_go_to_account.click()
        email = self.wait_and_find(locators.AccountLocators.EMAIL_INPUT)
        email.send_keys(data.HELPERS.email_for_test)
        password = self.wait_and_find(locators.AccountLocators.PASSWORD_INPUT)
        password.send_keys(data.HELPERS.password)
        button_log_in = self.wait_and_find(locators.AccountLocators.LOG_IN_BUTTON)
        button_log_in.click()
        button_personal_account = self.wait_and_find(locators.AccountLocators.LK)
        button_personal_account.click()
        history_orders_button = self.wait_and_find(locators.AccountLocators.ORDERS_HISTORY)
        history_orders_button.click()

    @allure.title('Проверка url страницы')
    def check_url_page(self):
        self.check_url()

