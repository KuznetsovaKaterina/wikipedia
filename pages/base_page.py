from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    '''Checking for the availability of an element'''

    def element_is_visible(self, locator, timeout=5):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    def find_element(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))

    def find_elements(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_all_elements_located(locator))
