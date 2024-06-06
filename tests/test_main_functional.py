from pages.main_functional_page import MainFunctional
from data import URLS
import allure


class TestFunctional:

    @allure.title('Проверка перехода в конструктор')
    def test_constructor(self, driver):
        value = MainFunctional(driver)
        value.open_page(URLS.url)
        value.go_to_constructor()
        value.check_constructor_text_page()

    @allure.title('Проверка перехода в ленту заказов')
    def test_tape(self, driver):
        value = MainFunctional(driver)
        value.open_page(URLS.url)
        value.go_to_tape_order()
        value.check_text()

    @allure.title('Проверка отображения окна ингредиентов')
    def test_ingr_window(self, driver):
        value = MainFunctional(driver)
        value.open_page(URLS.url)
        value.ingredient_window()
        value.check_ingr()

    @allure.title('Проверка закрытия окна ингредиентов')
    def test_ingr_window_exit(self, driver):
        value = MainFunctional(driver)
        value.open_page(URLS.url)
        value.ingredient_window_exit()
        value.check_constructor_text_page()

    @allure.title('Проверка перемещения ингредиента')
    def test_ingredient_constructor(self, driver):
        value = MainFunctional(driver)
        value.open_page(URLS.url)
        value.add_ingredient()
        value.price()

    @allure.title('Проверка заказа с залогиненным пользователем')
    def test_order_with_auth(self, driver):
        value = MainFunctional(driver)
        value.open_page(URLS.url)
        value.get_order_with_auth()
        value.cooking()




