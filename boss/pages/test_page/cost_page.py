from pages.test_page.base_page import *
from selenium.webdriver.common.action_chains import  ActionChains
class CostPage(BasePage):
    #进入费用中心
    def charge(self):
        search_window = self.driver.current_window_handle  # 此行代码用来定位当前页面
        above = self.driver.find_element_by_class_name("user-operate")  # 鼠标悬停
        ActionChains(self.driver).move_to_element(above).perform()
        self.driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div/div[2]/div/ul/li[10]/div[2]/ul/li[3]/a").click()
    #点击费用总览
    def charge_center(self):
        self.driver.dind_element_by_link_test("费用总览").click()

    #点击收支明细
    def charge_seal(self):
        self.driver.dind_element_by_link_test("收支明细").click()

    #点击订单管理
    def charge_orderlist(self):
        self.driver.dind_element_by_link_test("订单管理").click()

    #点击代金券管理
    def charge_cash(self):
        self.driver.dind_element_by_link_test("代金券管理").click()
