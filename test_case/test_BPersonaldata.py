import sys,os
import pytest
# from os.path import dirname, abspath
# sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.Personaldata_page import PersonaldataPage

class Testpersonaldata:
    """
    个人资料
    """

    @pytest.mark.parametrize(
        "username, email",
        [("zhanglie", "1234562@qq.com")],
         ids=["case2"]
    )
    def test_perdata(self, browser, username, email):
        """
        修改
        :param browser:
        :param username: 姓名
        :param email: 邮箱
        :return:
        """
        page = PersonaldataPage(browser)
        page.username_bnt.click()
        print("点击用户名")
        page.personal_info.click()
        print("点击个人资料")
        # 截取倒数第二位以后的字符
        str1 = page.username_bnt.text[-2:]
        print("截取到的文字==="+str1)
        photos = page.photos.text
        print("头像文字==="+photos)
        if photos == str1:
            page.chanage_photo.click()
            print("点击更换头像")
            page.wait(3)
            os.system("upload\personalphoto.exe")
            print("上传头像")
            page.wait(3)
            page.save_bnt.click()
            print("点击保存")
            page.wait(2)
        else:
            page.delete_photo.click()
            print("点击删除")
            page.wait(5)
        page.username_box.click()
        print("光标定位姓名框")
        page.username_box.clear()
        print("清空姓名框")
        page.username_box.send_keys(username)
        print("输入修改的姓名")
        page.email_box.click()
        print("光标定位邮件框")
        page.email_box.clear()
        print("清空邮件框")
        page.email_box.send_keys(email)
        print("输入修改的邮件")
        page.save_button.click()
        print("点击保存")
        page.wait(2)
        page.personal_close.click()
        print("关闭个人资料浮层")

    if __name__ == '__main__':
        pytest.main(["-v", "-s", "test_BPersonaldata.py::Testpersonaldata", " ../report_test/report.html"])





