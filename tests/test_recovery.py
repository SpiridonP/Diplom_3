from pages.password_recovery_page import RecoveryPassword
from data import URLS
import allure


class TestRecovery:
    def test_button_recovery_click(self, driver):
        recovery = RecoveryPassword(driver)
        recovery.open_page(URLS.url)
        recovery.click_password_recovery()
        recovery.recovery_page()

    def test_send_email_and_click_buttonRecovery(self, driver):
        value = RecoveryPassword(driver)
        value.open_page(URLS.url)
        value.send_email_and_click_buttonRecovery()
        value.recovery_page()


    def test_check_password_not_hide(self, driver):
        value = RecoveryPassword(driver)
        value.open_page(URLS.url)
        value.send_email_and_click_buttonRecovery()
        value.send_new_password()
        value.check_save()
