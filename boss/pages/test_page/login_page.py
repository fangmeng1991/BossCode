from pages.test_page.base_page import *
from time import sleep
class LoginPage(BasePage):
    def login(self,username,password):
        # 公网生产环境
        self.driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[1]/div[2]/div/ul/li[10]/a").click()
        #self.driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div/div[2]/div/ul/li[6]/a").click()
        sleep(2)
        # 公网生产环境
        self.driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/form[2]/div[3]/div/span").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/form[1]/div[1]/div/div/input").send_keys(username)

        self.driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/form[1]/div[2]/div/div/input").send_keys(password)
        #captha = input("请输入验证码")
        #self.driver.find_element_by_name("code").send_keys(captha)
        #self.driver.find_element_by_name("code").send_keys("ddac905438d61eaeb6dbf1827c80f0d4")
        self.driver.find_element_by_name("code").send_keys("ddac")
        self.driver.find_element_by_tag_name("button").click()