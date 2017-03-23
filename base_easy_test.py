# coding=utf8

from selenium import webdriver
import unittest
import utils


class Base_Easy_Test(unittest.TestCase):
        siteurl = ""
        site_title = ""
        driver = ""

        def setUp(self):
                self.select_driver_adapter()

        def default_action(self):
                self.driver.get(self.siteurl)
                # self.assertIn(self.site_title,  self.driver.title)

        def tearDown(self):
                pass

        def close_web_browser(self):
                self.driver.quit()

        def close_web_tab(self):
                self.driver.close()

        def select_driver_adapter(self, driver_name=""):
                select_driver_name = "chrome" if driver_name == "" else driver_name

                if select_driver_name.lower() == "firefox":
                        self.driver = webdriver.Firefox()
                elif select_driver_name.lower() == "chrome":
                        self.driver = webdriver.Chrome()
                else:
                        utils.record_log("select web driver name is wrong")
                        self.driver = ""
