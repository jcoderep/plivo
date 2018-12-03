# ==============================================================================================
# Plivo Assignment
# Author ::     Jitender Singh Rana
# mail id ::    jeet841991@gmail.com
# Date ::       03-Dec-2018
# ===============================================================================================

"""
Class containing methods for Login Page

    click_create_an_app   :   Method to click on create app button

    enter_username        :   Method to enter Username

    enter_password        :   Method to enter password

    click_login_button    :   Method to click on login button
"""

import time

class LoginPage(object):
    '''
    This class contains all methods for login page
    '''
    def __init__(self, driver, log):
        """Initializing method for LoginPage class"""
        if not driver:
            raise Exception('driver not provided')
        self.driver = driver
        self.log = log

    def click_create_an_app(self):
        """Method to click on create an app option"""
        self.log.info('clicking on create app button')
        button = self.driver.find_element_by_xpath("//a[contains(text(),'Create an App')]")
        button.click()
        time.sleep(5)

    def enter_username(self):
        """Method to enter username"""

    def enter_password(self):
        """Method to enter password"""

    def click_login_button(self):
        """Method to click on login button"""
