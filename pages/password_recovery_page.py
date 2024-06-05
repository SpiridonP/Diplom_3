from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
import allure
import data
import time

class RecoveryPassword(BasePage):
    #LK = (By.CLASS_NAME, 'AppHeader_header__linkText__3q_va ml-2')
    LK = (By.XPATH, './/p[text()="Личный Кабинет"]')
    PASSWORD_RECOVERY = (By.XPATH, './/a[text()="Восстановить пароль"]')
    EMAIL_INPUT = (By.NAME, 'name')
    BUTTON_RECOVERY = (By.XPATH, './/button[text()="Восстановить"]')
    PASSWORD_INPUT = (By.XPATH, './/form/fieldset/div/div/input[@name="Введите новый пароль"]')
    EYE_BUTTON = (By.XPATH, ".//div[contains(@class,'input__icon')]")
    BUTTON_SAVE = (By.XPATH, './/fieldset/button[text()="Сохранить"]')



    def click_password_recovery(self):
        user_account = self.wait_and_find(self.LK)
        user_account.click()
        password_recovery = self.wait_and_find(self.PASSWORD_RECOVERY)
        password_recovery.click()
        time.sleep(1)

    def recovery_page(self):
        self.check(data.ASSERTS.recovery_page)


    def send_email_and_click_buttonRecovery(self):
        user_account = self.wait_and_find(self.LK)
        user_account.click()
        password_recovery = self.wait_and_find(self.PASSWORD_RECOVERY)
        password_recovery.click()
        email_input = self.wait_and_find(self.EMAIL_INPUT)
        email_input.send_keys(data.HELPERS.email)
        button_recovery = self.wait_and_find(self.BUTTON_RECOVERY)
        button_recovery.click()



    def send_new_password(self):
        user_account = self.wait_and_find(self.LK)
        user_account.click()
        password_recovery = self.wait_and_find(self.PASSWORD_RECOVERY)
        password_recovery.click()
        email_input = self.wait_and_find(self.EMAIL_INPUT)
        email_input.send_keys(data.HELPERS.email)
        time.sleep(3)
        button_recovery = self.wait_and_find(self.BUTTON_RECOVERY)
        button_recovery.click()
        time.sleep(3)
        new_password = self.wait_and_find(self.PASSWORD_INPUT)
        new_password.send_keys(data.HELPERS.password_new)
        eye = self.wait_and_find(self.EYE_BUTTON)
        eye.click()
        time.sleep(3)


    def check_save(self):
        self.check(data.ASSERTS.save)






