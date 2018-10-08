#-*- coding: UTF-8 -*-
import pytest
from page.BookMeetings_page import Meetings
from test_case import test_ALogin
from selenium.webdriver.common.action_chains import ActionChains

class TestBookmeeting:
    @pytest.mark.parametrize(
        "title",
        [("测试会议")],
        ids=["case5"]
        )
    def test_bookmeeting(self, browser, title):
        """会议预订"""
        page = Meetings(browser)
        test_ALogin.Testlogin.test_login(self, "18210785192", "zl123456", browser)
        page.mymeeting_logo.click()
        page.nextmonth_bnt.click()
        start = page.meetingtime_1
        end = page.meetingtime_2
        ActionChains(browser).drag_and_drop(start, end).perform()
        page.createmeeting_bnt.click()
        page.meetingtitle_frame.send_keys(title)
        meetingarea = page.choosemeeting_area.text
        if meetingarea == "请选择地点":
            page.meeting_area.click()
            aa = page.meeting_room
            print(aa)
            # for i in aa:
            #     print(i)
        else:
            print("已选择会议地点")

        # self.browser.find_element_by_name("contents").send_keys(self.config.getOther("info", "meetingtitle"))
        # self.logger.info("填写会议内容")
        # self.browser.find_element_by_xpath(self.config.getXPath("meetingremindbox")).click()
        # self.logger.info("选择提醒时间")
        # self.browser.find_element_by_xpath(self.config.getXPath("meetingsubmintbnt")).click()
        # self.logger.info("点击立即预订")

        page.wait(2)

    if __name__ == '__main__':
        pytest.main(["-v", "-s", "test_Bookmeetings.py::TestBookmeeting::test_bookmeeting",  "--html", "./report.html"])
