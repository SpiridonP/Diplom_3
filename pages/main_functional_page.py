from pages.base_page import BasePage
from page_locators import locators
import allure
import data
from seletools.actions import drag_and_drop

class MainFunctional(BasePage):
    @allure.title('Проверка перехода в конструктор')
    @allure.step('Нажимаем на кнопку "Конструктора"')
    def go_to_constructor(self):
        button_personal_account = self.wait_and_find(locators.AccountLocators.LK)
        button_personal_account.click()
        button_constructor = self.wait_and_find(locators.MainFunctionalLocators.BUTTON_CONSTRUCTOR)
        button_constructor.click()

    @allure.title('Проверка текста на странице конструктора')
    def check_constructor_text_page(self):
        self.check(data.ASSERTS.burger_text)

    @allure.title('Проверка перехода в ленту заказов')
    @allure.step('Нажимаем на кнопку "Лента заказов"')
    def go_to_tape_order(self):
        tape = self.wait_and_find(locators.TapePageLocators.ORDER_TAPE)
        tape.click()
        self.wait_and_find(locators.TapePageLocators.ALL_TIME_COUNTER)

    @allure.title('Проверка текста на странице ленты заказов')
    def check_tape_page(self):
        self.page()

    @allure.title('Проверка открытия окна ингредиента')
    @allure.step('Нажимаем на ингредиент (открывается окно)"')
    def ingredient_window(self):
        ingredient = self.wait_and_find(locators.MainFunctionalLocators.SOME_INGREDIENT)
        ingredient.click()
        self.wait_and_find(locators.MainFunctionalLocators.BUTTON_EXIT)

    @allure.title('Проверка текста в окне ингредиента')
    def check_ingr(self):
        self.check(data.ASSERTS.ingr)

    def check_text(self):
        self.check(data.ASSERTS.all_time)

    @allure.title('Проверка закрытия окна ингредиента')
    @allure.step('Нажимаем на ингредиент (открывается окно) и нажимаем на крестик"')
    def ingredient_window_exit(self):
        ingredient = self.wait_and_find(locators.MainFunctionalLocators.SOME_INGREDIENT)
        ingredient.click()
        exit = self.wait_and_find(locators.MainFunctionalLocators.BUTTON_EXIT)
        exit.click()

    @allure.title('Проверка перетаскивания ингредиента в конструктор')
    @allure.step('Перетаскиваем компонент в конструктор"')
    def add_ingredient(self):
        source = self.wait_and_find(locators.MainFunctionalLocators.BULKA)
        target = self.wait_and_find(locators.MainFunctionalLocators.CONSTR)
        drag_and_drop(self.driver, source, target)

    @allure.title('Проверка увеличения цены после добавления ингредиента')
    def price(self):
        self.check_price(locators.MainFunctionalLocators.PRICE)

    @allure.title('Проверка заказа авторизованного пользователя')
    @allure.step('Авторизоваться и "сделатиь заказ"')
    def get_order_with_auth(self):
        button_go_to_account = self.wait_and_find(locators.AccountLocators.ACCOUNT)
        button_go_to_account.click()
        email = self.wait_and_find(locators.AccountLocators.EMAIL_INPUT)
        email.send_keys(data.HELPERS.email_for_test)
        password = self.wait_and_find(locators.AccountLocators.PASSWORD_INPUT)
        password.send_keys(data.HELPERS.password)
        button_log_in = self.wait_and_find(locators.AccountLocators.LOG_IN_BUTTON)
        button_log_in.click()
        source = self.wait_and_find(locators.MainFunctionalLocators.BULKA)
        target = self.wait_and_find(locators.MainFunctionalLocators.CONSTR)
        drag_and_drop(self.driver, source, target)
        order = self.wait_and_find(locators.MainFunctionalLocators.ORDER_BUTTON)
        order.click()
        exit = self.wait_and_find(locators.MainFunctionalLocators.BUTTON_EXIT)
        exit.click()

    @allure.title('Проверка, что заказ готовится')
    def cooking(self):
        self.check(data.ASSERTS.order_cooking)









