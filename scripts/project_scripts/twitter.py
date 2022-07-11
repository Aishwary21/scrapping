import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from scripts.project_scripts.login import login
from scripts.project_scripts.search import search
from scripts.project_scripts.convert_to_csv import convert
from scripts.project_scripts.count import get_tweet


def run():
    try:
        # option = Options()
        # option.add_argument('headless')

        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.twitter.com/")

        driver.maximize_window()
        time.sleep(3)
        login(driver)
        time.sleep(4)
        search(driver)
        time.sleep(3)
        tweet=get_tweet(driver)
        convert(tweet)
        
    except Exception as e:
        print(str(e))
    finally:
        driver.quit()

    