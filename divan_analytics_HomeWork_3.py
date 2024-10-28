from selenium import webdriver
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
url = 'https://www.divan.ru/category/divany-i-kresla'
driver.get(url)
wait = WebDriverWait(driver, 15)
prices = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//span[@class="ui-LD-ZU KIkOH" and @data-testid="price"]')))

with open('prices_divan_3.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])

    for price in prices:
        #print(price.text)
        writer.writerow([price.text])

driver.quit()
