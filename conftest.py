import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    fire = webdriver.Chrome()
    fire.maximize_window()
    yield fire
    fire.quit()