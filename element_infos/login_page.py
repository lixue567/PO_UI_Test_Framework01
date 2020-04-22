import os
from selenium import webdriver
from selenium.webdriver.common.by import By

current_path = os.path.dirname(__file__)
driver_path = os.path.join(current_path,'../webdriver/chromedriver')

class LoginPage(object):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('http://106.53.50.202:8999/zentao4/www/my/')
        #属性 页面上的控件
        #用户名
        self.username_inputbox = self.driver.find_element(By.XPATH,'//input[@id="account"]')
        #密码
        self.password_inputbox = self.driver.find_element(By.XPATH,'//input[@name="password"]')
        self.keeplogin_checkbox = self.driver.find_element(By.XPATH,'//input[@id="keepLoginon"]')
        self.login_button = self.driver.find_element(By.XPATH,'//button[@id="submit"]')
        self.forgetpassword_link = None
    #方法：控件的操作
    def input_username(self,username):
        self.username_inputbox.send_keys(username)

    def input_password(self,password):
        self.password_inputbox.send_keys(password)

    def click_login(self):
        self.login_button.click()

if __name__ == "__main__":
    login_page = LoginPage()
    login_page.input_username('lixue')
    login_page.input_password('lixue@123')
    login_page.click_login()


