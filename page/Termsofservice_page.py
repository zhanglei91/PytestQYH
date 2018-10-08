from.common import PageObject, PageElement
from page import Login_page

"""查看协议"""

class Termsofservicepage(PageObject):
    # login_element = Login_page.LoginPage
    # button = login_element.account_bnt
    # account_button = PageElement(name=button)
    # account_button = PageElement(name="account")
    account_bnt = PageElement(name="account")
    register_bnt = PageElement(xpath="//a[contains(text(),'注册新账号')]")
    register_num = PageElement(xpath="//a[contains(text(),'没有微信号？手机号注册')]")
    terms_service = PageElement(xpath="//a[contains(text(),'《服务条款》')]")
    judge = PageElement(xpath="//h1[contains(text(),'企云会服务协议')]")
    return_login = PageElement(xpath="")
