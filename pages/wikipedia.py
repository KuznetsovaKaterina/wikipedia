import re

from selenium.webdriver.common.by import By
from pages.base_page import Base


# Locators table «Programming languages used in most popular websites»
class Locators:
    ROW = (By.XPATH, f'// *[ @ id = "mw-content-text"] / div[1] / table[1] / tbody / tr')
    COLUMN = (By.XPATH, f'// *[ @ id = "mw-content-text"] / div[1] / table[1] / tbody / tr[1]/td')


class TableWebsites(Base):

    def get_table(self):
        rows = len(self.find_elements(Locators.ROW))
        cols = len(self.find_elements(Locators.COLUMN))
        result = []  # variable for all table data
        data = []  # variable for the data of each row
        for j in range(1, cols + 1):
            data.clear()
            for i in range(1, rows + 1):
                locator = (By.XPATH,
                           '// *[ @ id = "mw-content-text"] / div[1] / table[1] / tbody / tr[' + str(i) + ']/td[' +
                           str(j) + ']')
                elem = self.find_element(locator).text
                data.append(elem)
            result.append(data.copy())
        return result

    '''Converts the popularity field to numbers'''
    def get_number_popularity(self, popularity):
        not_number = str(popularity).replace(",", "").replace(".", "").replace("[", "", 1)
        not_number_without_brackets = re.sub(r'\[[^\]]*\]', '',
                                             not_number)  # regular expression to replace [] and everything in it
        numbers = re.findall(r'\d+', not_number_without_brackets)  # regular expression for finding digits
        return numbers
