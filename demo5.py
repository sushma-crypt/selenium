from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

chromeOptions = Options()
chromeOptions.add_argument("--kiosk")

driver = webdriver.Chrome(options=chromeOptions)
driver.get("https://eeaonline.eea.state.ma.us/portal#!/search/asbestos")

element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "ProjectID")))

Project_ID = driver.find_element_by_name("ProjectID")
Project_ID.clear()
Project_ID.send_keys("567")

location_name = driver.find_element_by_name("LocationName")
location_name.clear()
location_name.send_keys("america")

location_address = driver.find_element_by_name("LocationAddress")
location_address.clear()
location_address.send_keys("smart city, US")
time.sleep(1)