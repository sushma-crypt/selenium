from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chromeOptions = Options()
#chromeOptions.add_argument("--kisok")

#locating elements by id:

driver = webdriver.Chrome(options=chromeOptions)
driver.get("https://www.python.org/")
ele = driver.find_element_by_id("id-search-field")
time.sleep(3)
ele.clear()
ele.send_keys("lists")
ele.send_keys(Keys.RETURN)
driver.quit()