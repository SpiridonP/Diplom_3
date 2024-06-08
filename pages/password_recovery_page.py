from page_locators import locators
from pages.base_page import BasePage
import allure
import data
import time

class RecoveryPassword(BasePage):

    @allure.title('Проверка кнопки "Восстановить пароль')
    @allure.step('Нажать на кнопку "Восстановить пароль"')
    def click_password_recovery(self):
        user_account = self.wait_and_find(locators.RecoveryPasswordLocators.LK)
        user_account.click()
        password_recovery = self.wait_and_find(locators.RecoveryPasswordLocators.PASSWORD_RECOVERY)
        password_recovery.click()
        time.sleep(1)

    @allure.step('Проверка текста страницы восстановления')
    def recovery_page(self):
        self.check(data.ASSERTS.recovery_page)

    @allure.title('Проверка отправки на email')
    @allure.step('Вписать в поле email и нажать на "Восстановить"')
    def send_email_and_click_buttonRecovery(self):
        user_account = self.wait_and_find(locators.RecoveryPasswordLocators.LK)
        user_account.click()
        password_recovery = self.wait_and_find(locators.RecoveryPasswordLocators.PASSWORD_RECOVERY)
        password_recovery.click()
        email_input = self.wait_and_find(locators.RecoveryPasswordLocators.EMAIL_INPUT)
        email_input.send_keys(data.HELPERS.email)
        button_recovery = self.wait_and_find(locators.RecoveryPasswordLocators.BUTTON_RECOVERY)
        button_recovery.click()

    @allure.title('Проверка нового пароля')
    @allure.step('После отправки на email ввести пароль и нажать на иконку глаза"')
    def send_new_password(self):
        user_account = self.wait_and_find(locators.RecoveryPasswordLocators.LK)
        user_account.click()
        password_recovery = self.wait_and_find(locators.RecoveryPasswordLocators.PASSWORD_RECOVERY)
        password_recovery.click()
        email_input = self.wait_and_find(locators.RecoveryPasswordLocators.EMAIL_INPUT)
        email_input.send_keys(data.HELPERS.email)
        time.sleep(3)
        button_recovery = self.wait_and_find(locators.RecoveryPasswordLocators.BUTTON_RECOVERY)
        button_recovery.click()
        time.sleep(3)
        new_password = self.wait_and_find(locators.RecoveryPasswordLocators.PASSWORD_INPUT)
        new_password.send_keys(data.HELPERS.password_new)
        eye = self.wait_and_find(locators.RecoveryPasswordLocators.EYE_BUTTON)
        eye.click()
        time.sleep(3)

    @allure.title('Проверка нового пароля (пароль виден)')
    def check_save(self):
        self.check(data.ASSERTS.save)






