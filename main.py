import random
import requests
from bs4 import BeautifulSoup
import keyboard

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from fake_useragent import UserAgent
import time
from proxylist import proxy_list
from gmail import email_list
from wallet import wallet_list
from usernames import username_list

link = 'https://sweepwidget.com/view/38759-935rjsty/d3fsdz-38759'

#options UserAgent
#useragent = UserAgent()
options = webdriver.ChromeOptions()
#options.add_argument(f"user-agent={useragent.chrome}")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-data-dir=C:\\Users\\catii\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
driver = webdriver.Chrome(
    executable_path='chromedriver/123.exe',
    options=options
)

#option proxy

i = 1


try:
    while i < 30:
        gmail = random.choice(email_list)
        # gmail = 'ickinsbrantwalk@gmail.com'
        wallet = random.choice(wallet_list)
        # wallet = '0x57a72B83E1F7aAe63B5a28080AD7666F7fabBc03'
        username = random.choice(username_list)
        driver.execute_script(
            "var s=window.document.createElement('script'); s.src='javascript.js';window.document.head.appendChild(s);")
        driver.get("chrome://settings/clearBrowserData")

        time.sleep(5)
        print('История очищена')
        driver.switch_to.window(driver.window_handles[0])

        driver.get(link)
        print(link + ' Загружена')
        time.sleep(10)
        name_input = driver.find_element_by_name('sw__login_name')
        name_input.clear()
        name_input.send_keys(gmail)
        print('Имя ' + gmail + ' введено')

        email_input = driver.find_element_by_name('sw__login_email')
        email_input.clear()
        email_input.send_keys(gmail)
        print('Почта ' + gmail + ' введена')

        wallet_input = driver.find_element_by_name('sw_text_input_3_1')
        wallet_input.clear()
        wallet_input.send_keys(wallet)
        print('Кошелек ' + wallet + ' введен')

        login_button = driver.find_element_by_id('sw_login_button')
        login_button.click()
        print('Залогинился')
        time.sleep(5)

        # mission 1
        main_tg_1 = driver.find_element_by_id('sw_entry_telegram_join_channel_2_1')
        main_tg_1.click()
        time.sleep(1)
        main_tg_1_2 = driver.find_element_by_id('sw_link_telegram_join_channel_2_1')
        main_tg_1_2.click()
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        main_tg = driver.find_element_by_id('sw_telegram_join_channel_2_1')
        main_tg.clear()
        main_tg.send_keys(username)
        time.sleep(2)
        main_tg_verify = driver.find_element_by_id('sw_verify_telegram_join_channel_2_1')
        main_tg_verify.click()
        time.sleep(2)
        print('Задание выполнено')

        # mission 2
        annonce_tg_1 = driver.find_element_by_id('sw_entry_h_telegram_join_channel_4_1')
        annonce_tg_1.click()
        time.sleep(1)
        annonce_tg_1_2 = driver.find_element_by_id('sw_link_telegram_join_channel_4_1')
        annonce_tg_1_2.click()
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        annonce_tg = driver.find_element_by_id('sw_telegram_join_channel_4_1')
        annonce_tg.clear()
        annonce_tg.send_keys(username)
        time.sleep(2)
        annonce_tg_verefy = driver.find_element_by_id('sw_verify_telegram_join_channel_4_1')
        annonce_tg_verefy.click()
        time.sleep(2)
        print('Задание выполнено')

        # mission3
        follow_twitter_1 = driver.find_element_by_id('sw_entry_twitter_follow_6_1')
        follow_twitter_1.click()
        time.sleep(1)
        follow_twitter_1_2 = driver.find_element_by_id('sw_input_row_2_twitter_follow_6_1')
        follow_twitter_1_2.click()
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        follow_twitter = driver.find_element_by_id('sw_twitter_follow_6_1')
        follow_twitter.clear()
        follow_twitter.send_keys(username)
        time.sleep(2)
        follow_twitter_verefy = driver.find_element_by_id('sw_verify_twitter_follow_6_1')
        follow_twitter_verefy.click()
        time.sleep(2)
        print('Задание выполнено')

        # mission 4
        retweet_1 = driver.find_element_by_id('sw_entry_twitter_retweet_7_1')
        retweet_1.click()
        time.sleep(1)
        retweet_1_2 = driver.find_element_by_id('sw_link_twitter_retweet_7_1')
        retweet_1_2.click()
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        retweet = driver.find_element_by_id('sw_twitter_retweet_7_1')
        retweet.clear()
        retweet.send_keys(username)
        time.sleep(2)
        retweet_verefy = driver.find_element_by_id('sw_verify_twitter_retweet_7_1')
        retweet_verefy.click()
        time.sleep(2)
        print('Задание выполнено')

        # mission 5
        tg_first_1 = driver.find_element_by_id('sw_entry_telegram_join_channel_12_1')
        tg_first_1.click()
        time.sleep(1)
        tg_first_1_2 = driver.find_element_by_id('sw_link_telegram_join_channel_12_1')
        tg_first_1_2.click()
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        tg_first = driver.find_element_by_id('sw_telegram_join_channel_12_1')
        tg_first.clear()
        tg_first.send_keys(username)
        time.sleep(2)
        tg_first_verefy = driver.find_element_by_id('sw_verify_telegram_join_channel_12_1')
        tg_first_verefy.click()
        time.sleep(2)

        # mission 6
        tg_second_1 = driver.find_element_by_id('sw_entry_telegram_join_channel_10_1')
        tg_second_1.click()
        time.sleep(1)
        tg_second_1_2 = driver.find_element_by_id('sw_link_telegram_join_channel_10_1')
        tg_second_1_2.click()
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        tg_second = driver.find_element_by_id('sw_telegram_join_channel_10_1')
        tg_second.clear()
        tg_second.send_keys(username)
        time.sleep(2)
        tg_second_verefy = driver.find_element_by_id('sw_verify_telegram_join_channel_10_1')
        tg_second_verefy.click()
        print('Задание выполнено')
        print('Меняй ip')
        time.sleep(5)
        time.sleep(10)
        print('выключай РП')
        time.sleep(10)
        i += 1



except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()