import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class LoginPage(BasePage):
    log = cl.customLogger ( logging.DEBUG )

    def __init__(self,driver):
        super().__init__(driver)
        self.driver =driver

    # locators
    _login_link = "//a[@href='/login']"
    _email_field = "email"
    _password_field = "login-password"
    _login_button = "login"

    # def getLoginLink(self):
    #     return self.driver.find_element(By.XPATH,self._login_link)
    #
    # def getEmailField(self):
    #     return self.driver.find_element(By.ID,self._email_field)
    #
    # def getPasswordField(self):
    #     return self.driver.find_element(By.ID,self._password_field)
    #
    # def getButtonField(self):
    #     return self.driver.find_element(By.ID,self._login_button)


    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="xpath")

    def enterEmail(self,email):
        self.sendKeys(email,self._email_field)

    def enterPassword(self,password):
        self.sendKeys(password,self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="id")

    def login(self,email="",password=""):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()


    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//*[@class='zen-c-account']",locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//*[@'incorrectdetails']",locatorType="id")
        return result

    def verifyTitle(self):
        if "Login" in self.getTitle():
            return True
        else:
            return False



        # loginLink = self.driver.find_element(By.XPATH, "//a[@href='/login']" )
        # loginLink.click()
        #
        # emailField = self.driver.find_element(By.ID, "email")
        # emailField.send_keys(username)
        #
        # passwordField = self.driver.find_element(By.ID, "login-password")
        # passwordField.send_keys(password)
        #
        # loginButton = self.driver.find_element(By.ID, "login")
        # loginButton.click()