#-*- coding: UTF-8 -*-
import pytest
from page.Console_page import Consolepage
from page.Personaldata_page import PersonaldataPage
from test_case import test_ALogin
from test_case import test_Console

class TestConsoleout:
    """
    退出控制台
    """

    def test_consoleout(self, browser):
        """
        退出登录
        :param brower:
        :return:
        """
        # 测试代码
        test_ALogin.Testlogin.test_login(self, "18210785192", "zl123456", browser)
        test_Console.TestConsolelogin.test_conlogin(self,  browser, "zl123456")

        # 正式代码
        page = Consolepage(browser)
        pages = PersonaldataPage(browser)
        pages.username_bnt.click()
        print("点击用户名")
        page.console_out.click()
        print("退出控制台")
        assert page.out_assert.text[0:2] == "首页"


    if __name__ == '__main__':
        pytest.main(["-v", "-s", "test_ConsoleOut.py::TestConsoleout", "--html", "../report_test/report.html"])

