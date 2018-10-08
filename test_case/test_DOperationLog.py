
import pytest
from page.OperationLog_page import OperationLogpage
from test_case.test_Console import TestConsolelogin

class TestOperationLog:

    ids=["case4"]
    def test_operationlog(self, browser):
        """操作日志"""
        page = OperationLogpage(browser)
        # TestConsolelogin.test_conlogin(self, browser, "zl123456")
        page.log_logo.click()
        page.wait(2)

    if __name__ == '__main__':
        pytest.main(["-v", "-s", "test_DOperationLog.py::TestOperationLog", "--html", "./report.html"])

