from page_locators import locators
from pages.base_page import BasePage
import allure
import data
from seletools.actions import drag_and_drop


class Tape(BasePage):

    @allure.title('Проверка открытия окна заказа')
    @allure.step('В ленте заказов кликнуть на заказ')
    def order_window_check(self):
        tape_button = self.wait_and_find(locators.TapePageLocators.ORDER_TAPE)
        tape_button.click()
        order = self.wait_and_find(locators.TapePageLocators.SOME_ORDER)
        order.click()

    @allure.title('Проверка текста в окне заказа')
    def check_order_window_text(self):
        self.check(data.ASSERTS.done)

    @allure.title('Проверка заказа пользователя в ленте заказа')
    @allure.step('После заказа появляется номер в окне (этот номер отображается в ленте заказа)')
    def check_users_order(self):
        button_go_to_account = self.wait_and_find(locators.AccountLocators.ACCOUNT)
        button_go_to_account.click()
        email = self.wait_and_find(locators.AccountLocators.EMAIL_INPUT)
        email.send_keys(data.HELPERS.email_for_test)
        password = self.wait_and_find(locators.AccountLocators.PASSWORD_INPUT)
        password.send_keys(data.HELPERS.password)
        button_log_in = self.wait_and_find(locators.AccountLocators.LOG_IN_BUTTON)
        button_log_in.click()
        source = self.wait_and_find(locators.TapePageLocators.BULKA)
        target = self.wait_and_find(locators.TapePageLocators.CONSTR)
        drag_and_drop(self.driver, source, target)
        order = self.wait_and_find(locators.MainFunctionalLocators.ORDER_BUTTON)
        order.click()
        exit = self.wait_and_find(locators.MainFunctionalLocators.BUTTON_EXIT)
        exit.click()
        tape_button = self.wait_and_find(locators.TapePageLocators.ORDER_TAPE)
        tape_button.click()
        self.wait_and_find(locators.TapePageLocators.ALL_TIME_COUNTER)

    @allure.title('Проверка номера заказа')
    def check_order_number(self):
        self.check_source(locators.TapePageLocators.ORDERS_NUMBER_TEXT)

    @allure.title('Проверка заказа пользователя в поле "В работе"')
    @allure.step('После заказа перейти в ленту заказов и проверить поле "В работе"')
    def compare_numbers(self):
        button_go_to_account = self.wait_and_find(locators.AccountLocators.ACCOUNT)
        button_go_to_account.click()
        email = self.wait_and_find(locators.AccountLocators.EMAIL_INPUT)
        email.send_keys(data.HELPERS.email_for_test)
        password = self.wait_and_find(locators.AccountLocators.PASSWORD_INPUT)
        password.send_keys(data.HELPERS.password)
        button_log_in = self.wait_and_find(locators.AccountLocators.LOG_IN_BUTTON)
        button_log_in.click()
        source = self.wait_and_find(locators.TapePageLocators.BULKA)
        target = self.wait_and_find(locators.TapePageLocators.CONSTR)
        drag_and_drop(self.driver, source, target)
        order = self.wait_and_find(locators.MainFunctionalLocators.ORDER_BUTTON)
        order.click()
        exit = self.wait_and_find(locators.MainFunctionalLocators.BUTTON_EXIT)
        exit.click()
        tape_button = self.wait_and_find(locators.TapePageLocators.ORDER_TAPE)
        tape_button.click()
        self.wait_and_find(locators.TapePageLocators.ALL_TIME_COUNTER)

    @allure.title('Текст номера заказа')
    def compares(self):
        self.compare(locators.TapePageLocators.TEXT_NUMBER)

    @allure.title('Проверка увеличения числа заказов в поле "Выполнено за все время:"')
    @allure.step('После заказа перейти в ленту заказов и проверить поле "Выполнено за все время:"')
    def increase_all_time(self):
        tape_button = self.wait_and_find(locators.TapePageLocators.ORDER_TAPE)
        tape_button.click()
        first_number = self.wait_and_find(locators.TapePageLocators.ALL_TIME_COUNTER).text
        button_constructor = self.wait_and_find(locators.MainFunctionalLocators.BUTTON_CONSTRUCTOR)
        button_constructor.click()
        button_go_to_account = self.wait_and_find(locators.AccountLocators.ACCOUNT)
        button_go_to_account.click()
        email = self.wait_and_find(locators.AccountLocators.EMAIL_INPUT)
        email.send_keys(data.HELPERS.email_for_test)
        password = self.wait_and_find(locators.AccountLocators.PASSWORD_INPUT)
        password.send_keys(data.HELPERS.password)
        button_log_in = self.wait_and_find(locators.AccountLocators.LOG_IN_BUTTON)
        button_log_in.click()
        source = self.wait_and_find(locators.TapePageLocators.BULKA)
        target = self.wait_and_find(locators.TapePageLocators.CONSTR)
        drag_and_drop(self.driver, source, target)
        order = self.wait_and_find(locators.MainFunctionalLocators.ORDER_BUTTON)
        order.click()
        exit = self.wait_and_find(locators.MainFunctionalLocators.BUTTON_EXIT)
        exit.click()
        tape_button = self.wait_and_find(locators.TapePageLocators.ORDER_TAPE)
        tape_button.click()
        self.wait_and_find(locators.TapePageLocators.ALL_TIME_COUNTER)
        new_number = self.wait_and_find(locators.TapePageLocators.ALL_TIME_COUNTER).text
        self.wait_and_find(locators.TapePageLocators.ALL_TIME_COUNTER)
        self.increase(first_number, new_number)

    @allure.title('Проверка увеличения числа заказов в поле "Выполнено за сегодня:"')
    @allure.step('После заказа перейти в ленту заказов и проверить поле "Выполнено за сегодня:"')
    def increase_today(self):
        tape_button = self.wait_and_find(locators.TapePageLocators.ORDER_TAPE)
        tape_button.click()
        first_number = self.wait_and_find(locators.TapePageLocators.TODAY_COUNTER).text
        button_constructor = self.wait_and_find(locators.MainFunctionalLocators.BUTTON_CONSTRUCTOR)
        button_constructor.click()
        button_go_to_account = self.wait_and_find(locators.AccountLocators.ACCOUNT)
        button_go_to_account.click()
        email = self.wait_and_find(locators.AccountLocators.EMAIL_INPUT)
        email.send_keys(data.HELPERS.email_for_test)
        password = self.wait_and_find(locators.AccountLocators.PASSWORD_INPUT)
        password.send_keys(data.HELPERS.password)
        button_log_in = self.wait_and_find(locators.AccountLocators.LOG_IN_BUTTON)
        button_log_in.click()
        source = self.wait_and_find(locators.TapePageLocators.BULKA)
        target = self.wait_and_find(locators.TapePageLocators.CONSTR)
        drag_and_drop(self.driver, source, target)
        order = self.wait_and_find(locators.MainFunctionalLocators.ORDER_BUTTON)
        order.click()
        exit = self.wait_and_find(locators.MainFunctionalLocators.BUTTON_EXIT)
        exit.click()
        tape_button = self.wait_and_find(locators.TapePageLocators.ORDER_TAPE)
        tape_button.click()
        self.wait_and_find(locators.TapePageLocators.ALL_TIME_COUNTER)
        new_number = self.wait_and_find(locators.TapePageLocators.TODAY_COUNTER).text
        self.wait_and_find(locators.TapePageLocators.TODAY_COUNTER)
        self.increase(first_number, new_number)




