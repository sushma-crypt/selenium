from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.support import select
from selenium.webdriver.common.keys import Keys




url = "https://eeaonline.eea.state.ma.us/Portal/#!/search/asbestos"
driver = webdriver.Chrome("C://webdrivers/chromedriver.exe")
driver.get(url)
soup = BeautifulSoup(driver.page_source, "html.parser")
#print(soup.prettify())


select_tag = soup.find("select")
options = select_tag.find_all("option")
for option in options:
  print(option.text)
driver.close()

#ele_droptown = driver.find_element_by_id('TownName')
#Select = select(ele_droptown)
#item = Select.select_by_visible_index('ACTON')
#print(item)


#search_ele =driver.find_element_by_class_name("btn btn-primary btn-custom pull-right")
#search_ele.send_keys("ACTON")
#search_ele.send_keys(Keys.RETURN)