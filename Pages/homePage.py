from Locators.locators import Locators

class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.my_info_module = Locators.my_info_module_xpath

    def click_my_info(self):
        self.driver.find_element_by_xpath(self.my_info_module)



