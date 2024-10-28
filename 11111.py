from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
max_retries = 5
prices = []
river = webdriver.Firefox()
url = 'https://www.divan.ru/category/divany-i-kresla'
driver.get(url)
wait = WebDriverWait(driver, 15)
# Получение элементов с обработкой исключения
for i in range(max_retries):
    try:
        price_elements = driver.find_elements(By.XPATH, '//span[@class="ui-LD-ZU KIkOH" and @data-testid="price"]')
        prices = [price.text for price in price_elements]  # Собираем текст всех цен
        break  # Если успешно выполнено, выходим из цикла
    except StaleElementReferenceException:
        print(f"Попытка {i+1}/{max_retries} - элемент устарел. Повторная попытка...")
        time.sleep(1)  # Ожидаем перед новой попыткой

# Проверка и запись цен
if prices:
    with open('prices.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Price"])
        for price in prices:
            writer.writerow([price])
else:
    print("Не удалось получить данные о ценах.")
