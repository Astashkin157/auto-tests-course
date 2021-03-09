from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button1 = browser.find_element_by_css_selector(".trollface")
    button1.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    browser.execute_script("window.scrollBy(0, 200);")
    input1 = browser.find_element_by_css_selector('#answer')
    input1.send_keys(calc(x))
    button2 = browser.find_element_by_css_selector(".btn")
    button2.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
