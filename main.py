from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options() 
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'


driver = webdriver.Firefox(executable_path=r'C:\WebDrivers\geckodriver.exe', options=options)

# driver.get('http://google.com/')

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
# driver = webdriver.Firefox()

# driver.get("https://www.thesparksfoundationsingapore.org/")
driver.get("https://anoop-111.github.io/product_landing/");





print("\n \n========= Let's Check For The TestCases =========\n")

########################## TestCase 1:Title ###############################
print("TestCase #1:")
if(driver.title):
    print("Title Verification Successful  ✔️ ")
else:
    print("Title Verification Failed! ❌\n")
time.sleep(3)
print("")


########################## TestCase 2:Home button #########################
print("TestCase #2: Home page buy link ")
try:
    driver.find_element(By.XPATH,"/html/body/section[1]/div[1]/a/button").click()
    print("Home BUY link works! ✔️\n")
except NoSuchElementException:
    print("Home BUY Link Doesn't Work! ❌\n")

print("coming back to main page")
driver.back()
time.sleep(3)




######################### TestCase 3:Check if CORE Section works properly #########################
print("TestCase #3: CORE SECTION")
try:
    driver.find_element(By.XPATH,"/html/body/header/nav/ul/li[2]/a").click()
    print("Core section visited ✔️\n")

    driver.find_element(By.XPATH," /html/body/section[2]/div/div[2]/div[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH," /html/body/section[2]/div/div[2]/div[2]").click()
    time.sleep(3)
    driver.find_element(By.XPATH," /html/body/section[2]/div/div[2]/div[3]").click()
    time.sleep(3)
    driver.find_element(By.XPATH," /html/body/section[2]/div/div[2]/div[4]").click()
    time.sleep(3)
    
except NoSuchElementException:
    print("Core Seection does not work properly ❌\n")
time.sleep(3)




####################### TestCase 4:About Section ########################################
print("TestCase #4: ABOUT SECTION")
try:
    driver.find_element(By.XPATH,"/html/body/header/nav/ul/li[3]/a").click()
    print("About section visited ✔️\n")

    driver.find_element(By.XPATH,"/html/body/section[3]/div/div[2]/a/button").click()
    time.sleep(3)

    print("About Section -> LEARN MORE Button works ✔️")

    print("coming back to main page")
    driver.back()
  
except NoSuchElementException:
    print("Core Seection does not work properly ❌\n")
time.sleep(3)


print("")



##################### TestCase 5:Features Section ######################################
print("TestCase #5: FEATURES SECTION")
try:
    driver.find_element(By.XPATH,"/html/body/header/nav/ul/li[4]/a").click()
    print("Features section visited ✔️\n")

    driver.find_element(By.XPATH,"/html/body/section[4]/div/div[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"/html/body/section[4]/div/div[2]").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"/html/body/section[4]/div/div[3]").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"/html/body/section[4]/div/div[4]").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"/html/body/section[4]/div/div[5]").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"/html/body/section[4]/div/div[6]").click()
    time.sleep(3)

    print("Feature Section -> Items visited ✔️")


except NoSuchElementException:
    print("Feature Section does not work properly ❌\n")
time.sleep(3)


print("")



########################### TestCase 6:Check the Contact us Page #########################

print("TestCase #6: mail to seller")
try:
    driver.find_element(By.XPATH,'/html/body/header/nav/ul/li[6]/a').click()
    time.sleep(3)
    # driver.find_element(By.LINK_TEXT,'Why Join Us').click()
    # time.sleep(3)
    print("Typing your name...")
    driver.find_element(By.XPATH,'/html/body/section[6]/form/input[1]').send_keys('Anoopkumar')
    time.sleep(3)
    print("Typing your Email address...")
    driver.find_element(By.XPATH,'/html/body/section[6]/form/input[2]').send_keys('anoopkumarshukla111@gmail.com')
    time.sleep(3)
    driver.find_element(By.XPATH,'/html/body/section[6]/form/input[3]').send_keys('1234567899')
    time.sleep(3)
    print("Typing message...")
    driver.find_element(By.XPATH,'/html/body/section[6]/form/textarea').send_keys('You are awesome !')
    time.sleep(3)
    print("sending now...")
    # driver.find_element(By.NAME,'Email').send_keys('anoopkumarshukla111@gmail.com')
    # time.sleep(3)
    driver.find_element(By.XPATH,'/html/body/section[6]/form/input[4]').click()
    # driver.find_element(By.ID('button-s')).click();
    # driver.close(); 
    print("Form Verification Successful! ✔️\n")
    time.sleep(3)
except NoSuchElementException:
    print("Form Verification Failed! ❌\n")
    time.sleep(3)



