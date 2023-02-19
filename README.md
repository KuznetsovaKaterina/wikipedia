# wikipedia
### Описание
Параметризованный автотест для таблицы "Programming languages used in most popular websites" на сайте https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites.

Тест проверяет что в таблице нет строк, у которых значение в столбце "Popularity(unique visitors per month)" меньше значения, передаваемого в качестве параметра в тест. 


### Особенности запуска
Используется webdriver Microsoft Edge.

Чтобы запустить через Firefox в файле conftest.py раскоментировать следующую строчку:

`driver = webdriver.Firefox()`

Для запуска через Google Chrome раскоментировать следующую строчку:

`driver = webdriver.Chrome(ChromeDriverManager().install())`

и установить библиотеку ChromeDriverManager:

`from webdriver_manager.chrome import ChromeDriverManager`
