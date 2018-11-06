
import pytest
from page.Ordermanagement_page import Orderman
from test_case import test_ALogin
from test_case import test_Console
from datetime import datetime
class TestOrderman:
    """
    订单管理
    """

    # 参数化
    @pytest.mark.parametrize(
        "num",
        [("60", "10", "10")],
        ids=["case"]
        )

    def test_personadd(self, browser, num):
        """订单管理"""
        page = Orderman(browser)
        # 模块测试代码(正式验证需注释)
        page.get("http://pre.yunmeetings.com")
        test_ALogin.Testlogin.test_login(self, "18210785192", "zl123456", browser)
        test_Console.TestConsolelogin.test_conlogin(self, browser, "zl123456")
        # 正式测试代码
        page.order_logo.click()
        print("点击订单管理")
        page.wait(1)
        titles = page.closewindow_title.text
        free_use = page.upgrade_but.text
        if titles == "未完成订单提醒":
            page.wait(1)
            page.closewindow_bnt.click()
            print("点击“×”")
            page.wait(1)
            page.close_order.click()
            print("点击取消")
            page.wait(1)
            page.sure_closeorder.click()
            print("点击确定")
            page.wait(2)
            page.increase_bnt.click()
            print("点击增容按钮")
            page.wait(2)
        elif free_use == "升级专业版":
            page.wait(1)
            page.upgrade_but.click()
        else:
            page.wait(2)
            print("已是付费用户")
            page.increase_bnt.click()
            print("点击增容按钮")
            page.wait(2)
        page.switch_Windows()
        print("切换到升级或增容页面")
        page.person_add.click()
        print("增加人员==+")
        # 输入人员数量
        # page.person_input.clear()
        # page.person_input.send_keys(num[0])
        page.room_add.click()
        print("增加会议室数量==+")
        page.storage_add.click()
        print("增加存储空间==+")
        # 滚动条到底部
        page.scroll_foot()
        page.submit_bnt.click()
        print("点击提交订单按钮")
        page.pay_bnt.click()
        print("点击立即支付")
        #跳转到支付页面
        page.wait(2)
        page.enter_window(2)
        title = page.get_title()
        browser_title = title[0:3]
        print(browser_title)
        assert browser_title == "支付宝"
        # 关闭当前窗口
        # page.close_window()
        page.enter_window(1)
        page.paysuccess_bnt.click()
        print("点击提示框支付成功按钮")
        page.repayment_bnt.click()
        print("点击提示框重新支付按钮")
        page.WeChat_bnt.click()
        print("选择微信")
        page.pay_bnt.click()
        print("点击立即支付")
        page.wait(2)
        # 断言
        # wcj = page.WeChat_judge.text
        # print(wcj)
        # assert wcj == "微信支付"
        # page.wait(5)
        page.enter_window(1)
        page.wait(2)
        page.paysuccess_bnt.click()
        print("点击提示框支付成功按钮")
        page.repayment_bnt.click()
        print("点击提示框重新支付按钮")
        page.Bank_bnt.click()
        print("选择银行汇款")
        page.pay_bnt.click()
        print("点击立即支付")
        page.wait(2)

    if __name__ == '__main__':
        pytest.main(["-v", "-s","test_Ordermanage.py::TestOrderman", "--html", "../report_test/report.html"])





