#-*- coding: UTF-8 -*-
import pytest
from page.Termsofservice_page import Termsofservicepage
from page.Login_page import LoginPage
from page.common import WebDriver

class TestTermsofservice:
    """
    查看协议
    """

    def test_Termsof(self, browser):
        """
        查看服务条款
        :param browser:
        :return:
        """
        pages = LoginPage(browser)
        page = Termsofservicepage(browser)
        page.get("http://pre.yunmeetings.com")
        pages.account_bnt.click()
        print("点击账号登录")
        page.register_bnt.click()
        print("点击注册新账号")
        page.register_num.click()
        print("手机号注册")
        page.terms_service.click()
        print("服务条款")
        page.wait(2)
        page.switch_Windows()
        print("跳转到服务条款页面")
        success = page.judge.text
        assert success == "企云会服务协议"

    if __name__ == '__main__':
        pytest.main(["-v", "-s", "test_Termsofservices.py::TestTermsofservice",  "--html", "../report_test/report.html"])