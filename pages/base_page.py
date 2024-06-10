from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait



class BasePage:
    def __init__(self, driver):
        self.driver = driver


    def wait_and_find(self, locator):
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)


    def check(self, answer_locators):
        assert answer_locators in self.driver.page_source


    def find_locator(self, locator):
        self.driver.find_element(*locator)


    def open_page(self, url):
        self.driver.get(url)

    def page(self):
        assert 'Выполнено за все время:' in self.driver.page_source

    def check_url(self):
        assert self.driver.current_url == 'https://stellarburgers.nomoreparties.site/account/order-history'

    def check_price(self, locator):
        assert self.driver.find_element(*locator).text != 0

    def check_source(self, locator):
        assert self.driver.find_element(*locator).text in self.driver.page_source

    def compare(self, locator):
        assert '0' in self.driver.find_element(*locator).text

    def increase(self, value_one, value_two):
        assert value_one != value_two






