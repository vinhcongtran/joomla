'''
Created on Nov 27, 2015

@author: vinh.cong.tran
'''
class LoginPage():
    
    def __init__(self):
        self.txtUserName = ".//*[@id='mod-login-username']"
        self.txtPassword = "//*[@id='mod-login-password']"
        self.btnLogin = "//a[contains(text(),'Log in')]"