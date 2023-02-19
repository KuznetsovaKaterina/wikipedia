import pytest

from data.data import Table
from pages.wikipedia import TableWebsites


class TestTable:
    @pytest.mark.parametrize('value', [10000000, 15000000, 50000000, 100000000, 500000000, 1000000000, 1500000000])
    def test_popularity(self, driver, value):
        wiki_page = TableWebsites(driver,
                                  "https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites")
        wiki_page.open()
        data = wiki_page.get_table()
        table = Table(data[0], data[1], data[2], data[3], data[4], data[5])
        popularity = wiki_page.get_number_popularity(table.popularity)
        errors = []  # variable for rows with error
        i = 0  # variable for index
        for elem in popularity:
            if int(elem) < value:
                errors.append(f"{table.websites[i]} "
                              f"(Frontend:{table.front_end[i]} "
                              f"|Backend:{table.back_end[i]} "
                              f"has {table.popularity[i]} "
                              f"unique visitors per month. (Expected more than {value})")
            i = i + 1
        assert errors == [], f"There are {len(errors)} rows in the table with popularity less than the parameter:" \
                             f"\n {errors}"
