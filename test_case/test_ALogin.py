import sys
import pytest
# from os.path import dirname, abspath
# sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.Login_page import LoginPage
from page.Personaldata_page import PersonaldataPage


class Testlogin:
    """
    登录
    """

    @pytest.mark.parametrize(
        "name, password",
        [("18210785192", "zl123456")],
        ids=["case1"]
    )

    def test_login(self, name, password, browser):
        """
        登录-正向
        :param name: 用户名
        :param password: 密码
        :param browser:
        :return:
        """
        global page
        page = LoginPage(browser)
        page.get("http://pre.yunmeetings.com")
        page.account_bnt.click()
        print("点击账号登录")
        page.name_input.send_keys(name)
        print("输入用户名")
        page.password_input.send_keys(password)
        print("输入密码")
        page.submit_bnt.click()
        print("点击登录")
        home_page = page.one_page.text
        page.wait(2)
        assert home_page == "会议预订"


    def test_loginout(self, browser):
        """
        退出
        :return:
        """
        pages = PersonaldataPage(browser)
        # 复用个人资料中定位到的“用户名”元素
        pages.username_bnt.click()
        print("点击用户名")
        page.loginout_bnt.click()
        page.wait(2)
        print("点击退出登录")


    if __name__ == '__main__':
        pytest.main(["-v", "-s", "test_ALogin.py::Testlogin"])

