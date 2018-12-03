# ==============================================================================================
# Plivo Assignment
# Author ::     Jitender Singh Rana
# mail id ::    jeet841991@gmail.com
# Date ::       03-Dec-2018
# ===============================================================================================

"""
Class containing methods for Grid Page

    click_lets_get_started   :   Method to click on Lets's get started button'

    fill_form                :  Method to enter value in input boxes with given xpath

    __click_new_page         :  Method to click on New page

    add_new_page             :   Method to add new page

    expand_module            :  Method to expand given module

    get_component_in_active_tab : Method to move component in active tab

    set_incoming_and_outgoing_path : Method to set connections for compoenents in grid
"""

import time
from selenium.webdriver import ActionChains


class GridPage(object):
    '''
    This class contains all methods for grid page
    '''
    def __init__(self, driver, log):
        """Initializing method for GridPage class

        Args:
            driver  :   webdriver object to be passed from test case

            log     :   logging object to be passed from test case
        """
        if not driver:
            raise Exception('driver not provided')
        self.driver = driver
        self.log = log

    def click_lets_get_started(self):
        '''
        Method to click on lets's get started button
        '''
        self.log.info('clicking on lets get started button')
        button = self.driver.find_element_by_xpath("//div[@id='intro-dialog-cont']"\
                                                   "/div[2]/button")
        button.click()

    def fill_form(self, xpth, value):
        """Method to fill values in text boxes

        Args:
            xpth    :   xpath of the textbox to be filled

            value   :   value to be filled in the textbox

        """
        self.log.info('Entering value: %s in textbox', value)
        self.driver.find_element_by_xpath(xpth).send_keys(value)

    def __click_new_page(self):
        """Method to click new page button"""
        self.log.info('Clicking on new page button')
        button = self.driver.find_element_by_id("add-page")
        button.click()

    def add_new_page(self):
        """Method to add new page"""
        self.log.info('Adding a new page')
        self.__click_new_page()
        self.fill_form("//input[@class='indented submitonenter']", "TestPage")
        self.driver.find_element_by_xpath("//input[@class='indented submitonenter']"\
                                          "/../../../../div[3]/button").click()

    def expand_module(self, module_name):
        """Method to expand a particular modules pane

            Args:
                module_name    : name of the module to be expanded

            Exceptions:
                None
        """
        self.log.info('Expanding module: %s', module_name)
        module = self.driver.find_element_by_xpath("//a[contains(.,'"+module_name+"') and "\
                                                        "@href='javascript:void(0)']")
        module.click()
        time.sleep(5)

    def get_component_in_active_tab(self,
                                    component_name,
                                    xoffset,
                                    yoffset):
        """Method to get component to active tab

            Args:
                component_name    : name of the component to be moved to grid

                xoffset           : x component of offset by which component is to be moved

                yoffset           : y component of offset by which component is to be moved

            Exceptions:
                None
        """
        self.log.info('Getting component: %s in the active tab', component_name)
        source = self.driver.find_element_by_xpath("//li[contains(.,'"+component_name+"') "\
                                                         "and @unselectable='on']")

        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop_by_offset(source, xoffset, yoffset).perform()
        time.sleep(5)

    def set_incoming_and_outgoing_path(self,
                                       source_component_id,
                                       target_component_id,
                                       node=None):
        """Method to obtain offset and move to element

            Args:
                source_component_id    :    Id of the source component

                target_component_id    :    Id of the target component

                node    :    In case of multiple output nodes, connection to sent/not-sent
        """

        self.log.info('Setting connection from %s to %s',
                      source_component_id, target_component_id)
        if node == 'sent':
            source = self.driver.find_element_by_xpath(
                "//div[@id='" + source_component_id + "']"\
                "//div[@class='panel-nodes-attached inner']/div")
        elif node == 'not_sent':
            source = self.driver.find_element_by_xpath(
                "//div[@id='" + source_component_id + "']"\
                "//div[@class='panel-nodes-attached inner']/div[2]")
        else:
            source = self.driver.find_element_by_xpath(
                "//div[@id='" + source_component_id + "']"\
                "//div[@class='mod-rail mod-south']/div")

        target = self.driver.find_element_by_xpath(
            "//div[@id='" + target_component_id + "']"\
            "//div[@class='mod-rail mod-north']/div")

        action_chains = ActionChains(self.driver)
        action_chains.click_and_hold(source).move_to_element(target).click(target).release()\
        .perform()
        time.sleep(5)
