# coding=utf8

import base_easy
import utils
from selenium.webdriver.common.keys import Keys


class Easy_Cnblogs(base_easy.Base_Easy):
        search_key = "golang"
        siteurl = "http://www.cnblogs.com/"
        site_title = "cnblogs"

        def cnblog_search(self, search_key=""):
                self.driver.get(self.siteurl)
                elem = self.driver.find_element_by_id("zzk_q")

                search_key = self.search_key if search_key == "" else search_key
                elem.send_keys(search_key)
                elem.send_keys(Keys.ENTER)

                return self.driver.page_source

        def cnblog_search_golang(self):
                self.select_driver_adapter()
                page_info = self.cnblog_search('golang')
                if 'golang' in page_info:
                        msg = "cnblog search work succes"
                else:
                        msg = "cnblog search work failed"

                utils.record_log(msg)

        def cnblog_search_nosql(self):
                page_info = self.cnblog_search('nosql')
                if 'nosql' in page_info:
                        msg = "cnblog search work succes"
                else:
                        msg = "cnblog search work failed"

                utils.record_log(msg)

        def save_upload_search_nosql(self):
                self.cnblog_search_nosql()
                self.save_and_uload_snapshot()

        def run_jobs(self):
                # self.cnblog_search_golang()
                # self.cnblog_search_nosql()
                self.save_upload_search_nosql()
