from pages.tape_page import Tape
from data import URLS
import allure

class TestTapeOrder:

    @allure.title('Проверка отображения окна заказа')
    def test_check_order_window(self, driver):
        value = Tape(driver)
        value.open_page(URLS.url)
        value.order_window_check()
        value.check_order_window_text()

    @allure.title('Проверка отображения заказа пользователя')
    def test_check_users_order(self, driver):
        value = Tape(driver)
        value.open_page(URLS.url)
        value.check_users_order()
        value.check_order_number()

    @allure.title('Проверка отображения заказа в поле "В работе"')
    def test_compare(self, driver):
        value = Tape(driver)
        value.open_page(URLS.url)
        value.compare_numbers()
        value.compares()

    @allure.title('Проверка увеличения кол-ва заказов в "Выполнено за все время:"')
    def test_increase_all_time(self, driver):
        value = Tape(driver)
        value.open_page(URLS.url)
        value.increase_all_time()

    @allure.title('Проверка увеличения кол-ва заказов в "Выполнено за сегодня:"')
    def test_increase_today(self, driver):
        value = Tape(driver)
        value.open_page(URLS.url)
        value.increase_today()