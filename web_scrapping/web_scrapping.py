from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui


webdriver = webdriver.Chrome()
webdriver.get("https://rpachallengeocr.azurewebsites.net/")

element_table = webdriver.find_element(By.XPATH, '//*[@id="tableSandbox"]')

lines_table = element_table.find_elements(By.TAG_NAME, "tr")
columns_table = element_table.find_elements(By.TAG_NAME, "td")

lines = 1
for line in lines_table:
    print(line.text)
    lines =+ 1

