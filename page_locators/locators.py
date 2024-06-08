from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainFunctionalLocators:
    LK = (By.LINK_TEXT, "Личный Кабинет")
    EMAIL_INPUT = (By.NAME, 'name')
    PASSWORD_INPUT = (By.NAME, "Пароль")
    LOG_IN_BUTTON = (By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')
    ORDERS_HISTORY = (By.XPATH, ".//a[text()='История заказов']")
    LOG_OUT = (By.XPATH, ".//button[text()='Выход']")
    BUTTON_CONSTRUCTOR = (By.LINK_TEXT, "Конструктор")
    ORDER_TAPE = (By.XPATH, './/p[text()="Лента Заказов"]')
    SOME_INGREDIENT = (By.XPATH, './/p[text()="Флюоресцентная булка R2-D3"]')
    BUTTON_EXIT = (By.XPATH, './/button[@type="button"]')
    ALL_TIME = (By.XPATH, './/p[text()="Выполнено за все время:"]')
    BULKA = (
        By.XPATH, ".//p[contains(text(), 'Краторная булка N-200i')]")
    CONSTR = (
        By.XPATH, ".//section[contains(@class, 'BurgerConstructor_basket')]")
    PRICE = (By.CLASS_NAME, 'constructor-element__price')
    ORDER_BUTTON = (By.XPATH, './/button[text()="Оформить заказ"]')
    ACCOUNT = (By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")


class RecoveryPasswordLocators:
    LK = (By.XPATH, './/p[text()="Личный Кабинет"]')
    PASSWORD_RECOVERY = (By.XPATH, './/a[text()="Восстановить пароль"]')
    EMAIL_INPUT = (By.NAME, 'name')
    BUTTON_RECOVERY = (By.XPATH, './/button[text()="Восстановить"]')
    PASSWORD_INPUT = (By.XPATH, './/form/fieldset/div/div/input[@name="Введите новый пароль"]')
    EYE_BUTTON = (By.XPATH, ".//div[contains(@class,'input__icon')]")
    BUTTON_SAVE = (By.XPATH, './/fieldset/button[text()="Сохранить"]')


class AccountLocators:
    ACCOUNT = (By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    LK = (By.LINK_TEXT, "Личный Кабинет")
    EMAIL_INPUT = (By.NAME, 'name')
    PASSWORD_INPUT = (By.NAME, "Пароль")
    LOG_IN_BUTTON = (By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')
    ORDERS_HISTORY = (By.XPATH, ".//a[text()='История заказов']")
    LOG_OUT = (By.XPATH, ".//button[text()='Выход']")
    SAVE = (By.XPATH, './/button[text()="Сохранить"]')
    ENTER = (By.XPATH, './/h2[@text()="Вход"]')


class TapePageLocators:
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