from pages.test_page.base_page import *
from selenium.webdriver.common.action_chains import  ActionChains


class ProductPage(BasePage):
    def product(self):
        search_window = self.driver.current_window_handle  # 此行代码用来定位当前页面
        above = self.driver.find_element_by_class_name("user-operate")  # 鼠标悬停
        ActionChains(self.driver).move_to_element(above).perform()
        self.driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div/div[2]/div/ul/li[10]/div[2]/ul/li[4]/a").click()


    #点击我的产品
    def product_saas(self):
        self.driver.dind_element_by_link_test("我的产品").click()


    #点击我的微服务
    def product_service(self):
        self.driver.dind_element_by_link_test("我的微服务").click()


    #点击云资源管理
    def product_paas(self):
        self.driver.dind_element_by_link_test("云资源管理").click()
