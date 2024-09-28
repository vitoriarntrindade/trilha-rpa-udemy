from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui as wait_time
from openpyxl import load_workbook
import os
from typing import List


def extract_table_data_to_excel(file_name: str, url: str, sheet_name: str, iterations: int) -> None:
    spreadsheet = load_workbook(filename=file_name)
    selected_sheet = spreadsheet[sheet_name]

    driver = webdriver.Chrome()
    driver.get(url)

    for _ in range(iterations):
        table = driver.find_element(By.XPATH, '//*[@id="tableSandbox"]')
        rows = table.find_elements(By.TAG_NAME, "tr")

        for row_index, row in enumerate(rows, start=len(selected_sheet['A']) + 1):
            columns: List[str] = row.text.split(" ")
            if len(columns) >= 3:
                selected_sheet[f"A{row_index}"] = columns[0]
                selected_sheet[f"B{row_index}"] = columns[1]
                selected_sheet[f"C{row_index}"] = columns[2]

        wait_time.sleep(2)
        next_button = driver.find_element(By.XPATH, '//*[@id="tableSandbox_next"]')
        next_button.click()
        wait_time.sleep(2)

    spreadsheet.save(filename=file_name)
    driver.quit()
    os.startfile(file_name)

extract_table_data_to_excel(file_name="data.xlsx", url="https://rpachallengeocr.azurewebsites.net/", sheet_name="Data", iterations=3)
