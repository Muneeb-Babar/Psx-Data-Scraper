import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Setup Chrome driver
driver = webdriver.Chrome(service=Service(r"c:\Users\AAC\Downloads\chromedriver-win64\chromedriver.exe"))

# Open the website
driver.get("https://www.psx.com.pk/market-summary/")
time.sleep(5)  # Wait for the page to load

# Find all tables
tables = driver.find_elements(By.XPATH, "//div[@class='table-responsive']//table")

all_data = []

for table in tables:
    rows = table.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        cols = [col.text for col in row.find_elements(By.TAG_NAME, "td")]
        if cols:
            all_data.append(cols)

# Save to CSV
df = pd.DataFrame(all_data)
df.to_csv("psx_all_tables.csv", index=False)
print("Saved all tables to psx_all_tables.csv")

driver.quit()
