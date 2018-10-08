import sys,os
import pytest
# from os.path import dirname, abspath
# sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.Personaldata_page import PersonaldataPage

class Testpersonaldata:

    @pytest.mark.parametrize(
        "username, email",
        [("zhanglie", "1234562@qq.com")],
         ids=["case2"]
    )
    def test_perdata(self, browser, username, email):
        """个人资料"""
        page = PersonaldataPage(browser)
        page.username_bnt.click()
        page.personal_info.click()
        # 截取倒数第二位以后的字符
        str1 = page.username_bnt.text[-2:]
        print(str1)
        photos = page.photos.text
        print(photos)
        if photos == str1:
            page.chanage_photo.click()
            page.wait(3)
            os.system("upload\personalphoto.exe")
            page.wait(3)
            page.save_bnt.click()
            page.wait(2)
        else:
            page.delete_photo.click()
            page.wait(5)
        page.username_box.click()
        page.username_box.clear()
        page.username_box.send_keys(username)
        page.email_box.click()
        page.email_box.clear()
        page.email_box.send_keys(email)
        page.save_button.click()
        page.wait(2)
        page.personal_close.click()

    if __name__ == '__main__':
        pytest.main(["-v", "-s", "test_BPersonaldata.py::Testpersonaldata"])





