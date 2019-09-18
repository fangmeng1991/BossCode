from pages.test_page.base_page import *
from selenium.webdriver.common.action_chains import  ActionChains


class ProviderPage(BasePage):
    def manage(self):
        search_window = self.driver.current_window_handle  # 此行代码用来定位当前页面
        above = self.driver.find_element_by_class_name("user-operate")  # 鼠标悬停
        ActionChains(self.driver).move_to_element(above).perform()
        self.driver.find_element_by_id("manage").click()


    #点击我的信息
    def myinfo(self):
        self.driver.find_element_by_xpath('//*[@id="primaryNavbar"]/ul/li[1]/a').click()


    #点击产品管理
    def product(self):
        self.driver.find_element_by_xpath('//*[@id="primaryNavbar"]/ul/li[2]/a').click()
        self.driver.find_element_by_xpath('/html/body/div/div/ul/li[1]/a').click()
        self.driver.find_element_by_xpath('/html/body/div/div/ul/li[2]/a').click()
        self.driver.find_element_by_xpath('/html/body/div/div/ul/li[3]/a').click()
        self.driver.find_element_by_xpath('/html/body/div/div/ul/li[4]/a').click()
        self.driver.find_element_by_xpath('/html/body/div/div/ul/li[5]/a').click()


    #点击订单管理
    def order(self):
        self.driver.find_element_by_xpath('//*[@id="primaryNavbar"]/ul/li[3]/a').click()
        self.driver.find_element_by_xpath('/html/body/div/div/ul/li[1]/a').click()
        self.driver.find_element_by_xpath('/html/body/div/div/ul/li[2]/a').click()
        self.driver.find_element_by_xpath('/html/body/div/div/ul/li[3]/a').click()
        self.driver.find_element_by_xpath('/html/body/div/div/ul/li[4]/a').click()


    #点击应用管理
    def management(self):
        self.driver.find_element_by_xpath('//*[@id="primaryNavbar"]/ul/li[4]/a').click()

