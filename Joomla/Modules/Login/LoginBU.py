'''
Created on Nov 27, 2015

@author: vinh.cong.tran
'''
from Actions.Login import Login
from Actions.ControlPanel import ControlPanel

class LoginBU(Login, ControlPanel):
    
    def __init__(self):
        Login.__init__(self)
        ControlPanel.__init__(self)
    
    def TC_01(self):
        # Step 1 - Open Browser
        webDriver = self.openBrowser()
        
        # Step 2 - Navigate to Joomla Administrator page
        self.navigateToURL(webDriver, "http://localhost/joomla/administrator")
        
        # Step 3 - Enter username
        self.enterUsername(webDriver, "admin")
        
        # Step 4 - Enter password
        self.enterPassword(webDriver, "admin")
        
        # Step 5 - Click Login button
        self.clickLoginButton(webDriver)
        
        # VP - The Administrator Control Panel page is displayed
        self.checkControlPanelPageIsDisplayed(webDriver)
        
        # CLOSE BROWSER
        self.closeBrowser(webDriver)
        
if __name__ == '__main__':
    loginClass = LoginBU()
    loginClass.TC_01()