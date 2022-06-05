import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from Testdata.Testdata import Filelocation

s = Service('c:\\chromedriver_win32\\chromedriver.exe')
driver = webdriver.Chrome(service=s)

credential = []
f = open(Filelocation.get_path())
for l in f.readlines():
    if l != '\n':
        credential.append(l.replace('\n',''))
#close the file
f.close()
print(credential)

driver.get("https://github.com/login")
#login to git
driver.find_element(By.CSS_SELECTOR,"input[id='login_field']").send_keys(credential[0])
driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys(credential[1])

driver.find_element(By.CSS_SELECTOR,"input[value='Sign in']").click()
#creating new repository
driver.find_elements(By.XPATH,"//span[@class='dropdown-caret']")[0].click()
driver.find_elements(By.CSS_SELECTOR,"details-menu a[class='dropdown-item']")[0].click()
reponame = credential[2]    # repository name given Notepad entry
driver.find_element(By.CSS_SELECTOR, "input[id='repository_name']").send_keys(reponame)
driver.find_element(By.CSS_SELECTOR, "input[id='repository_visibility_public']")
#selecting Node value from the drop down list
driver.find_elements(By.CSS_SELECTOR,"summary[role='button']")[4].click()
driver.find_elements(By.CSS_SELECTOR, "filter-input input[type='text']")[0].send_keys('Node')
time.sleep(2)
driver.find_element(By.XPATH,"//div[contains(text(),'Node')]").click()
driver.find_elements(By.CSS_SELECTOR,"button[type='submit']")[1].click()
#after successfull creation of Repository validating  name of the repo and if the .gitignore file is present in it
text = driver.find_element(By.CSS_SELECTOR, "strong[itemprop='name'] a").get_attribute("innerText")
if text == reponame:
    giti=driver.find_element(By.CSS_SELECTOR, "span[class='css-truncate css-truncate-target d-block width-fit'] a").get_attribute("innertext")
    print("Your have created repository with name: ", reponame)
    print("Your repository contains: ", giti)
else:
    print("Not able to find the repository: ", reponame)
#Signout

time.sleep(5)
driver.find_elements(By.XPATH,"//span[@class='dropdown-caret']")[1].click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "form button[class='dropdown-item dropdown-signout']").click()
