import time
from scripts.project_scripts.xpaths import search_box
from selenium.webdriver.common.keys import Keys
def search(driver):
    search="#bollywood"
    time.sleep(3)
    driver.find_element_by_xpath(search_box()).send_keys(search)
    time.sleep(2)
    driver.find_element_by_xpath(search_box()).send_keys(Keys.ENTER)
    time.sleep(1)
    