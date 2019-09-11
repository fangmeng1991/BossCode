from pages.test_page.base_page import *
from time import sleep
class LoginPage(BasePage):
    def login(self,username,password):
        #self.driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[1]/div[2]/div/ul/li[10]/a").click() #公网生产环境
        self.driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div/div[2]/div/ul/li[6]/a").click()
        sleep(2)
        search_window = self.driver.current_window_handle
        #self.driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/form[2]/div[3]/div/span").click() #公网生产环境
        sleep(2)
        search_window = self.driver.current_window_handle
        self.driver.find_element_by_name("username").send_keys(username)
        self.driver.find_element_by_name("password").send_keys(password)
        #captha = input("请输入验证码")
        #self.driver.find_element_by_name("code").send_keys(captha)
        self.driver.find_element_by_name("code").send_keys("ddac905438d61eaeb6dbf1827c80f0d4")
        self.driver.find_element_by_tag_name("button").click()