
from.common import PageObject, PageElement

"""登录页面元素"""
class LoginPage(PageObject):
    account_bnt = PageElement(name="account")
    name_input = PageElement(id_="phoneNumber")
    password_input = PageElement(id_="inputPassword")
    submit_bnt = PageElement(id_="submitBtn")
    one_page = PageElement(xpath="//a[contains(text(),'会议预订')]")



