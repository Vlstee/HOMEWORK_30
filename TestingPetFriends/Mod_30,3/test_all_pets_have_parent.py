# ________________ЗАДАНИЕ 30.3.1________________
# ________________ЯВНЫЕ ОЖИДАНИЯ________________

import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def test_all_pets_are_present(go_to_my_pets):
    '''Проверка того, что на странице "Мои питомцы" присутствуют все питомцы'''

    # ________________Установка явного ожидания________________
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.\\.col-sm-4.left')))

    # ________________Сохранение элементов статистики в переменную "statistic"
    statistic = pytest.driver.find_elements(By.CSS_SELECTOR, '.\\.col-sm-4.left')

    # ________________Установка явного ожидания________________
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.table.table-hover tbody tr')))

    # ________Сохранение элементов карточек питомцев в переменную "pets"________
    pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

    # _________Получение количества питомцев из данных статистики______
    number = statistic[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])

    # __________Получение количества карточек питомцев________________
    number_of_pets = len(pets)

    # Проверка того, что количество питомцев из статистики совпадает с количеством карточек питомцев
    assert number == number_of_pets