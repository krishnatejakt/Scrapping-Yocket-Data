from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome('C:\\Users\\krishnateja\\Downloads\\chromedriver_win32\\chromedriver.exe') #replace this with exectuable path
browser.get('https://yocket.in/account/login')
time.sleep(2)

#login = browser.find_element_by_xpath("//a[@href='/account/login']")
#login.click()

username = browser.find_element_by_xpath("//input[@name='email']")
username.send_keys('xxxxxxxxxxxxxxxxx') #replace with your email id
time.sleep(2)

next_btn = browser.find_element_by_xpath("//button[@id='users_login_email']")
next_btn.click()
time.sleep(2)

password = browser.find_element_by_xpath("//input[@name='password']")
password.send_keys('xxxxxxxxxxxxxxxxx') #replace with your password

signin_btn = browser.find_element_by_xpath("//button[@id='users_login_password']")
signin_btn.click()
time.sleep(2)

search_btn = browser.find_element_by_xpath("//input[@id='search-input']")
search_btn.send_keys('suny buffalo') # replace this with your desired university
time.sleep(2)
search_btn.send_keys(Keys.ARROW_DOWN)
search_btn.send_keys(Keys.RETURN)

admits_rejects =  browser.find_element_by_xpath("//a[@href='/applications-admits-rejects/state-university-of-new-york-at-buffalo/2']")
admits_rejects.click()

#for elem in browser.find_elements_by_xpath('.//div[@class = "row text-center"]'):
#       print(elem.text, end =" ")
time.sleep(2)

for i in range(2,20):# Number of Pages you change this.
    time.sleep(1)
    url = "//a[@href='/applications-admits-rejects/state-university-of-new-york-at-buffalo/2?page={}']".format(i) #inspect the page and check for the link.
    admits_rejects =  browser.find_element_by_xpath(url)
    admits_rejects.click()
    time.sleep(2)
    x = []
    for y in browser.find_elements_by_xpath('.//small'):
        if 'NEW' not in y.text:
            x.append(y.text)
    i = 0
    for elem in browser.find_elements_by_xpath('.//div[@class = "row text-center"]'):
        print(x[i]+' '+elem.text)
        with open('admits.txt','a+') as f:
            f.write(x[i])
            f.write('\n'+elem.text+'\n') 
        i+=1

