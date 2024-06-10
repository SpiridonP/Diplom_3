from pages.password_recovery_page import RecoveryPassword
from data import URLS
import allure


class TestRecovery:

    @allure.title('Проверка нажатия на кнопку "Восстановления пароля"')
    def test_button_recovery_click(self, driver):
        recovery = RecoveryPassword(driver)
        recovery.open_page(URLS.url)
        recovery.click_password_recovery()
        recovery.recovery_page()

    @allure.title('Проверка ввода email и нажатия на "Восстановить"')
    def test_send_email_and_click_buttonRecovery(self, driver):
        value = RecoveryPassword(driver)
        value.open_page(URLS.url)
        value.send_email_and_click_buttonRecovery()
        value.recovery_page()

    @allure.title('Проверка отображения пароля при нажатии на иконку глаза"')
    def test_check_password_not_hide(self, driver):
        value = RecoveryPassword(driver)
        value.open_page(URLS.url)
        value.send_email_and_click_buttonRecovery()
        value.send_new_password()
        value.check_save()
