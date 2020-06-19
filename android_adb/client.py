# -*- coding: utf-8 -*-
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time, random, re
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import datetime

# Appium 基本参数
PLATFORM = 'Android'
DEVICE_NAME = 'ONEPLUS A5000'
DRIVER_SERVER = 'http://127.0.0.1:4723/wd/hub'
TIMEOUT = 800
NORESET = 'True'
FLICK_STRAT_X = 300
FLICK_START_Y = 300
FLICK_DISTANCE = 700


class Automation(object):
    # 初始化 Appium 基本参数
    def __init__(self, APP_PACKAGE, APP_ACTIVITY):
        self.desired_caps = {
            'platformName': PLATFORM,
            "platformVersion": "10.0.0",
            'deviceName': DEVICE_NAME,
            'appPackage': APP_PACKAGE,
            'appActivity': APP_ACTIVITY,
            'noReset': NORESET,
            'newCommandTimeout': TIMEOUT,
        }
        print('打开 appium 服务器...')
        print('配置 appium ...')
        self.driver = webdriver.Remote(DRIVER_SERVER, self.desired_caps)
        # self.wait = WebDriverWait(self.driver, 10)
        self.size = self.driver.get_window_size()
        print(self.size)


a = Automation("com.tencent.mm", ".ui.LauncherUI")

