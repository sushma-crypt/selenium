from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chromeOptions = Options()
chromeOptions.add_argument("--kisok")

#locating elements by link text:

driver = webdriver.Chrome(options=chromeOptions)
driver.get("https://annamalaiuniversity.ac.in/index.php")

ele = driver.find_element_by_name("q")
time.sleep(1)
ele.clear()
ele.send_keys("student")
ele.send_keys(Keys.RETURN)

ele_link = driver.find_element_by_link_text("Student Information Center")
# locating elements by partial link text:
#ele_link = driver.find_element_by_partial_link_text("Building Image")

time.sleep(1)
ele_link.click()

driver.quit()