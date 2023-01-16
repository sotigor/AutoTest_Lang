Проверка наличия кнопки "Добавить в корзину" на сайте
при использовании:
1. Pytest и Selenium
2. Фикстур из файла conftest.py
3. Настройки тестового окружения через командную строку
   при помощи встроенной функции pytest_addoption и 
   фикстуры request.

Для использования в командной строке настроены две переменные:
1. name_browser,  может принимать значения chrome или firefox (по умолчанию chrome)
2. language, может принимать значения "uk", "ru", "es", "en-gb" или "fr".

Пример ввода в командной строке:

pytest --language=en-gb test_items.py





 