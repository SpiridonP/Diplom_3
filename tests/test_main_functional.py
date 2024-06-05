from pages.main_functional_page import MainFunctional
from data import URLS
import allure


class TestFunctional:
    def test_constructor(self, driver):
        value = MainFunctional(driver)
        value.open_page(URLS.url)
        value.go_to_constructor()
        value.check_constructor_text_page()


    def test_pape(self, driver):
        value = MainFunctional(driver)
        value.open_page(URLS.url)
        value.go_to_tape_order()
        value.check_text()

    def test_ingr_window(self, driver):
        value = MainFunctional(driver)
        value.open_page(URLS.url)
        value.ingredient_window()
        value.check_ingr()

    def test_ingr_window_exit(self, driver):
        value = MainFunctional(driver)
        value.open_page(URLS.url)
        value.ingredient_window_exit()
        value.check_constructor_text_page()

    def test_ingredient_constructor(self, driver):
        value = MainFunctional(driver)
        value.open_page(URLS.url)
        value.add_ingredient()
        value.price()

    def test_order_with_auth(self, driver):
        value = MainFunctional(driver)
        value.open_page(URLS.url)
        value.get_order_with_auth()
        value.cooking()




