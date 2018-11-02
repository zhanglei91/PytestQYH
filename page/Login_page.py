
from.common import PageObject, PageElement

"""登录页面元素"""
class LoginPage(PageObject):
    """
    登录
    """
    # 账号密码登录
    account_bnt = PageElement(name="account")
    # 用户名
    name_input = PageElement(id_="phoneNumber")
    # 密码
    password_input = PageElement(id_="inputPassword")
    # 登录
    submit_bnt = PageElement(id_="submitBtn")
    # 断言
    one_page = PageElement(xpath="//a[contains(text(),'会议预订')]")

    """
    退出
    """
    # 退出登录
    loginout_bnt = PageElement(xpath="//a[contains(text(),'退出登录')]")






