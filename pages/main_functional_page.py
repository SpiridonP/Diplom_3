from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
import allure
import data
import time
from seletools.actions import drag_and_drop


class MainFunctional(BasePage):
    LK = (By.LINK_TEXT, "Личный Кабинет")
    EMAIL_INPUT = (By.NAME, 'name')
    PASSWORD_INPUT = (By.NAME, "Пароль")
    LOG_IN_BUTTON = (By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')
    ORDERS_HISTORY = (By.XPATH, ".//a[text()='История заказов']")
    LOG_OUT = (By.XPATH, ".//button[text()='Выход']")
    BUTTON_CONSTRUCTOR = (By.LINK_TEXT, "Конструктор")
    ORDER_TAPE = (By.XPATH, './/p[text()="Лента Заказов"]')
    SOME_INGREDIENT = (By.XPATH, './/p[text()="Флюоресцентная булка R2-D3"]')
    #BUTTON_EXIT = (By.XPATH, './/button[type="button"]')
    BUTTON_EXIT = (By.XPATH, './/button[@type="button"]')
    ALL_TIME = (By.XPATH, './/p[text()="Выполнено за все время:"]')
    BULKA = (
        By.XPATH, ".//p[contains(text(), 'Краторная булка N-200i')]")
    CONSTR = (
        By.XPATH, ".//section[contains(@class, 'BurgerConstructor_basket')]")
    PRICE = (By.CLASS_NAME, 'constructor-element__price')
    ORDER_BUTTON = (By.XPATH, './/button[text()="Оформить заказ"]')
    ACCOUNT = (By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")

    def go_to_constructor(self):
        button_personal_account = self.wait_and_find(self.LK)
        button_personal_account.click()
        button_constructor = self.wait_and_find(self.BUTTON_CONSTRUCTOR)
        button_constructor.click()

    def check_constructor_text_page(self):
        self.check(data.ASSERTS.burger_text)


    def go_to_tape_order(self):
        tape = self.wait_and_find(self.ORDER_TAPE)
        tape.click()
        self.wait_and_find(self.ALL_TIME)


    def check_tape_page(self):
        self.page()

    def ingredient_window(self):
        ingredient = self.wait_and_find(self.SOME_INGREDIENT)
        ingredient.click()
        self.wait_and_find(self.BUTTON_EXIT)

    def check_ingr(self):
        self.check(data.ASSERTS.ingr)


    def check_text(self):
        self.check(data.ASSERTS.all_time)

    def ingredient_window_exit(self):
        ingredient = self.wait_and_find(self.SOME_INGREDIENT)
        ingredient.click()
        exit = self.wait_and_find(self.BUTTON_EXIT)
        exit.click()

    def add_ingredient(self):
        source = self.wait_and_find(self.BULKA)
        target = self.wait_and_find(self.CONSTR)
        drag_and_drop(self.driver, source, target)

    def price(self):
        self.check_price(self.PRICE)


    def get_order_with_auth(self):
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

    def cooking(self):
        self.check(data.ASSERTS.order_cooking)







