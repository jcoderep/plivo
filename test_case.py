# ==============================================================================================
# Plivo Assignment
# Author ::     Jitender Singh Rana
# mail id ::    jeet841991@gmail.com
# Date ::       03-Dec-2018
# ===============================================================================================

"""Test case to perform and validate following opertions
    1. Navigate to "http://quickfuseapps.com/ -> Create Page -> Component grid
    2. Add new page and add components to it,
        - Send an SMS (from Messaging module)
        - Send an Email (from Messaging module)
        - Hang up or Exit (from Basic module)
    3. Make appropriate connections for the components
    4. Enter the value for Send an SMS and Send an Email components
"""

import logging

from selenium import webdriver

from login_page import LoginPage
from grid_page import GridPage


class TestClass():
    """Test Class for quickfuseapps website testing"""

    def __init__(self):
        """Initializing method for class myClass"""
        self.driver = webdriver.Chrome()

        logging.basicConfig(filename='plivo.log', level=logging.INFO)
        self.log = logging.getLogger(__name__)
        self.log.info("\n==========================================\n")

        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("http://quickfuseapps.com/")
        self.loginobj = LoginPage(self.driver, self.log)
        self.gridobj = GridPage(self.driver, self.log)

    def run(self):
        """main method"""
        try:

            self.loginobj.click_create_an_app()

            self.gridobj.click_lets_get_started()
            self.gridobj.add_new_page()
            self.gridobj.expand_module("Messaging")

            self.gridobj.get_component_in_active_tab('Send an SMS', '550', '100')
            self.gridobj.set_incoming_and_outgoing_path("module-1", "module-2")
            self.gridobj.fill_form("//textarea[@name='phone_constant']", "9156435462")
            self.gridobj.fill_form("//textarea[@name='message_phrase[]']", "Hello")

            self.gridobj.get_component_in_active_tab("Send an Email", '850', '100')
            self.gridobj.set_incoming_and_outgoing_path("module-2", "module-3", "not_sent")
            self.gridobj.fill_form("//input[@name='smtp_url']", "abc.def.com")
            self.gridobj.fill_form("//input[@name='port']", "123.456,789.123")
            self.gridobj.fill_form("//input[@name='username']", "Tester")
            self.gridobj.fill_form("//input[@name='password']", "test!!123")
            self.gridobj.fill_form("//textarea[@name='from_constant']", "User_1")
            self.gridobj.fill_form("//textarea[@name='to_constant']", "User_2")
            self.gridobj.fill_form("//textarea[@name='subject_constant']", "TestMessage")
            self.gridobj.fill_form("//textarea[@name='cc_constant']", "User_3")
            self.gridobj.fill_form("//div[contains(@class,'module-title') and contains(text(),"\
                                          "'Send an Email')]/../../../..//textarea[@name="\
                                          "'message_phrase[]']", "Hello Everyone")

            self.gridobj.expand_module("Basic")
            self.gridobj.get_component_in_active_tab("Hang Up or Exit", '300', '100')
            self.gridobj.set_incoming_and_outgoing_path("module-2", "module-4", "sent")

            self.gridobj.get_component_in_active_tab("Hang Up or Exit", '600', '400')
            self.gridobj.set_incoming_and_outgoing_path("module-3", "module-5", "sent")

            self.gridobj.get_component_in_active_tab("Hang Up or Exit", '1150', '350')
            self.gridobj.set_incoming_and_outgoing_path("module-3", "module-6", "not_sent")

        except Exception as exp:
            self.log.info(exp)
            raise exp
        finally:
            self.driver.close()


def main():
    "main method"
    test_obj = TestClass()
    test_obj.run()

if __name__ == "__main__":
    main()
