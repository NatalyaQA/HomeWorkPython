import time
import pytest
from webbrowser import BaseBrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
print("установил драйвер")
driver.get("http://suninjuly.github.io/cats.html")
print("старт задания")
time.sleep(15)
print("начинаю тест из def.......")
# link = "http://suninjuly.github.io/cats.html"
# driver = webdriver.Chrome()
# driver.get("http://suninjuly.github.io/cats.html")
# driver.get(link)
def test_1():
    print("зашел в функцию и сообщаю об этом")
    time.sleep(20)
    bullet_cat_text = driver.find_element(By.XPATH, '//p[text()="Bullet cat"]').text
    print("взял значение текста")
    time.sleep(15)
    print("оно равно: ", bullet_cat_text, "сейчас буду сравнивать через assert")
    time.sleep(15)
    assert bullet_cat_text == "Bullet cat", "wrong!"
    print("я сделал твое задание")
    time.sleep(15)
    print("и теперь могу закрыться и отдохнуть - \"твой браузер\"")
# закрываем браузер после всех манипуляций
    driver.quit()
