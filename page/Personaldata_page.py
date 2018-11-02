from.common import PageObject, PageElement

"""个人资料页面元素"""
class PersonaldataPage(PageObject):
    # 用户名
    username_bnt = PageElement(xpath="//span[@class='userName']")
    # 个人资料
    personal_info = PageElement(xpath="//a[contains(text(), '个人资料')]")
    # 更换头像
    chanage_photo = PageElement(xpath="//div[contains(text(), '更换头像')]")
    # 保存
    save_bnt = PageElement(xpath="//button[contains(text(), '保存')]")
    # 删除头像
    delete_photo = PageElement(xpath="//a[contains(text(), '删除头像')]")
    # 点击保存
    save_button = PageElement(xpath="//form[@id ='nameform']/div[3]/div/button")
    # 判断头像
    photos = PageElement(xpath="//div[div/div[contains(text(), '头像')]]/div/div[2]/span")
    # 姓名框
    username_box = PageElement(name="username")
    # 邮件框
    email_box = PageElement(name="email")
    # 关闭“×”
    personal_close = PageElement(xpath="//div[@id='profile']/a")
