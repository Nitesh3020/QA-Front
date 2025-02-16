from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("charile30@gmail.com","Qwerty@123")
        result1 = self.lp.verifyTitle()
        self.ts.mark(result1,"Title is incorrect")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_vaildLogin", result2,"Login was not Successful")
        
    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("charile@gmail.com","Qwerty@1234")
        result = self.lp.verifyLoginFailed()
        assert result == False