import unittest
from common.browser_engine import BrowserEngine
from pages.test_page.uesr_page import *
from pages.test_page.login_page import *
class TestUser(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("test start")
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)
    @classmethod
    def tearDown(self):
        print("test end")
        self.driver.quit()

    def cass0001(self):
        loginpage = LoginPage(self.driver)
        loginpage.login('guimo151', 'guimo1')
        userpage = UserPage(self.driver)
        userpage.user()
        BasePage.get_windows_img(self)  # 调用基类截图方法

    if __name__ == '__main__':
        unittest.main()