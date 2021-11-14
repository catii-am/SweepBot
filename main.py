import random
import requests
from bs4 import BeautifulSoup
import keyboard

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from fake_useragent import UserAgent
import time
from proxylist import proxy_list
from gmail import email_list
from wallet import wallet_list
from usernames import username_list

link = 'https://sweepwidget.com/view/38759-935rjsty/d3fsdz-38759'

i = 1         #НЕ ТРОГАТЬ
b = 30        #КОЛЛИЧЕСТВО ПОВТОРОВ





try:
    while i < b:
        # options UserAgent
        useragent = UserAgent()
        options = webdriver.ChromeOptions()
        options.add_argument(f"user-agent={useragent.chrome}")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--disable-blink-features=AutomationControlled")
        # options.add_argument("user-data-dir=C:\\Users\\dd\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
        driver = webdriver.Chrome(
            executable_path='chromedriver/123.exe',
            options=options
        )
        gmail = random.choice(email_list)
        wallet = random.choice(wallet_list)
        username = random.choice(username_list)
        driver.execute_script(
            "var s=window.document.createElement('script'); s.src='javascript.js';window.document.head.appendChild(s);")
        # driver.get("chrome://settings/clearBrowserData")
        #
        # time.sleep(3)
        # print('История  очищена')
        driver.switch_to.window(driver.window_handles[0])


        driver.get(link)
        print(link + ' загружена')
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "sw__login_name"))
        )
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
        time.sleep(2)



        # mission 4
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "sw_entry_twitter_retweet_7_1"))
        )
        retweet_1 = driver.find_element_by_id('sw_entry_twitter_retweet_7_1')
        retweet_1.click()
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "sw_link_twitter_retweet_7_1"))
        )
        time.sleep(1)
        retweet_1_2 = driver.find_element_by_id('sw_link_twitter_retweet_7_1')
        retweet_1_2.click()
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        retweet = driver.find_element_by_id('sw_twitter_retweet_7_1')
        retweet.clear()
        retweet.send_keys(username)
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "sw_verify_twitter_retweet_7_1"))
        )
        retweet_verefy = driver.find_element_by_id('sw_verify_twitter_retweet_7_1')
        retweet_verefy.click()
        print('Задание выполнено')

        # mission3
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "sw_entry_twitter_follow_6_1"))
        )
        follow_twitter_1 = driver.find_element_by_id('sw_entry_twitter_follow_6_1')
        follow_twitter_1.click()
        time.sleep(1)
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "sw_input_row_2_twitter_follow_6_1"))
        )
        follow_twitter_1_2 = driver.find_element_by_id('sw_input_row_2_twitter_follow_6_1')
        follow_twitter_1_2.click()
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        follow_twitter = driver.find_element_by_id('sw_twitter_follow_6_1')
        follow_twitter.clear()
        follow_twitter.send_keys(username)
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "sw_verify_twitter_follow_6_1"))
        )
        follow_twitter_verefy = driver.find_element_by_id('sw_verify_twitter_follow_6_1')
        follow_twitter_verefy.click()
        print('Задание выполнено')

        # mission 2
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "sw_entry_h_telegram_join_channel_4_1"))
        )
        annonce_tg_1 = driver.find_element_by_id('sw_entry_h_telegram_join_channel_4_1')
        annonce_tg_1.click()
        time.sleep(1)
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "sw_link_telegram_join_channel_4_1"))
        )
        annonce_tg_1_2 = driver.find_element_by_id('sw_link_telegram_join_channel_4_1')
        annonce_tg_1_2.click()
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        annonce_tg = driver.find_element_by_id('sw_telegram_join_channel_4_1')
        annonce_tg.clear()
        annonce_tg.send_keys(username)
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "sw_verify_telegram_join_channel_4_1"))
        )
        annonce_tg_verefy = driver.find_element_by_id('sw_verify_telegram_join_channel_4_1')
        annonce_tg_verefy.click()
        print('Задание выполнено')

        # mission 1
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "sw_entry_telegram_join_channel_2_1"))
        )
        main_tg_1 = driver.find_element_by_id('sw_entry_telegram_join_channel_2_1')
        main_tg_1.click()
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "sw_link_telegram_join_channel_2_1"))
        )
        time.sleep(1)
        main_tg_1_2 = driver.find_element_by_id('sw_link_telegram_join_channel_2_1')
        main_tg_1_2.click()
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        main_tg = driver.find_element_by_id('sw_telegram_join_channel_2_1')
        main_tg.clear()
        main_tg.send_keys(username)
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "sw_verify_telegram_join_channel_2_1"))
        )
        main_tg_verify = driver.find_element_by_id('sw_verify_telegram_join_channel_2_1')
        main_tg_verify.click()
        print('Задание выполнено')


        time.sleep(4)



        # mission 6
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "sw_entry_telegram_join_channel_10_1"))
        )
        tg_second_1 = driver.find_element_by_id('sw_entry_telegram_join_channel_10_1')
        tg_second_1.click()
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "sw_link_telegram_join_channel_10_1"))
        )
        time.sleep(1)
        tg_second_1_2 = driver.find_element_by_id('sw_link_telegram_join_channel_10_1')
        tg_second_1_2.click()
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        tg_second = driver.find_element_by_id('sw_telegram_join_channel_10_1')
        tg_second.clear()
        tg_second.send_keys(username)
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "sw_verify_telegram_join_channel_10_1"))
        )
        tg_second_verefy = driver.find_element_by_id('sw_verify_telegram_join_channel_10_1')
        tg_second_verefy.click()
        print('Задание выполнено')

        # mission 5
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "sw_entry_telegram_join_channel_12_1"))
        )
        tg_first_1 = driver.find_element_by_id('sw_entry_telegram_join_channel_12_1')
        tg_first_1.click()
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "sw_link_telegram_join_channel_12_1"))
        )
        time.sleep(1)
        tg_first_1_2 = driver.find_element_by_id('sw_link_telegram_join_channel_12_1')
        tg_first_1_2.click()
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        tg_first = driver.find_element_by_id('sw_telegram_join_channel_12_1')
        tg_first.clear()
        tg_first.send_keys(username)
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "sw_verify_telegram_join_channel_12_1"))
        )
        tg_first_verefy = driver.find_element_by_id('sw_verify_telegram_join_channel_12_1')
        tg_first_verefy.click()
        print('Задания выполнены!')
        time.sleep(8)
        driver.quit()
        # print('Включи РП')
        # time.sleep(5)
        # time.sleep(10)
        # print('Выключи РП')
        # time.sleep(10)
        i += 1
        if i == 5:
          print('смени IP')



except Exception as ex:
    print(ex)
    pass

finally:
    driver.close()
    driver.quit()