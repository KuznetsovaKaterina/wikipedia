import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture()
def driver():
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    ''' If you wont to use driver Firefox uncomment the line below and comment line 9'''
    #driver = webdriver.Firefox()
    ''' If you wont to use driver Chrome uncomment the line below, install library "ChromeDriverManager" and comment line 9'''
    #driver = webdriver.Chrome(ChromeDriverManager().install())

    yield driver
    driver.quit()
