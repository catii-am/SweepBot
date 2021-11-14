import random
import requests
import wheel
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from fake_useragent import UserAgent
import time
from proxylist import proxy_list
from gmail import email_list
from wallet import wallet_list

link = 'https://sweepwidget.com/view/35441-r26ut0a5/olyus8-35441'

#options UserAgent
#useragent = UserAgent()
options = webdriver.ChromeOptions()
#options.add_argument(f"user-agent={useragent.chrome}")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-data-dir=C:\\Users\\ddd\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
driver = webdriver.Chrome(
    executable_path='chromedriver/123.exe',
    options=options
)

#option proxy




try:
    gmail = random.choice(email_list)
    driver.execute_script("var s=window.document.createElement('script'); s.src='javascript.js';window.document.head.appendChild(s);")
    driver.get('chrome://settings/clearBrowserData')
    print('История очищена')
    time.sleep(15)


    driver.get(link)
    print(link + ' загружена')
    time.sleep(5)
    name_input = driver.find_element_by_name('sw__login_name')
    name_input.clear()
    name_input.send_keys(gmail)
    #name_input.send_keys('vaszaycev2000@gmail.com')
    print('Имя введено')

    email_input = driver.find_element_by_name('sw__login_email')
    email_input.clear()
    email_input.send_keys(gmail)
    #email_input.send_keys('vaszaycev2000@gmail.com')
    print('Почта введена')
    time.sleep(3)

    login_button = driver.find_element_by_id('sw_login_button')
    login_button.click()
    time.sleep(1)
    if(driver.find_element_by_id('sw_entry_amount_allowed_text')):
        print('Антиспам')
        driver.close()
        driver.quit()
    else:
        time.sleep(300)

    #tg_follow = driver.find_by_


except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()