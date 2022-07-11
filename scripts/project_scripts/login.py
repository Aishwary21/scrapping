import time
from scripts.project_scripts.xpaths import google_signin_button, email_input, next_button, password_input, login_button

def login(driver):
    driver.find_element_by_xpath(google_signin_button()).click()
    
    
    time.sleep(3)
    
    email="aishwarynaraya3"
    
    driver.find_element_by_xpath(email_input()).send_keys(email)
    
    driver.find_element_by_xpath(next_button()).click()
    
    time.sleep(3)
    
    password="aishwary2001"
    
    driver.find_element_by_xpath(password_input()).send_keys(password)
    
    driver.find_element_by_xpath(login_button()).click()
    
    