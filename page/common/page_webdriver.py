import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class WebDriver(object):

    def wait(self, sec):
        """
        sleep
        :param sec: second
        :return:
        """
        time.sleep(sec)

    def get_title(self):
        """
        Get window title.
        Usage:
        driver.get_title()
        """
        return self.driver.title

    def get_alert_text(self):
        """
        Gets the text of the Alert.
        Usage:
        driver.get_alert_text()
        """
        return self.driver.switch_to.alert.text

    def accept_alert(self):
        """
        Accept warning box.
        Usage:
        driver.accept_alert()
        """
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        """
        Dismisses the alert available.
        Usage:
        driver.dismiss_alert()
        """
        self.driver.switch_to.alert.dismiss()

    def get_text(self):
        """
        获取文本
        """
        self.driver.text()

    def switch_Windows(self):
        # 获取默认页面的句柄
        default_handle = self.driver.current_window_handle
        # 获取所有句柄
        handles = self.driver.window_handles
        for handle in handles:
            if handle != default_handle:
                self.driver.switch_to_window(handle)


    def enter_window(self, number):
        """
        跳转到指定窗口
        :return:
        """
        allhandles = self.driver.window_handles
        for handle1 in allhandles:
            if handle1 != allhandles:
                self.driver.switch_to_window(allhandles[number])

    def close_window(self):
        """
        关闭当前窗口
        从标签页A打开新的标签页B，关闭标签页A
        :return:
        """
        self.driver.close()


    def close_nowwindow(self):
        """
        关闭新开窗口
        从标签页A打开新的标签页B，关闭标签页B
        :return:
        """
        action = ActionChains(self.driver)
        action.key_down(Keys.CONTROL).send_keys("w").key_up(Keys.CONTROL).perform()



    def scroll_top(self):
        """
        移动滚动条到顶部
        :return:
        """
        # if self.driver == "chorme":
        js = "var q=document.body.scrollTop=0"
        # else:
            # js = "var q=document.decumentElement.scorllTop=0"
        self.driver.execute_script(js)


    def scroll_foot(self):
        """
        移动滚动条到底部
        :return:
        """
        # if self.driver == "chorme":
        js = "var q=document.body.scrollTop=10000"
        # else:
            # js = "var q=document.decumentElement.scorllTop=10000"
        self.driver.execute_script(js)
