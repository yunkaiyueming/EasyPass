# coding=utf8

from selenium import webdriver
import utils
import time
import os
import qiniu_help


class Base_Easy():
        siteurl = ""
        site_title = ""
        driver = ""

        def __init__(self, driver_name=""):
                self.select_driver_adapter(driver_name)

        def default_action(self):
                self.driver.get(self.siteurl)

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
                elif select_driver_name.lower() == "phantomjs":
                        self.driver = webdriver.PhantomJS(
                                executable_path=r'D:\phantomjs\phantomjs-2.1.1-windows\bin\phantomjs.exe')
                else:
                        utils.record_log("select web driver name is wrong")
                        self.driver = ""

        def save_snapshot(self, save_name="", width=1000, height=1000):
                self.driver.set_window_size(width, height)
                if not save_name:
                        save_name = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

                save_path = "Shot/" + save_name + ".png"
                utils.record_log(save_path + " save success")
                self.driver.save_screenshot(save_path)
                return save_name + ".png"

        def save_and_uload_snapshot(self, save_name="", width=1000, height=1000):
                auto_save_file_name = self.save_snapshot(save_name, width, height)
                if not save_name:
                        save_name = auto_save_file_name
                local_file_path = "Shot/" + save_name

                if os.path.exists(local_file_path):
                        qiniu_help.upload_file(local_file_path, save_name)
                else:
                        utils.record_log(local_file_path + "file is not exist")

        def get_page_response_time(self, view_url):
                start_time = time.time()
                self.driver.get(view_url)
                end_time = time.time()
                return end_time - start_time
