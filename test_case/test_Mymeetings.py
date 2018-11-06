#-*- coding: UTF-8 -*-
import pytest
from page.MyMeetings_page import Meetings
from test_case import test_ALogin
from selenium.webdriver.common.action_chains import ActionChains

class TestBookmeeting:
    """
    我的会议-会议预订
    """

    @pytest.mark.parametrize(
       "meeting_name",
        [("测试会议")],
        ids=["case"]
        )

    def test_bookmeeting(self, browser, meeting_name):
        """
        预订会议
        :param browser:
        :param meeting_name: 会议名称
        :return:
        """
        global page
        page = Meetings(browser)
        # 模块测试代码(正式验证需注释)
        page.get("http://pre.yunmeetings.com")
        test_ALogin.Testlogin.test_login(self, "18210785192", "zl123456", browser)
        # 正式代码块
        page.mymeeting_logo.click()
        print("点击我的会议")
        page.nextmonth_bnt.click()
        print("点击切换下一个月")
        start = page.meetingtime_1
        end = page.meetingtime_2
        ActionChains(browser).drag_and_drop(start, end).perform()
        print("选择开始和结束时间")
        page.createmeeting_bnt.click()
        print("点击新建会议")
        page.meetingtitle_frame.send_keys(meeting_name)
        print("填写会议名称")
        page.wait(2)
        meeting_area = page.choosemeeting_area.text
        if meeting_area == "请选择地点":
            page.meeting_area.click()
            print("点击会议地点")
            page.wait(2)
            # 会议室名称位置
            room_name = page.meetingroom_name
            # 会议室列表长度
            room_num = len(room_name)
            # 循环遍历会议室列表
            for i in range(room_num):
                # 循环获取会议列表中全部有占用标识会议室
                occupy_list = page.room_occupy
                # 获取标识文本
                list_text = occupy_list[i].text
                if list_text == "占用":
                    print("有占用")
                    # metting_room_name =room_name[i+1].click()
                    # print(metting_room_name.text)
                else:
                    room_name[0].click()
                    break
                # 会议室名称文本
                # metting_room_name = room_name[i].text
                # 获取全部会议室名称
                # metting_room_name_data = metting_room_name
        else:
            print("已选择会议地点")
        page.book_bnt.click()
        print("点击立即预订按钮")
        page.wait(2)
        global get_meeting_name
        get_meeting_name = page.get_meeting_name.text
        print(get_meeting_name)
        assert page.book_assert.text[0:4] == "会议详情"
        page.wait(2)


    @pytest.mark.parametrize(
       "modify_name",
        [("修改会议")],
        ids=["case"]
        )
    def test_modifymeeting(self, modify_name):
        """
        修改会议
        :param modify_name: 修改会议名称
        :return:
        """
        page.close_X.click()
        print("点击×")
        page.modify_metname.click()
        print("点击会议名称")
        page.modify_bnt.click()
        print("点击修改按钮")
        page.wait(1)
        page.meetingtitle_frame.clear()
        print("清空会议名称")
        page.meetingtitle_frame.send_keys(modify_name)
        print("输入新会议名称")
        page.save_modify.click()
        print("点击保存按钮")
        page.wait(2)


    def test_cancelmeeting(self):
        """
        取消会议
        :return:
        """
        # page.cancel_name = get_meeting_name
        page.close_X.click()
        print("点击×")
        page.cancel_metname.click()
        print("点击会议名称")
        page.cancel_bnt.click()
        print("点击取消按钮")
        page.wait(1)
        page.sure_bnt.click()
        print("点击确认按钮")
        page.wait(2)


    def test_deletemeeting(self):
        """
        删除会议
        :return:
        """
        page.list_bnt.click()
        print("点击列表")
        page.feature_meeting.click()
        print("点击未来会议")
        page.delete_name.click()
        print("点击被删除会议名称")
        page.wait(2)
        page.delete_bnt.click()
        print("点击删除按钮")
        page.wait(1)
        page.sure_delbnt.click()
        print("确认删除")
        page.wait(2)






if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_Mymeetings.py::TestBookmeeting",  "--html", "../report_test/report.html"])
