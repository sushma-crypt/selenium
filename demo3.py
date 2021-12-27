from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chromeOptions = Options()
chromeOptions.add_argument("--kisok")

#locating elements by css selector:

driver = webdriver.Chrome(options=chromeOptions)
driver.get("https://annamalaiuniversity.ac.in/search.php?q=student")
ele = driver.find_element_by_css_selector("search")
time.sleep(1)
ele.clear()
ele.send_keys("student")
ele.send_keys(Keys.RETURN)

driver.quit()