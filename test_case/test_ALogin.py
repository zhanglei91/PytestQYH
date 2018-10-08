import sys
import pytest
# from os.path import dirname, abspath
# sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.Login_page import LoginPage


@pytest.mark.parametrize(
    "name, password",
    [("18210785192", "zl123456")],
    ids=["case2"]
)
class Testlogin:

    def test_login(self, name, password, browser):
        """登录"""
        page = LoginPage(browser)
        page.get("http://test.yunmeetings.com")
        page.account_bnt.click()
        page.name_input.send_keys(name)
        page.password_input.send_keys(password)
        page.submit_bnt.click()
        home_page = page.one_page.text
        page.wait(2)
        assert home_page == "会议预订"


    if __name__ == '__main__':
        pytest.main(["-v", "-s", "test_ALogin.py::Testlogin"])

