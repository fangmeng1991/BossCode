from pages.test_page.base_page import *
from selenium.webdriver.common.action_chains import  ActionChains


class UserPage(BasePage):
    # 进入用户中心
    def user(self):
        above = self.driver.find_element_by_class_name("user-operate")  # 鼠标悬停
        ActionChains(self.driver).move_to_element(above).perform()
        #self.driver.find_element_by_id("manage").click()
        self.driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[1]/div[2]/ul/li[2]/div[2]/ul/li[2]/a").click()
        #点击我的企业

    def my_business(self):
        #search_window = self.driver.current_window_handle  # 此行代码用来定位当前页面
        self.driver.find_element_by_link_text("我的企业").click()
