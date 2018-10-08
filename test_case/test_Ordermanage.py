
import pytest
from page.Ordermanagement_page import Orderman
from test_case import test_ALogin
from test_case import test_Console
from datetime import datetime
class TestOrderman:

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
        page.get("http://test.yunmeetings.com")
        test_ALogin.Testlogin.test_login(self, "18210785199", "zl123456", browser)
        test_Console.TestConsolelogin.test_conlogin(self, browser, "zl123456")
        # 正式测试代码
        page.order_logo.click()
        print("点击订单管理")
        page.wait(1)
        titles = page.closewindow_title.text
        print("打印标题"+titles)
        print("打印完毕")
        free_use = page.upgrade_but.text
        if titles == "未完成订单提醒":
            page.closewindow_bnt.click()
            print("点击“×”")
            page.close_order.click()
            print("点击取消")
            page.sure_closeorder.click()
            print("点击确定")
            page.wait(2)
        # elif free_use == "升级专业版":
        #     page.upgrade_but.click()
        # else:
        #     page.wait(5)
        #     page.increase_bnt.click()
        # # 切换到新开页面
        # page.switch_Windows()
        # # 点击人员“+”
        # page.person_add.click()
        # # 输入人员数量
        # # page.person_input.clear()
        # # page.person_input.send_keys(num[0])
        # # 点击会议室数“+”
        # page.room_add.click()
        # # 点击存储空间“+”
        # page.storage_add.click()
        # # 滚动条到底部
        # page.scroll_foot()
        # # 点击提交订单按钮
        # page.submit_bnt.click()
        # # 点击立即支付
        # page.pay_bnt.click()
        # #跳转到支付页面
        # page.wait(2)
        # page.enter_window(2)
        # title = page.get_title()
        # # print(title)
        # # assert title == "支付宝 - 网上支付 安全快速！"
        # # 关闭当前窗口
        # page.close_window()
        # page.enter_window(1)
        # # 提示框支付成功按钮
        # page.paysuccess_bnt.click()
        # 提示框重新支付按钮
        # page.repayment_bnt.click()
        # # 选择微信
        # page.WeChat_bnt.click()
        # # 点击立即支付
        # page.pay_bnt.click()
        # # 断言
        # wcj = page.WeChat_judge.text
        # assert wcj == "微信支付"
        # page.wait(5)
        # page.enter_window(1)
        # page.wait(2)
        # # 提示框支付成功按钮
        # page.paysuccess_bnt.click()
        # # 提示框重新支付按钮
        # page.repayment_bnt.click()
        # # 银行汇款
        # page.Bank_bnt.click()
        # # 点击立即支付
        # page.pay_bnt.click()
        # page.wait(2)
        page.wait(15)

    if __name__ == '__main__':
        pytest.main(["-v", "-s","test_Ordermanage.py::TestOrderman", "--html", "../report_test/report.html"])





