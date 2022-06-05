import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from Testdata.Testdata import Filelocation

s = Service('c:\\chromedriver_win32\\chromedriver.exe')
driver = webdriver.Chrome(service=s)

#steps to pick the user details and name of the repository from the Notepad
credential = []
f = open(Filelocation.get_path())
for l in f.readlines():
    if l != '\n':
        credential.append(l.replace('\n',''))
#close the file
f.close()
print(credential)

driver.get("https://github.com/login")
#login to Git
driver.find_element(By.CSS_SELECTOR,"input[id='login_field']").send_keys(credential[0])
driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys(credential[1])

driver.find_element(By.CSS_SELECTOR,"input[value='Sign in']").click()
driver.find_elements(By.XPATH,"//span[@class='dropdown-caret']")[1].click()
time.sleep(5)
element = driver.find_element(By.XPATH,"//a/strong[@class='css-truncate-target']")
value = element.get_attribute("textContent")
if credential[0] in value:
   print("logged-in user is validated as : " + credential[0])  #Verify that the right username/email address is displayed on the text "Signed

#Signout
driver.find_element(By.CSS_SELECTOR, "form button[class='dropdown-item dropdown-signout']").click()

driver.close()



