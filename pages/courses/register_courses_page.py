import time
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from pages.home.login_page import LoginPage

class RegisterCoursesPage(BasePage):
    log = cl.customLogger(logging.DEBUG)
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.login_page = LoginPage(driver)  
        
    ## Locators ##     
    _all_courses_link = "//a[@href='/courses']"
    _search_box = "//input[@id='search']"
    _search_course_icon = "//button[@class='find-course search-course']"
    _course = "//div[@id='course-list']"
    _all_courses = "course-list"
    _enroll_button = "//button[contains(@class, 'dynamic-button') and contains(@class, 'btn-enroll') and text()='Enroll in Course']"
    _cc_num = "//input[@aria-label='Credit or debit card number']"
    _cc_exp = "//iframe[@title='Secure expiration date input frame']"
    _cc_cvv = "//iframe[@title='Secure CVC input frame']"
    _submit_enroll = "//button[contains(., 'Buy')]"  
    _enroll_error_message = "//span[text()='Your card number is invalid.']" 

    ### Element Interactions ###

    def performLogin(self):
        self.login_page.login("charile30@gmail.com", "Qwerty@123")

    def clickMainCourse(self):
        print("I reached here")
        self.driver.execute_script("arguments[0].click();", self.getElement("//a[@href='/courses']", locatorType="xpath"))
        
    def enterCourseName(self, course_name):
        # Enter course name in the search box
        self.sendKeys(course_name, locator=self._search_box, locatorType="xpath")
        # Click the search button
        self.elementClick(locator=self._search_course_icon, locatorType="xpath")
        # Locate the course from the results
        course_xpath = f"//h4[contains(text(), '{course_name}')]/ancestor::a"
        self.elementClick(locator=course_xpath, locatorType="xpath")

        
    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(locator=self._course.format(fullCourseName), locatorType="xpath")

    def clickOnEnrollButton(self):
        self.elementClick(locator=self._enroll_button, locatorType="xpath")

    def enterCardNum(self, num):
        iframe = self.getElement("//iframe[contains(@name, 'privateStripeFrame')]", locatorType="xpath")
        self.driver.switch_to.frame(iframe)
        self.sendKeys(num, locator=self._cc_num, locatorType="xpath")
        self.driver.switch_to.default_content()
    
    def enterCardExp(self, exp):
        iframe = self.getElement("//iframe[@title='Secure expiration date input frame']", locatorType="xpath")
        self.driver.switch_to.frame(iframe)
        self.waitForElement("//input[@name='exp-date']", locatorType="xpath", timeout=10)
        self.sendKeys(exp, locator="//input[@name='exp-date']", locatorType="xpath")
        self.driver.switch_to.default_content()

    def enterCardCVV(self, cvv):
        iframe = self.getElement("//iframe[@title='Secure CVC input frame']", locatorType="xpath")
        self.driver.switch_to.frame(iframe)
        self.waitForElement("//input[@name='cvc']", locatorType="xpath", timeout=10)
        self.sendKeys(cvv, locator="//input[@name='cvc']", locatorType="xpath")
        self.driver.switch_to.default_content()
    
    def clickEnrollSubmitButton(self):
        # Wait for the element to be clickable (XPath locator type)
        self.waitForElement(self._submit_enroll, locatorType="xpath", timeout=10)
        # Click the submit button
        self.elementClick(locator=self._submit_enroll, locatorType="xpath")

    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)

    def enrollCourse(self, num="", exp="", cvv=""):
        self.clickOnEnrollButton()
        self.webScroll(direction="down")
        self.enterCreditCardInformation(num, exp, cvv)
        self.clickEnrollSubmitButton()

    def verifyEnrollFailed(self):
        messageElement = self.waitForElement(self._enroll_error_message, locatorType="xpath")
        result = self.isElementDisplayed(element=messageElement)
        return result