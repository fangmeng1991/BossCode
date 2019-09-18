from pages.test_page.base_page import *
class HomePage(BasePage):
    #富集云
    def fujiyun(self):
        self.driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[1]/div[2]/div/ul/li[1]/a").click()
    #工业移动网
    def gongye(self):
        self.driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[1]/div[2]/div/ul/li[2]/a").click()
    #雾小脑
    def wuxiaonao(self):
        self.driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[1]/div[2]/div/ul/li[3]/a").click()
    #工业网关
    def wangguan(self):
        self.driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[1]/div[2]/div/ul/li[4]/a").click()
    #行业专业云
    def hangye(self):
        self.driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[1]/div[2]/div/ul/li[5]/a").click()
    #富能云商城
    def funengyun(self):
        self.driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[1]/div[2]/div/ul/li[6]/a").click()
    #平台应用
    def pingtai(self):
        self.driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[1]/div[2]/div/ul/li[7]/a").click()
    #合作伙伴
    def hezuo(self):
        self.driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[1]/div[2]/div/ul/li[8]/a").click()
    #开发者中心
    def kaifazhe(self):
        self.driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[1]/div[2]/div/ul/li[9]/a").click()