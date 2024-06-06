import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from data import URLS
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By




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

    #def action(self):
     #   action_chains = ActionChains(self.driver)
      #  element = (By.XPATH, './/p[text()="Флюоресцентная булка R2-D3"]')
       # target = (By.XPATH, './/span[@alt="Перетяните булочку сюда (верх)"]')
        #action_chains.drag_and_drop(element, target)
    def check_price(self, locator):
        assert self.driver.find_element(*locator).text != 0

    def check_source(self, locator):
        assert self.driver.find_element(*locator).text in self.driver.page_source

    def compare(self, locator):
        assert '0' in self.driver.find_element(*locator).text

    def increase(self, value_one, value_two):
        assert value_one != value_two






