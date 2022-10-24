import time
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

def test_title_site():
    try:

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get('https://www.saucedemo.com/')
        time.sleep(10)

        assert driver.title == 'Swag Labs'
        print("успешно")

    finally:
        driver.quit()

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get('https://www.saucedemo.com/')
#
# def test_title():
#     title_from_site = driver.title
#     assert title_from_site == "Swag Labs"


