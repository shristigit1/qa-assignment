import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

s = Service('c:\\chromedriver_win32\\chromedriver.exe')
driver = webdriver.Chrome(service=s)

f = open('C:\\Users\\Monu\\Desktop\\Selenium code\\gitdetails1.txt')
for y in f.readlines():
    if y != '\n':
        print(y)
        x = y.split(',')
        print(x)
        driver.get("https://github.com/login")
        driver.find_element(By.CSS_SELECTOR, "input[id='login_field']").send_keys(x[0])
        driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys(x[1])
        driver.find_element(By.XPATH,"//input[@value='Sign in']").click()

        driver.find_elements(By.XPATH, "//span[@class='dropdown-caret']")[1].click()
        element = driver.find_element(By.XPATH, "//a/strong[@class='css-truncate-target']")
        value = element.get_attribute("textContent")
        if x[0] in value:
            print("logged-in user is validated as : " + x[0])
        driver.find_element(By.CSS_SELECTOR, "form[class='logout-form']").click()
        driver.close()

f.close()
