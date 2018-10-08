from.common import PageObject, PageElement

class OperationLogpage(PageObject):
    log_logo = PageElement(xpath="//span[contains(text(),'操作日志')]")
    clear_bnt = PageElement(xpath="//button[contains(text(),'清除记录')]")
    sureclear_bnt =PageElement(xpath="//div[@class='modal-footer']/button[contains(text(),'清除')]")
    cancel_bnt = PageElement(xpath="//div[@class='modal-footer']/button[contains(text(),'取消')]")
    page_box = PageElement(xpath="//div[span[contains(text(),'显示条数')]]/div/button")