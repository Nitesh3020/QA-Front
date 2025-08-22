import time
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class MoviePage(BasePage):
    log =  cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ## Locators ## 
    _main_search_ = "//span[text()='Search for Movies, Events, Plays, Sports and Activities']" 
    _searchbox_ = "//input[@placeholder='Search for Movies, Events, Plays & more']"
    _book_tickets_ = "(//button[.//span[text()='Book tickets']])[1]"


    ## ELement Interactions ##

    def SearchBox(self):
        self.elementClick(locator=self._main_search_,locatorType="xpath")
    
    def MovieTickets(self,Movie_Name):
        self.sendKeys(Movie_Name, locator=self._searchbox_,locatorType="xpath")
    
    def Moviebox(self):
        self.elementClick(locator=self._searchbox_,locatorType="xpath")
        
    def BookTickets(self):
        self.elementClick(locator=self._book_tickets_,locatorType="xpath")
