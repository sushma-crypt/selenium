from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chromeOptions = Options()


#locating elements by x path:

driver = webdriver.Chrome(options=chromeOptions)
driver.get("https://app.pluralsight.com/")

ele = driver.find_element_by_xpath("//input[@name='q']")
time.sleep(1)
ele.clear()
ele.send_keys("Pradeerth Padman")
ele.send_keys(Keys.RETURN)

driver.quit()