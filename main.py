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
    print("Title Verification Successful  ✔️ ",driver.title)
else:
    print("Title Verification Failed! ❌\n")
time.sleep(3)
print("")


########################## TestCase 2:Home button #########################
print("TestCase #2:")
try:
    driver.find_element(By.PARTIAL_LINK_TEXT,"The Sparks Foundation").click()
    print("Home link works! ✔️\n")
except NoSuchElementException:
    print("Home Link Doesn't Work! ❌\n")
time.sleep(3)

########################## TestCase 3:Check if navbar appears #########################
print("TestCase #3:")
try:
    driver.find_element(By.CLASS_NAME,"navbar")
    print("Navbar Verification Successful! ✔️\n")
except NoSuchElementException:
    print("Navbar Verification Failed! ❌\n")
time.sleep(3)

######################## TestCase 4:Scrolling down ########################################
print("TestCase #4:")
for i in range(0,1500,200):
    driver.execute_script(f"window.scrollTo(0, window.scrollY + {i})")
    time.sleep(1)
print("scrolled down ✔️")

###################### TestCase 5:scrolling up ######################################
print("TestCase #5:")
driver.find_element(By.ID,"about").click()
time.sleep(1)
print("scrolled up ✔️")
print("")


########################## TestCase 6:About Us Page #########################
print("TestCase #6:")
try:
    driver.find_element(By.LINK_TEXT,'About Us').click()
    time.sleep(3)

    print('Page visited Successfully! ✔️\n')
except NoSuchElementException:
    print("Page visit Failed! Does not exist. ❌\n")
    time.sleep(3)


########################## TestCase 7:Policies and Code #########################
print('TestCase #7:')
try:
    driver.find_element(By.LINK_TEXT,'Policies and Code').click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT,"Policies").click()
    time.sleep(3)
    print('Policy page exists. Success! ✔️\n')
except NoSuchElementException:
    print('Policy Page Does not exist. Failed! ❌\n')
    time.sleep(3)


########################## TestCase 8:Workshop page #########################
print('TestCase #8:')
try:
    driver.find_element(By.LINK_TEXT,'Programs').click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT,"Workshops").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT,'LEARN MORE').click()
    time.sleep(3)
    print('Workshop Page Verified! ✔️\n')
except NoSuchElementException:
    print('No New Tab opened. Failed! ❌\n')


########################## TestCase 9: Check If Logo Exists #########################
print('TestCase #9:')
try:
    driver.find_element(By.XPATH,'//*[@id="home"]/div/div[1]/h1/a/*').click()
    print('Found Logo! Success! ✔️\n')
    time.sleep(3)
except NoSuchElementException:
    print('No logo found! ❌\n')

time.sleep(4)
driver.switch_to.window(driver.window_handles[0])
print("switched to 1st Tab\n")
time.sleep(1.5)

########################## TestCase 10:Check the Form #########################
print("TestCase #10:")
try:
    driver.find_element(By.LINK_TEXT,'Join Us').click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT,'Why Join Us').click()
    time.sleep(3)
    print("Typing your name...")
    driver.find_element(By.NAME,'Name').send_keys('Anoop')
    time.sleep(3)
    print("Typing your Email address...")
    driver.find_element(By.NAME,'Email').send_keys('fake@gmail.com')
    time.sleep(3)
    select =Select(driver.find_element(By.CLASS_NAME,'form-control'))
    time.sleep(3)
    select.select_by_visible_text('Student')
    time.sleep(3)
    driver.find_element(By.CLASS_NAME,'button-w3layouts').click()
    time.sleep(3)
    print("Form Verification Successful! ✔️\n")
    time.sleep(3)
except NoSuchElementException:
    print("Form Verification Failed! ❌\n")
    time.sleep(3)


########################### TestCase 11:Check the Contact us Page #########################
print("TestCase #11:")
try:
    driver.find_element(By.LINK_TEXT,"Contact Us").click()
    time.sleep(1)
    info = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div[2]/p[2]')
    time.sleep(1)
   
    
    if(info.text == "+65-8402-8590, info@thesparksfoundation.sg"):
        print('contact Information Correct!')
    else:
        print('Contact Information Incorrect!')
   
    print("Contact Page Verification Sucessful! ✔️\n")
except NoSuchElementException:
    print("Contact Page Verification unsuccessful! ❌")


########################### TestCase 12:again back to main page #########################


print("TestCase #12:")
# driver.find_element(By.XPATH,"/html/body/section[1]/div[1]/a/button").click()
print(" again back to main page ✔️")
# time.sleep(3)
print("")

########################### TestCase 13:clicking 1-6 #########################


print("TestCase #13:")

driver.find_element(By.XPATH,'/html/body/footer')
# time.sleep(1)

# driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/section/div/ol/li[3]/a").click()
# print(" clicked 3 Mentorship ✔️")
# time.sleep(1)

# driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/section/div/ol/li[4]/a").click()
# print(" clicked 4 support ✔️")
# time.sleep(1)

# driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/section/div/ol/li[5]/a").click()
# print(" clicked 5 scholarships ✔️")
# time.sleep(1)

# driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/section/div/ol/li[6]/a").click()
# print(" clicked 6 community ✔️")
# time.sleep(1)


# driver.execute_script("window.scrollTo(0, 200)")
# time.sleep(2)
# print("scrolled 200px")
# print("")

########################### TestCase 14:iframe for youtube #########################

# print("TestCase #14:")

# required_frame = driver.find_element(By.XPATH,"")
# driver.switch_to.frame(required_frame) 

# element = driver.find_element(By.XPATH,"//button[@aria-label='Play']")
# element.click()

# print("YouTube video played ✔️")


# time.sleep(10)
# stop = driver.find_element(By.XPATH,"/html/body/div/div/div[1]/video").click()
# print("Pause Video ✔️\n")
# time.sleep(1.5)


# driver.refresh()
# time.sleep(3)
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# print("page refreshed & Scrolled down ✔️\n")
# time.sleep(4)
########################### TestCase 15:Jobs at Angel.co Portal #########################

print("TestCase #15:")

# driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/div[2]/ul/li[2]/a").click()
# print("Jobs at Angel.co Portal page:- Success ✔️\n")
# time.sleep(10)


########################### TestCase 16:Jobs at Tech in Asia Portal #########################

print("TestCase #16:")

# driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/div[2]/ul/li[3]/a").click()
# print("Jobs at Tech in Asia Portal page:- Success ✔️\n")
# time.sleep(10)


########################### TestCase 17: AINE AI page #########################

print("TestCase #17:")

# driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/div[1]/ul/li[2]/a").click()
# print("AINE AI page:- Success ✔️\n")
# time.sleep(8)

########################### TestCase 18:Xaltius Page ##################

print("TestCase #18:")
# driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/div[1]/ul/li[1]/a").click()
# print("Xaltius page:- Success ✔️\n")
# time.sleep(5)

########################### TestCase 19:TSF Global Page ##################

print("TestCase #18:")
# driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/div[4]/ul/li[1]/a").click()
# print("Sparks Foundation Global Page:- Success ✔️\n")
# time.sleep(5)
