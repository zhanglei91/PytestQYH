from.common import PageObject, PageElement

"""个人资料页面元素"""
class PersonaldataPage(PageObject):
    username_bnt = PageElement(xpath="//span[@class='userName']")
    personal_info = PageElement(xpath="//a[contains(text(), '个人资料')]")
    chanage_photo = PageElement(xpath="//div[contains(text(), '更换头像')]")
    save_bnt = PageElement(xpath="//button[contains(text(), '保存')]")
    delete_photo = PageElement(xpath="//a[contains(text(), '删除头像')]")
    save_button = PageElement(xpath="//form[@id ='nameform']/div[3]/div/button")
    photos = PageElement(xpath="//div[div/div[contains(text(), '头像')]]/div/div[2]/span")
    username_box = PageElement(name="username")
    email_box = PageElement(name="email")
    personal_close = PageElement(xpath="//div[@id='profile']/a")

