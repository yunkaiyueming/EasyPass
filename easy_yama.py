# coding=utf8

import base_easy
from selenium.webdriver.common.keys import Keys
import utils
import ConfigParser


class Easy_Yama(base_easy.Base_Easy):
        siteurl = ""
        site_title = ""
        is_login = False
        login_user = ""
        login_pwd = ""

        login_btn_id = "cas_login_btn"
        login_user_id = "username"
        login_pwd_id = "password"

        def __init__(self):
                base_easy.Base_Easy.__init__(self)

                cf = ConfigParser.ConfigParser()
                cf.read('./config.ini')
                self.login_user = cf.get('login_account', 'login_user')
                self.login_pwd = cf.get('login_account', 'login_pwd')
                self.siteurl = cf.get('yama', 'siteurl')
                self.site_title = cf.get('yama', 'site_title')

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
                        msg = "yama login failed"
                        self.is_login = False
                utils.record_log(msg)

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

        def visit_url_action(self):
                self.check_login()
                self.driver.get(self.siteurl + "daily_report/url_action")
                if "URL" in self.driver.page_source:
                        msg = "daily url action work success"
                else:
                        msg = "daily url action work failed"
                utils.record_log(msg)

        def run_jobs(self):
                self.visit_24hours_url_view()
                self.save_and_uload_snapshot()
                utils.record_log('upload yama 24 hours success')

                self.visit_url_action()
                self.save_and_uload_snapshot()
                utils.record_log('upload yama 24 hours success')

if __name__=='__main__':
        import easy_yama
        easy_yama.Easy_Yama().run_jobs()
