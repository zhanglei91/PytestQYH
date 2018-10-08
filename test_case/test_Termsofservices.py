import pytest
from page.Termsofservice_page import Termsofservicepage
from page.common import WebDriver

class Termsofservice:

    def test_Termsof(self, browser):
        """查看协议"""
        page = Termsofservicepage(browser)
        page.account_bnt.click()
        page.register_bnt.click()
        page.register_num.click()
        page.terms_service.click()
        WebDriver.open_new_window(self, "link_text=《服务条款》")
        # # 获取默认页面的句柄
        # default_handle = self.driver.current_window_handle
        #
        # # 获取所有句柄
        # handles = self.driver.window_handles
        # for handle in handles:
        #     if handle != default_handle:
        #         self.driver.switch_to_window(handle)
        success = page.judge.text
        assert success == "企云会服务协议"

    if __name__ == '__main__':
        pytest.main(["-v", "-s", "test_Termsofservices.py::TestTermsofservice",  "--html", "./report.html"])