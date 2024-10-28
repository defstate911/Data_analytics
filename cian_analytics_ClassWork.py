from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.firefox.service import Service
import time
import csv

driver = webdriver.Firefox()
url = 'https://www.cian.ru/snyat-kvartiru-1-komn-ili-2-komn/'
driver.get(url)
time.sleep(5)
prices = driver.find_elements(By.XPATH, "//span[@data-mark='MainPrice']/span")


with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Записываем заголовок столбца

    # Записываем цены в CSV файл
    for price in prices:
        writer.writerow([price.text])

# Закрытие драйвера
driver.quit()
