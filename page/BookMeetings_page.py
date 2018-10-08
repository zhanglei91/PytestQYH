
from.common import PageElement, PageObject, PageElements

"""会议相关元素"""
class Meetings(PageObject):
    mymeeting_logo = PageElement(xpath="// a[contains(text(), '我的会议')]")
    # 下个月“>”按钮
    nextmonth_bnt = PageElement(xpath="//div[1]/div/div[1]/div[2]/div/div[1]/table/thead/tr[2]/th[3]/i")
    # 会议时间区域
    meetingtime_1 = PageElement(xpath="//div[@class='fc-time-grid fc-unselectable']/div[2]/table/tbody/tr[35]/td[2]")
    meetingtime_2 = PageElement(xpath="//div[@class='fc-time-grid fc-unselectable']/div[2]/table/tbody/tr[36]/td[2]")
    # 新建会议按钮
    createmeeting_bnt = PageElement(xpath="//div[contains(text(),'新建会议')]")
    # 已预订会议区域
    bookmeeting_area = PageElement(xpath="//div[@data-title='测试会议']")
    # 取消会议
    cancelmeeting_bnt = PageElement(xpath="//div[@class='handles']/button[contains(text(),'取消会议')]")
    # 取消会议-确定
    surecancel_bnt = PageElement(xpath="//button[contains(text(),'确定')]")
    # 预订页面 - 会议主题
    meetingtitle_frame = PageElement(xpath="//input[ @class ='form-control form-control-lg']")
    # 预订页面-会议地点
    choosemeeting_area = PageElement(xpath="//div[ @class ='pop place']/span[2]")
    meeting_area = PageElement(xpath="//span[contains(text(), '请选择地点')]")
    meeting_room = PageElements(xpath="span[@class='name']")