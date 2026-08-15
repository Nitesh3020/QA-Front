import utilities.custom_logger as cl
import logging
from base.selenium_driver import SeleniumDriver

class TestStatus(SeleniumDriver):
    log = cl.customLogger(logging.INFO)
    
    def __init__(self, driver):
        super(TestStatus,self).__init__(driver)
        self.resultList = []
        
    def setResult(self,result,resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL :: + " +resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.info("### VERIFICATION FAILED :: + " + resultMessage)
                    self.screenShot(resultMessage)
            else:
                self.resultList.append("FAIL")
                self.log.info("### VERIFICATION FAILED :: + " + resultMessage)
                self.screenShot(resultMessage)
        except:
            self.resultList.append("FAIL")
            self.log.info("### Exception Occured !!! ")
            self.screenShot(resultMessage)
            
            
    def mark(self,result,resultMessage):
        
        self.setResult(result, resultMessage)
    def markFinal(self, testName, result, resultMessage):
        
        self.setResult(result,resultMessage)
        if "FAIL" in self.resultList:
            self.log.error(testName + "### TEST FAILED")     
            self.resultList.clear()                        
            # assert True == False
            assert "FAIL" not in self.resultList

        else:
            self.log.info(testName + "##@ TEST SUCCESSFUL ")
            self.resultList.clear()
            # assert True == True
            assert "FAIL" not in self.resultList