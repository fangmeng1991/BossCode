from selenium import webdriver
from time import sleep
import unittest
from common.browser_engine import BrowserEngine
from pages.test_page.base_page import *
from pages.test_page.login_page import *
class TestLogin(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("test start")
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)
    @classmethod
    def tearDown(self):
        self.driver.quit()
    def test_login_success(self):
        #self.test_login('sqa0001','sqa123456')
        loginpage = LoginPage(self.driver)
        loginpage.login('testfii1', 'testfii2019')
        sleep(2)
        BasePage.get_windows_img(self)  # 调用基类截图方法
        #self.test_login('guimo151','guimo1')

        #title =self.driver.title
        #print(title)
        #self.assertEqual(title,"富士康工业互联网",msg="fail")
        try:
            assert '富集云' in self.driver.title
            print('Test Pass.')
        except Exception as e:
            print('Test Fail.', format(e))
    def test_admin(self,driver):
        # 登录
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").send_keys("Admin@134")
        captha = input("请输入验证码")
        driver.find_element_by_name("code").send_keys(captha)
        driver.find_element_by_tag_name("button").click()
        sleep(2)
        #driver.get("https://www.fii-icloud.com/admin.php")
        driver.get("https://www.fiibeacontest.xyz/admin.php")



    if __name__ == '__main__':
        unittest.main()