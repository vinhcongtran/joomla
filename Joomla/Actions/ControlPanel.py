'''
Created on Nov 27, 2015

@author: vinh.cong.tran
'''
from Interfaces.ControlPanelPage import ControlPanelPage


class ControlPanel(ControlPanelPage):
    def __init__(self):
        ControlPanelPage.__init__(self)
        
    def checkControlPanelPageIsDisplayed(self, webDriver):
        try:
            webDriver.find_element_by_xpath(self.pagUnique)
            print "PASSED - The Control Panel page is displayed"
        except Exception:
            print "FAILED - The Control Panel page isn't displayed"
    
    def closeBrowser(self, webDriver):
        webDriver.quit()