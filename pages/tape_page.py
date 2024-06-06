from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure
import data
from seletools.actions import drag_and_drop


class Tape(BasePage):
    ORDER_TAPE = (By.XPATH, './/p[text()="Лента Заказов"]')
    SOME_ORDER = (By.XPATH, ".//ul[@class='OrderFeed_list__OLh59']/li[2]")
    EMAIL_INPUT = (By.NAME, 'name')
    PASSWORD_INPUT = (By.NAME, "Пароль")
    LOG_IN_BUTTON = (By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')
    ACCOUNT = (By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    ALL_TIME_COUNTER = (By.XPATH, '//p[text()="Выполнено за все время:"]/../p[contains(@class,"OrderFeed_number")]')
    TODAY_COUNTER = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/../p[contains(@class,"OrderFeed_number")]')
    BULKA = (By.XPATH, ".//p[contains(text(), 'Краторная булка N-200i')]")
    CONSTR = (By.XPATH, ".//section[contains(@class, 'BurgerConstructor_basket')]")
    ORDERS_NUMBER_TEXT = (By.XPATH, '//li[1]//p[@class="text text_type_digits-default"]')
    TEXT_NUMBER = (By.XPATH, './/li[@class="text text_type_digits-default mb-2"]')
    ORDER_BUTTON = (By.XPATH, './/button[text()="Оформить заказ"]')
    BUTTON_EXIT = (By.XPATH, './/button[@type="button"]')
    BUTTON_CONSTRUCTOR = (By.LINK_TEXT, "Конструктор")

    @allure.title('Проверка открытия окна заказа')
    @allure.step('В ленте заказов кликнуть на заказ')
    def order_window_check(self):
        tape_button = self.wait_and_find(self.ORDER_TAPE)
        tape_button.click()
        order = self.wait_and_find(self.SOME_ORDER)
        order.click()

    @allure.title('Проверка текста в окне заказа')
    def check_order_window_text(self):
        self.check(data.ASSERTS.done)

    @allure.title('Проверка заказа пользователя в ленте заказа')
    @allure.step('После заказа появляется номер в окне (этот номер отображается в ленте заказа)')
    def check_users_order(self):
        button_go_to_account = self.wait_and_find(self.ACCOUNT)
        button_go_to_account.click()
        email = self.wait_and_find(self.EMAIL_INPUT)
        email.send_keys(data.HELPERS.email_for_test)
        password = self.wait_and_find(self.PASSWORD_INPUT)
        password.send_keys(data.HELPERS.password)
        button_log_in = self.wait_and_find(self.LOG_IN_BUTTON)
        button_log_in.click()
        source = self.wait_and_find(self.BULKA)
        target = self.wait_and_find(self.CONSTR)
        drag_and_drop(self.driver, source, target)
        order = self.wait_and_find(self.ORDER_BUTTON)
        order.click()
        exit = self.wait_and_find(self.BUTTON_EXIT)
        exit.click()
        tape_button = self.wait_and_find(self.ORDER_TAPE)
        tape_button.click()
        self.wait_and_find(self.ALL_TIME_COUNTER)

    @allure.title('Проверка номера заказа')
    def check_order_number(self):
        self.check_source(self.ORDERS_NUMBER_TEXT)

    @allure.title('Проверка заказа пользователя в поле "В работе"')
    @allure.step('После заказа перейти в ленту заказов и проверить поле "В работе"')
    def compare_numbers(self):
        button_go_to_account = self.wait_and_find(self.ACCOUNT)
        button_go_to_account.click()
        email = self.wait_and_find(self.EMAIL_INPUT)
        email.send_keys(data.HELPERS.email_for_test)
        password = self.wait_and_find(self.PASSWORD_INPUT)
        password.send_keys(data.HELPERS.password)
        button_log_in = self.wait_and_find(self.LOG_IN_BUTTON)
        button_log_in.click()
        source = self.wait_and_find(self.BULKA)
        target = self.wait_and_find(self.CONSTR)
        drag_and_drop(self.driver, source, target)
        order = self.wait_and_find(self.ORDER_BUTTON)
        order.click()
        exit = self.wait_and_find(self.BUTTON_EXIT)
        exit.click()
        tape_button = self.wait_and_find(self.ORDER_TAPE)
        tape_button.click()
        self.wait_and_find(self.ALL_TIME_COUNTER)

    @allure.title('Текст номера заказа')
    def compares(self):
        self.compare(self.TEXT_NUMBER)

    @allure.title('Проверка увеличения числа заказов в поле "Выполнено за все время:"')
    @allure.step('После заказа перейти в ленту заказов и проверить поле "Выполнено за все время:"')
    def increase_all_time(self):
        tape_button = self.wait_and_find(self.ORDER_TAPE)
        tape_button.click()
        first_number = self.wait_and_find(self.ALL_TIME_COUNTER).text
        button_constructor = self.wait_and_find(self.BUTTON_CONSTRUCTOR)
        button_constructor.click()
        button_go_to_account = self.wait_and_find(self.ACCOUNT)
        button_go_to_account.click()
        email = self.wait_and_find(self.EMAIL_INPUT)
        email.send_keys(data.HELPERS.email_for_test)
        password = self.wait_and_find(self.PASSWORD_INPUT)
        password.send_keys(data.HELPERS.password)
        button_log_in = self.wait_and_find(self.LOG_IN_BUTTON)
        button_log_in.click()
        source = self.wait_and_find(self.BULKA)
        target = self.wait_and_find(self.CONSTR)
        drag_and_drop(self.driver, source, target)
        order = self.wait_and_find(self.ORDER_BUTTON)
        order.click()
        exit = self.wait_and_find(self.BUTTON_EXIT)
        exit.click()
        tape_button = self.wait_and_find(self.ORDER_TAPE)
        tape_button.click()
        self.wait_and_find(self.ALL_TIME_COUNTER)
        new_number = self.wait_and_find(self.ALL_TIME_COUNTER).text
        self.wait_and_find(self.ALL_TIME_COUNTER)
        self.increase(first_number, new_number)

    @allure.title('Проверка увеличения числа заказов в поле "Выполнено за сегодня:"')
    @allure.step('После заказа перейти в ленту заказов и проверить поле "Выполнено за сегодня:"')
    def increase_today(self):
        tape_button = self.wait_and_find(self.ORDER_TAPE)
        tape_button.click()
        first_number = self.wait_and_find(self.TODAY_COUNTER).text
        button_constructor = self.wait_and_find(self.BUTTON_CONSTRUCTOR)
        button_constructor.click()
        button_go_to_account = self.wait_and_find(self.ACCOUNT)
        button_go_to_account.click()
        email = self.wait_and_find(self.EMAIL_INPUT)
        email.send_keys(data.HELPERS.email_for_test)
        password = self.wait_and_find(self.PASSWORD_INPUT)
        password.send_keys(data.HELPERS.password)
        button_log_in = self.wait_and_find(self.LOG_IN_BUTTON)
        button_log_in.click()
        source = self.wait_and_find(self.BULKA)
        target = self.wait_and_find(self.CONSTR)
        drag_and_drop(self.driver, source, target)
        order = self.wait_and_find(self.ORDER_BUTTON)
        order.click()
        exit = self.wait_and_find(self.BUTTON_EXIT)
        exit.click()
        tape_button = self.wait_and_find(self.ORDER_TAPE)
        tape_button.click()
        self.wait_and_find(self.ALL_TIME_COUNTER)
        new_number = self.wait_and_find(self.TODAY_COUNTER).text
        self.wait_and_find(self.TODAY_COUNTER)
        self.increase(first_number, new_number)




