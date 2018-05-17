#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
import time

URL = 'https://www.simuwang.com'

user='XXX'
passwd='XXX'

driver = webdriver.Chrome()

#访问链接
driver.get(URL)
time.sleep(2)

# 获取当前窗口的句柄
now_handle = driver.current_window_handle
print('当前主窗口句柄',now_handle)

# 点击 红包什么
try:
    # 点击 红包
    driver.find_element_by_xpath('//*[@id="close-btn"]').click()
    print("click success")
    time.sleep(0.5)
    # 点击 登录
    driver.find_element_by_xpath('//*[@id="topAll"]/div/div[2]/a[1]').click()
    print("登录界面")
    time.sleep(2)
except Exception as e:
    print(e)

action = action_chains.ActionChains(driver)

# sign in the user name and password
try:
    print("弹出界面信息")
    # user name
    gr_input_nickname = driver.find_element_by_xpath('//input[@id="gr_input_nickname"]')
    gr_input_nickname.send_keys(user)

    gr_input_nickname.send_keys(Keys.TAB) # tab over to not-visible element

    gr_input_pwd1 = driver.find_element_by_xpath('//input[@id="gr_input_pwd2"]')
    gr_input_pwd1.send_keys(passwd)
    print('登录填充用户名和密码')
    driver.find_element_by_xpath('//*[@id="gr-login-btn"]').click()
    time.sleep(10)

except Exception as e:
    print(e)


