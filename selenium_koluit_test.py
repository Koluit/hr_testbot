# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)



class KoluitTest(unittest.TestCase):
    def test_koluit(self):
        driver.get("https://www.koluit.com")
        main = driver.find_element_by_link_text("About")
        main.send_keys(Keys.RETURN)
        # Wait 10 (sec) click More button
        driver.implicitly_wait(10)
        main = driver.find_element_by_link_text("MORE")
        main.send_keys(Keys.RETURN)
        
        driver.implicitly_wait(10)
        main = driver.find_element_by_link_text("CONTACT US")
        main.send_keys(Keys.RETURN)
        
        driver.implicitly_wait(10)
        main = driver.find_element_by_id("g63-name").send_keys("Test")        
        main = driver.find_element_by_id("g63-email").send_keys("ryansinnott58@gmail.com")  
        main = driver.find_element_by_id("contact-form-comment-g63-message").send_keys("Testing 123")
        main = driver.find_element_by_class_name("wp-block-button__link")
        main.send_keys(Keys.RETURN)
        
 
 
if __name__ == "__main__":
	unittest.main()
# class SearchText(unittest.TestCase):
#     def setUp(self):
#         # create a new Firefox session
#         self.driver = webdriver.Chrome()
#         # self.driver.implicitly_wait(30)
#         # self.driver.maximize_window()
#         # # navigate to the application home page
#         self.driver.get("https://www.koluit.com")

    # def test_search_by_text(self):
    #     # get the search textbox
    #     self.search_field = self.driver.find_element_by_name("q")

    #     # enter search keyword and submit
    #     self.search_field.send_keys("Finance")
    #     self.search_field.submit()

    #     #get the list of elements which are displayed after the search
    #     #currently on result page usingfind_elements_by_class_namemethod

    #     lists = self.driver.find_elements_by_class_name("r")
    #     no=len(lists)
    #     self.assertEqual(10, len(lists))