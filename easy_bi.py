# coding=utf8

import utils
import base_easy
import ConfigParser


class Easy_Bi(base_easy.Base_Easy):
        siteurl = ''
        cas_login_url = ''
        is_login = False

        login_user = ""
        login_pwd = ""

        login_btn_id = "cas_login_btn"
        login_user_id = "username"
        login_pwd_id = "password"

        def __init__(self):
                base_easy.Base_Easy.__init__(self, 'phantomjs')

                cf = ConfigParser.ConfigParser()
                cf.read('./config.ini.bk')
                self.login_user = cf.get('login_account', 'login_user')
                self.login_pwd = cf.get('login_account', 'login_pwd')
                self.siteurl = cf.get('bi', 'siteurl')
                self.site_title = cf.get('bi', 'site_title')
                self.applist_url = cf.get('bi', 'applist_url')
                self.boss_month_cost_url = cf.get('bi', 'boss_month_cost_url')

        def home_page_login(self):
                self.driver.get(self.siteurl)
                login_btn = self.driver.find_element_by_partial_link_text("统一账户登录")
                login_btn.click()

        def cas_login(self):
                self.driver.get(self.cas_login_url)

        def login_bi(self):
                self.home_page_login()

                login_user_field = self.driver.find_element_by_id(self.login_user_id)
                login_user_field.send_keys(self.login_user)
                login_pwd_field = self.driver.find_element_by_id(self.login_pwd_id)
                login_pwd_field.send_keys(self.login_pwd)
                submit_elem = self.driver.find_element_by_name("submit")
                submit_elem.click()

                if 'BI' in self.driver.title:
                        msg = "bi login success"
                        self.is_login = True
                else:
                        self.is_login = False
                        msg = "bi login failed"
                utils.record_log(msg)

        def check_login(self):
                if not self.is_login:
                        self.login_bi()

        def some_game_applist_snapshot(self):
                self.check_login()

                self.driver.get(self.applist_url)
                self.save_snapshot()

        def get_boss_month_user_response_time(self):
                self.check_login()

                print self.boss_month_cost_url
                resp_time = self.get_page_response_time(self.boss_month_cost_url)
                print "boss big view time:", resp_time

        def run_jobs(self):
                self.some_game_applist_snapshot()

        def test_windows(self):
                self.driver.get(self.siteurl)
                for handle in self.driver.window_handles:
                        self.driver.switch_to_window(handle)

                self.driver.get(self.cas_login_url)
                for handle in self.driver.window_handles:
                        self.driver.switch_to_window(handle)

        def get_window_info(self):
                self.driver.get("http://www.baidu.com")
                print self.driver.get_window_size()
                self.driver.maximize_window()
                print self.driver.get_window_size()

        def scroll_window(self):
                self.driver.get("http://www.baidu.com")
                self.driver.set_window_size(500, 300)
                # self.driver.set_window_position()
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                print self.driver.get_window_size()

                self.driver.create_options()

        if __name__ == '__main__':
                import easy_bi
                easy_bi.Easy_Bi().get_boss_month_user_response_time()
