from.common import PageObject, PageElement

"""控制台页面元素"""
class Consolepage(PageObject):
    console_table = PageElement(xpath="//li[@id='ConsoleLoginPageId']/a")
    console_password = PageElement(xpath="//input[@name='password']")
    console_login_btn = PageElement(xpath="//button[contains(text(),'登录')]")
    console_close_btn = PageElement(xpath="//a[@class='btn-close']")
    console_assert = PageElement(xpath="//p[contains(text(),'欢迎使用企云会控制台')]")