
from.common import PageElement, PageObject

"""订单管理页面元素"""
class Orderman(PageObject):
    # 订单管理按钮
    order_logo = PageElement(xpath="//span[contains(text(),'订单管理')]")
    # 会议室总数量
    total_room = PageElement(xpath="//a[@class='roomTotal']")
    # 免费用户升级专业版
    upgrade_but = PageElement(xpath="//button[contains(text(),'升级专业版')]")
    # 付费用户增容
    increase_bnt = PageElement(xpath="//button[contains(text(),'增容')]")
    # 付费用户续费
    renew_bnt = PageElement(xpath="//button[contains(text(),'续费')]")
    # 人员“+”
    person_add = PageElement(xpath="//div[@class='sliderange bwer']/div[2]/div[2]/span[2]")
    # 人员“-” //div[@class='sliderange bwer']/div[2]/div[2]/span

    # 人员输入
    person_input = PageElement(xpath="//div[@class='sliderange bwer']/div[2]/div[2]/input")

    # 会议室“+”
    room_add = PageElement(xpath="//div[label[contains(text(),'会议室数')]]/div[@class='col boardroom-range']/div/div[2]/div[2]/span[2]")
    # 会议室“-”

    # 会议室输入
    room_input = PageElement(xpath="//div[label[contains(text(),'会议室数')]]/div[@class='col boardroom-range']/div/div[2]/div[2]/input")

    # 存储空间“+”
    storage_add = PageElement(xpath="//div[label[contains(text(),'存储空间')]]/div[@class='col storage-range']/div/div[2]/div[2]/span[2]")
    # 存储空间“-”

    # 存储空间输入
    storage_input = PageElement(xpath="//div[label[contains(text(),'存储空间')]]/div[@class='col storage-range']/div/div[2]/div[2]/input")

    # 提交订单
    submit_bnt = PageElement(xpath="//button[contains(text(),'提交订单')]")
    # 支付宝
    Alipay_bnt = PageElement(xpath="//a[@name='2']")
    # 微信
    WeChat_bnt = PageElement(xpath="//a[@name='1']")
    # 微信断言
    WeChat_judge = PageElement(xpath="//div[contains(text(),'微信支付')]")
    # 银行汇款
    Bank_bnt = PageElement(xpath="//a[@name='4']")
    # 立即支付
    pay_bnt = PageElement(xpath="//a[contains(text(),'立即支付')]")
    #支付成功按钮
    paysuccess_bnt = PageElement(xpath="//div[@class='modal-footer']/button")
    # 重新支付
    repayment_bnt = PageElement(xpath="//p[@class='payment-error-btn']/a")
    # 未完成订单提示框
    closewindow_title = PageElement(xpath="//form[@id='orderReminderForm']/div/div")
    # 未完成订单提示框“×”
    closewindow_bnt = PageElement(xpath="//form[@id='orderReminderForm']/div/button")
    # 取消订单
    close_order = PageElement(xpath="//span[contains(text(),'取消')]")
    # 取消订单-确定
    sure_closeorder = PageElement(xpath="//form[@id='cancelOrderForm']/div[3]/button[2]")