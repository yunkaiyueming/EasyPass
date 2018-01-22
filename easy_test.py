# coding=utf8

import base_easy
from selenium.webdriver.common.keys import Keys
import utils
import ConfigParser
from selenium.webdriver.common.action_chains import *
import time

#http://seleniumhq.github.io/selenium/docs/api/py/
#https://selenium-python-zh.readthedocs.io/en/latest/

class Easy_wbtest(base_easy.Base_Easy):

        def test(self):
                self.driver.get("https://www.baidu.com")
                elem = self.driver.find_element_by_name("wd")
                elem.send_keys("python selenium")
                elem.send_keys(Keys.ENTER)

                #self.driver.get("http:www.google.com")

                for handle in self.driver.window_handles:
                        print self.driver.switch_to_window(handle)

                print  self.driver.get_cookies()
                print self.driver.get_window_position()
#                print self.driver.get_window_rect()
                print self.driver.get_window_size()
                print self.driver.refresh()
                print self.driver.current_window_handle
                print self.driver.current_url
                print self.driver.current_window_handle
                print self.driver.name
                print self.driver.title

            #    ActionChains(self.driver).move_by_offset(100,100)

if __name__ == '__main__':
        Easy_wbtest().test()