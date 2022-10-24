import time
import pytest
from webbrowser import BaseBrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# link = "http://suninjuly.github.io/cats.html"
driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/cats.html")
# driver.get(link)

# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
print("установил драйвер")
# driver.get("http://suninjuly.github.io/cats.html")
print("старт задания")
time.sleep(15)

# def test_1():
#     bullet_cat_text = driver.find_element(By.XPATH, '//p[@text()="Bullet cat"]').text
#     print("взял значение текста")
#     print("оно равно: ", bullet_cat_text)
#     assert bullet_cat_text == "Bullet cat", "wrong!"
#     print("я сделал твое задание")
#     time.sleep(15)

bullet_cat_text = driver.find_element(By.XPATH, '//p[text()="Bullet cat"]').text
print("взял значение текста")
print("оно равно: ", bullet_cat_text)
assert bullet_cat_text == "Bullet cat", "wrong!"
print("я сделал твое задание")
time.sleep(15)
# закрываем браузер после всех манипуляций
driver.quit()
