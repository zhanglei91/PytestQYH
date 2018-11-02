#-*- coding: UTF-8 -*-
import pytest
from page.Login_page import LoginPage
from test_case import test_ALogin
from page.Personaldata_page import PersonaldataPage

class TestLoginOut:
    """
    退出
    """
    def test_loginout(self, browser):
        """
        退出
        :return:
        """

        # 正式代码
        page = LoginPage(browser)
        pages = PersonaldataPage(browser)
        # 测试代码
        test_ALogin.Testlogin.test_login(self, "18210785192", "zl123456", browser)
        # 复用个人资料中定位到的“用户名”元素
        pages.username_bnt.click()
        print("点击用户名")
        page.loginout_bnt.click()
        page.wait(2)
        print("点击退出登录")


if __name__ == '__main__':

    pytest.main(["-v", "-s", "test_LoginOut.py::TestLoginOut"])