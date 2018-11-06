from.common import PageObject, PageElement
from page import Login_page

"""查看协议页面元素"""

class Termsofservicepage(PageObject):
    # 注册新账号
    register_bnt = PageElement(xpath="//a[contains(text(),'注册新账号')]")
    # 没有微信号？手机号注册
    register_num = PageElement(xpath="//a[contains(text(),'没有微信号？手机号注册')]")
    # 服务条款
    terms_service = PageElement(xpath="//a[contains(text(),'《服务条款》')]")
    # 断言
    judge = PageElement(xpath="//h1[contains(text(),'企云会服务协议')]")

    # return_login = PageElement(xpath="")
