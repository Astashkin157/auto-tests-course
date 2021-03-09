from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    browser.execute_script("window.scrollBy(0, 200);")
    input1 = browser.find_element_by_css_selector('#answer')
    input1.send_keys(calc(x))
    button1 = browser.find_element_by_css_selector("#robotCheckbox")
    button1.click()
    button2 = browser.find_element_by_css_selector("#robotsRule")
    button2.click()
    button3 = browser.find_element_by_css_selector(".btn")
    button3.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
