import unittest
from common.browser_engine import BrowserEngine
from pages.test_page.home_page import *
from pages.test_page.login_page import *
class TestHome(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("test start")
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)
    @classmethod
    def tearDown(self):
        print("test end")
        self.driver.quit()

    def test_case001(self):
        loginpage = LoginPage(self.driver)
        loginpage.login('guimo151', 'guimo1')
        homepage =HomePage(self.driver)
        homepage.fujiyun()
        t =format(self.driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div[1]/p[2]/a").text)
        self.assertEqual(u"进一步了解  ",t)
        BasePage.get_windows_img(self)  # 调用基类截图方法
        #self.assertText(u"",)
    def test_case002(self):
        loginpage = LoginPage(self.driver)
        loginpage.login('guimo151', 'guimo1')
        sleep(2)
        homepage = HomePage(self.driver)
        homepage.gongye()
        t = format(self.driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div/div/div[1]').text)
        self.assertEqual(u"工业移动网",t,msg="Test Fail")
        BasePage.get_windows_img(self)  # 调用基类截图方法
    def test_case003(self):
        loginpage = LoginPage(self.driver)
        loginpage.login('guimo151', 'guimo1')
        sleep(2)
        homepage = HomePage(self.driver)
        homepage.wuxiaonao()
        t = format(self.driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[1]/div/a[1]/div[2]/span").text)
        self.assertEqual(u"Nadder 12Core CPU / 128G 内存 / 16T 硬盘",t,msg="Test Fail")
        BasePage.get_windows_img(self)  # 调用基类截图方法

    def test_case004(self):
        loginpage = LoginPage(self.driver)
        loginpage.login('guimo151', 'guimo1')
        homepage = HomePage(self.driver)
        homepage.wangguan()
        #判断/html/body/div/div[1]/div[2]/div[1]/div/a[1]/div[2]/span处元素的文本是否为Sirius Plus
        t = format(self.driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[1]/div/a[1]/div[2]/span").text)
        self.assertEqual(u"Sirius Plus",t,msg="Test Fail")
        BasePage.get_windows_img(self)  # 调用基类截图方法

    def test_case005(self):
        loginpage = LoginPage(self.driver)
        loginpage.login('guimo151', 'guimo1')
        homepage = HomePage(self.driver)
        homepage.hangye()
        t = format(self.driver.find_element_by_xpath("/html/body/div/div[1]/div/div[2]/div/div[1]/a/p").text)
        self.assertEqual(u"刀具云",t,msg="Test Fail")
        BasePage.get_windows_img(self)  # 调用基类截图方法

    def test_case006(self):
        loginpage = LoginPage(self.driver)
        loginpage.login('guimo151', 'guimo1')
        homepage = HomePage(self.driver)
        homepage.funengyun()
        t = format(self.driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[1]/div/ul/li[1]/a/p").text)
        self.assertEqual(u"富博士（咨询服务）",t,msg="Test Fail")
        BasePage.get_windows_img(self)  # 调用基类截图方法

    def test_case007(self):
        loginpage = LoginPage(self.driver)
        loginpage.login('guimo151', 'guimo1')
        homepage = HomePage(self.driver)
        homepage.pingtai()
        t = format(self.driver.find_element_by_xpath('//*[@id="applicationPlatform"]/div[2]/div/div[1]/a/div/p').text)
        self.assertEqual(u"CorePro",t,msg="Test Fail")
        BasePage.get_windows_img(self)  # 调用基类截图方法

    def test_case008(self):
        loginpage = LoginPage(self.driver)
        loginpage.login('guimo151', 'guimo1')
        homepage = HomePage(self.driver)
        homepage.hezuo()
        t = format(self.driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/a').text)
        self.assertEqual(u"合作伙伴体系",t,msg="Test Fail")
        BasePage.get_windows_img(self)  # 调用基类截图方法

    def test_case009(self):
        loginpage = LoginPage(self.driver)
        loginpage.login('guimo151', 'guimo1')
        homepage = HomePage(self.driver)
        homepage.kaifazhe()
        sleep(5)
        search_window = self.driver.current_window_handle
        t=self.driver.current_url
        print(t)
        BasePage.get_windows_img(self)  # 调用基类截图方法

    if __name__ == '__main__':
        unittest.main()
