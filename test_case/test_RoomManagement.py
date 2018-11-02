#-*- coding: UTF-8 -*-
import pytest,os
from page.RoomManagement_page import meetingromm
from page.Ordermanagement_page import Orderman
from test_case import test_ALogin
from test_case import test_Console

class Testroommanager:
    """
    控制台-会议室管理
    """

    # 添加会议室参数化
    @pytest.mark.parametrize(
        "room_name, room_capacity",
        [("测试会议室", "10")],
        )

    def test_addroom(self, browser, room_name, room_capacity):
        """
        添加会议室
        :param browser:
        :param room_name: 会议室名称
        :param room_capacity: 会议室容量
        :return: 无
        """
        pages = Orderman(browser)
        global page
        page = meetingromm(browser)
        # 模块测试代码(正式验证需注释)
        page.get("http://pre.yunmeetings.com")
        test_ALogin.Testlogin.test_login(self, "18210785192", "zl123456", browser)
        test_Console.TestConsolelogin.test_conlogin(self, browser, "zl123456")
        # 正式代码
        pages.order_logo.click()
        print("点击订单管理")
        page.wait(1)
        order_room_num = pages.total_room.text[0]
        page.roommanager_logo.click()
        print("点击会议室管理 ")
        room_num = page.total_room.text
        # 判断会议室是否已用完
        if order_room_num == room_num:
            # 调用删除会议室方法
            self.test_deleteroom()
        else:
            page.add_room.click()
            print("点击添加会议室按钮")
            page.wait(2)
            page.room_name.send_keys(room_name)
            print("输入会议室名称")
            page.room_capacity.send_keys(room_capacity)
            print("输入会议室容量")
            page.room_picture.click()
            page.wait(3)
            os.system("upload\personalphoto.exe")
            print("上传会议室图片")
            page.wait(5)
            page.room_save.click()
            print("点击保存")
            page.wait(2)
            page.cancel_bnt.click()
            print("点击取消按钮关闭弹窗")
            page.wait(2)

    # 修改会议室参数化
    @pytest.mark.parametrize(
        "modify_name, modify_capacity",
        [("修改会议室", "20")],
        )

    def test_modifyroom(self, modify_name, modify_capacity):
        """
        修改会议室
        :return:
        """
        page.wait(2)
        page.modify_bnt.click()
        print("点击修改")
        page.room_name.clear()
        print("清空会议名称")
        page.room_name.send_keys(modify_name)
        print("填写修改的会议室名称")
        page.room_capacity.clear()
        print("清空会议室容量")
        page.room_capacity.send_keys(modify_capacity)
        print("填写修改的会议室容量")
        page.room_save.click()
        print("点击保存")
        page.wait(2)
        assert page.assert_modify.text == "修改会议室"
        print("修改成功")
        page.wait(2)


    def test_deleteroom(self):
        """
        删除会议室
        :return:
        """
        page.all_area.click()
        print("选择全部区域")
        page.wait(1)
        page.delete_room.click()
        print("点击删除")
        page.wait(1)
        page.sure_delete.click()
        print("确认删除")
        page.wait(2)


    def test_spotroom(self):
        """
        停用会议室
        :return:
        """
        page.stop_room.click()
        print("点击停用按钮")
        page.wait(2)
        page.sure_stop.click()
        print("确定停用")
        page.wait(2)
        assert page.assert_stop.text == "启用"

    def test_openroom(self):
        """
        启用会议室
        :return:
        """
        # 列表中全部第三个操作按
        bnt_name = page.open_room
        # 判断列表数据条数
        bnt_num = len(bnt_name)
        # 循环遍历列表
        for i in range(bnt_num):
            # bnt_name = page.open_room
            if bnt_name[i].text == "启用":
                page.open_bnt.click()
                print("点击启用按钮")
                page.wait(2)
                page.sure_open.click()
                print("确认启用")
                page.wait(2)
                assert page.open_bnt.text == "停用"
                print("启用成功!")
            else:
                print("无停用会议室")
                # break





    if __name__ == '__main__':
        pytest.main(["-v", "-s","test_RoomManagement.py::Testroommanager", "--html", "../report_test/report.html"])
