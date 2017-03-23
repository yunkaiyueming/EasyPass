# coding=utf8

import base_easy
from selenium.webdriver.common.keys import Keys
import utils


class Easy_Yama(base_easy.Base_Easy):
        siteurl = "xx"
        site_title = "xx"
        is_login = False
        login_user = "xx"
        login_pwd = "xx"

        login_btn_id = "cas_login_btn"
        login_user_id = "username"
        login_pwd_id = "password"

        def login_yama(self):
                self.default_action()
                login_elem = self.driver.find_element_by_id(self.login_btn_id)
                login_elem.click()

                login_user_field = self.driver.find_element_by_id(self.login_user_id)
                login_user_field.send_keys(self.login_user)
                login_pwd_field = self.driver.find_element_by_id(self.login_pwd_id)
                login_pwd_field.send_keys(self.login_pwd)
                submit_elem = self.driver.find_element_by_name("submit")
                submit_elem.click()

                if 'YaMa' in self.driver.title:
                        msg = "yama login success"
                        self.is_login = True
                else:
                        self.is_login = False
                        msg = "yama login failed"
                utils.record_log(msg)
                print msg

        def check_login(self):
                if not self.is_login:
                        self.login_yama()

        def visit_24hours_url_view(self):
                self.check_login()
                self.driver.get(self.siteurl + "daily_report/hour_url_action")
                if "用户量".decode("utf-8") in self.driver.page_source:
                        msg = "24hours url work success"
                else:
                        msg = "24hours url work failed"
                utils.record_log(msg)
                print msg

        def visit_url_action(self):
                self.check_login()
                self.driver.get(self.siteurl + "daily_report/url_action")
                if "URL" in self.driver.page_source:
                        msg = "daily url action work success"
                else:
                        msg = "daily url action work failed"
                utils.record_log(msg)
                print msg

        def run_jobs(self):
                self.visit_24hours_url_view()
                self.visit_url_action()
