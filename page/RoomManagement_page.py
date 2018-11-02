#-*- coding: UTF-8 -*-

from.common import PageElement, PageElements, PageObject

"""会议室管理页面元素"""
class meetingromm(PageObject):
    # 会议室管理菜单
    roommanager_logo = PageElement(id_="3")
    # 会议室总数
    total_room = PageElement(xpath="//a[@id='treeDemo_1_a']/label")

    """
    添加会议室
    """
    # 添加会议室按钮
    add_room = PageElement(xpath="//button[contains(text(),'添加会议室')]")
    # 会议室名称
    room_name = PageElement(name="room_name")
    # room_name = PageElement(xpath="//form[@id='roomform']/div/input")
    # 会议室容量room_capacity
    room_capacity = PageElement(name="room_capacity")
    # 会议室图片
    room_picture = PageElement(xpath="//span[@class='btn-select-photo']/label")
    # 保存按钮
    room_save = PageElement(id_="save-btn")
    # 取消按钮
    cancel_bnt = PageElement(xpath="//a[contains(text(),'取消')]")

    """
    修改会议室
    """
    # 修改按钮
    modify_bnt = PageElement(xpath="//tbody[@id='roomBody']/tr/td[4]/button")
    # 断言
    assert_modify = PageElement(xpath="//h6/span")


    """ 
    删除会议室
    """
    # 全部区域
    all_area = PageElement(id_='treeDemo_1_a')
    # 删除按钮
    delete_room = PageElement(xpath="//tbody[@id='roomBody']/tr/td[4]/button[2]")
    # 确认删除
    sure_delete = PageElement(xpath="//form[@id='deleteForm']/div[3]/button[2]")

    """
    停用会议室
    """
    # 停用按钮
    stop_room = PageElement(xpath="//tbody[@id='roomBody']/tr/td[4]/button[contains(text(),'停用')]")
    # 确认停用
    sure_stop = PageElement(xpath="//form[@id='disableForm']/div[3]/button[2]")
    # 断言
    assert_stop = PageElement(xpath="//tbody[@id='roomBody']/tr/td[4]/button[contains(text(),'启用')]")

    """
    启用会议室
    """
    # 全部第三个按钮
    open_room = PageElements(xpath="//tbody[@id='roomBody']/tr/td[4]/button[3]")
    # 启用按钮
    open_bnt = PageElement(xpath="//tbody[@id='roomBody']/tr/td[4]/button[3]")
    # 确认启用
    sure_open = PageElement(xpath="//form[@id='enabledForm']/div[3]/button[2]")