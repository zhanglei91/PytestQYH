
from.common import PageElement, PageObject, PageElements

"""会议相关元素"""
class Meetings(PageObject):
    """预订会议"""
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
    # 会议室列表（全部会议室）
    meetingroom_name = PageElements(xpath="//label/div/span")
    # 占用（全部占用）
    room_occupy = PageElements(xpath="//div[@class='results']/label/span[1]")
    # 立即预订
    book_bnt = PageElement(xpath="//button[contains(text(),'立即预订')]")
    # 获取会议名称
    get_meeting_name = PageElement(xpath="//h5")
    # 断言
    book_assert = PageElement(xpath="//div[contains(text(),'会议详情')]")

    """修改会议"""
    # 修改按钮
    modify_bnt = PageElement(xpath="//button[contains(text(),'修改会议')]")
    # 被修改会议名称
    modify_metname = PageElement(xpath="//span[contains(text(),'测试会议')]")
    # 保存按钮
    save_modify = PageElement(xpath="//button[contains(text(),'保存')]")


    """取消会议"""
    # cancel_name = ""
    # 叉号
    close_X = PageElement(xpath="//body/div[last()]/a")
    # 被取消会议名称
    # cancel_metname = PageElement(xpath="//span[contains(text(),\'"+cancel_name+"\']")
    cancel_metname = PageElement(xpath="//span[contains(text(),'修改会议')]")
    # 取消会议按钮
    cancel_bnt = PageElement(xpath="//button[contains(text(),'取消会议')]")
    # 点击确定
    sure_bnt = PageElement(xpath="//button[contains(text(),'确定')]")

    """删除会议"""
    # 列表视图
    list_bnt = PageElement(id_='btn-list')
    # 未来的会议
    feature_meeting = PageElement(xpath="//a[contains(text(),'未来的会议')]")
    # 被删除会议
    delete_name = PageElement(xpath="//h6[contains(text(),'修改会议')]")
    # 删除按钮
    delete_bnt = PageElement(xpath="//button[contains(text(),'删除会议')]")
    # 确认删除
    sure_delbnt = PageElement(xpath="//button[contains(text(),'删除')]")


