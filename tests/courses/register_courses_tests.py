from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import time

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        self.courses.performLogin()
        time.sleep(5)
        self.courses.clickMainCourse()
        self.courses.enterCourseName("JavaScript")
        time.sleep(5)
        self.courses.selectCourseToEnroll("JavaScript for beginners") 
        self.courses.clickOnEnrollButton()
        time.sleep(5)
        self.courses.enrollCourse(num="7896 8954 1220 2892", exp="12/27", cvv="756")
        time.sleep(5)
        result = self.courses.verifyEnrollFailed()  
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment Failed Verification") 