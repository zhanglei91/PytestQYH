from.common import PageObject, PageElement

"""控制台页面元素"""
class Consolepage(PageObject):
    """登录控制台"""

    # 控制台
    console_table = PageElement(xpath="//li[@id='ConsoleLoginPageId']/a")
    # 密码框
    console_password = PageElement(xpath="//input[@name='password']")
    # 登录按钮
    console_login_btn = PageElement(xpath="//button[contains(text(),'登录')]")
    # 关闭按钮
    console_close_btn = PageElement(xpath="//a[@class='btn-close']")
    # 断言
    console_assert = PageElement(xpath="//p[contains(text(),'欢迎使用企云会控制台')]")

    """退出控制台"""
    # 退出按钮
    console_out = PageElement(xpath="//a[contains(text(),'退出控制台')]")
    # 断言
    out_assert = PageElement(xpath="//a[contains(text(),'首页')]")

