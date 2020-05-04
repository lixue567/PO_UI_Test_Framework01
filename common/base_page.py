import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.log_utils import logger

class BasePage(object):
    def __init__(self,driver):
        self.driver = driver

    # �����������װ -- > ���η�װ
    def open_url(self,url):
        self.driver.get( url )
        logger.info('��url��ַ %s '% url )

    def set_browser_max(self):
        self.driver.maximize_window()
        logger.info('������������')

    def set_browser_min(self):
        self.driver.minimize_window()
        logger.info('�����������С��')

    def refresh(self):
        self.driver.refresh()
        logger.info('�����ˢ�²���')

    def get_title(self):
        value = self.driver.title
        logger.info('��ȡ��ҳ���⣬������%s'%value)
        return value
    #.....

    #Ԫ�ز�����װ
    # element_info = {'element_name':'�û��������','locator_type':'xpath','locator_value':'//input[@name="account"]','timeout': 5 }
    def find_element(self,element_info):
        locator_type_name = element_info['locator_type']
        locator_value_info = element_info['locator_value']
        locator_timeout = element_info['timeout']
        if locator_type_name == 'id':
            locator_type = By.ID
        elif locator_type_name == 'name':
            locator_type = By.NAME
        elif locator_type_name == 'class':
            locator_type = By.CLASS_NAME
        elif locator_type_name == 'xpath':
            locator_type = By.XPATH
        element = WebDriverWait(self.driver , locator_timeout)\
            .until(lambda x:x.find_element(locator_type,locator_value_info))
        logger.info('[%s]Ԫ��ʶ��ɹ�'%element_info['element_name'])
        # element = WebDriverWait(self.driver, locator_timeout)\
        #     .until(EC.presence_of_element_located((locator_type, locator_value_info)))
        return element

    def click(self,element_info):
        element = self.find_element(element_info)
        element.click()
        logger.info('[%s]Ԫ�ؽ��е������'%element_info['element_name'])

    def input(self,element_info,content):
        element = self.find_element(element_info)
        element.send_keys(content)
        logger.info('[%s]Ԫ���������ݣ�%s' %(element_info['element_name'],content))


