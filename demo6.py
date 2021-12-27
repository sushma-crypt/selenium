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
driver.get("https://www.premierleague.com/")

players_ele = driver.find_element_by_link_text("Players").click()


element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "search-input")))


search_ele =driver.find_element_by_id("search-input")
search_ele.send_keys("Cristiano Ronaldo").click()
search_ele.send_keys(Keys.RETURN)
time.sleep(3)
driver.implicitly_wait(2)
click_ronaldo = driver.find_element_by_xpath("//img[@data-player='p14937']").click()

page_source_overview = driver.page_source
driver.close()

