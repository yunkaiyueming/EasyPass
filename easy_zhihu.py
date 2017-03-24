# coding=utf8

import base_easy
import utils
import ConfigParser
import json

class Easy_Zhihu(base_easy.Base_Easy):
        siteurl = "xx"
        login_cookies = {}

        def __init__(self):
                base_easy.Base_Easy.__init__(self)
                cf = ConfigParser.ConfigParser()
                cf.read('./config.ini')

                self.siteurl = cf.get('zhihu', 'siteurl')
                login_cookie_json = cf.get('zhihu', 'login_cookie_json')
                self.login_cookies = json.loads(login_cookie_json, encoding="utf8");

        def login_zhihu(self):
                pass

        def get_new_msg_count(self):
                self.driver.get(self.siteurl)
                for k, v in self.login_cookies.items():
                        self.driver.add_cookie({'name': k, 'value': v})

                self.driver.get(self.siteurl)
                new_msg_div = self.driver.find_element_by_id("zh-top-nav-count")
                count_num = new_msg_div.text
                utils.record_log("new count num : " + count_num)

        def save_snot_img(self):
                self.get_new_msg_count()

                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                self.save_and_uload_snapshot()

        def run_jobs(self):
                self.save_snot_img()

        if __name__ == '__main__':
                import easy_zhihu
                easy_zhihu.Easy_Zhihu()
