'''
Created on Nov 27, 2015

@author: vinh.cong.tran
'''
from selenium import webdriver
from Interfaces.LoginPage import LoginPage

class Login(LoginPage):
     
    def __init__(self):
        LoginPage.__init__(self)
     
    def openBrowser(self):
        webDriver = webdriver.Firefox()
        return webDriver
     
    def navigateToURL(self, webDriver, url):
        webDriver.get(url)
     
    def enterUsername(self, webDriver, username):
        userElement = webDriver.find_element_by_xpath(self.txtUserName)
        userElement.clear()
        userElement.send_keys(username)
     
    def enterPassword(self, webDriver, password):
        passElement = webDriver.find_element_by_xpath(self.txtPassword)
        passElement.clear()
        passElement.send_keys(password)
     
    def clickLoginButton(self, webDriver):
        loginElement = webDriver.find_element_by_xpath(self.btnLogin)
        loginElement.click()
     
    def login(self, webDriver, username, password):
        self.enterUsername(webDriver, username)
        self.enterPassword(webDriver, password)
        self.clickLoginButton(webDriver)