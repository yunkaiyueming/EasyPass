# coding=utf8

from selenium.webdriver.common.keys import Keys
import base_easy
import utils


class Easy_Baidu(base_easy.Base_Easy):
        search_key = "python"
        siteurl = "https://www.baidu.com"
        site_title = "baidu"

        def baidu_search(self, search_key=""):
                self.default_action()
                elem = self.driver.find_element_by_name("wd")

                search_key = self.search_key if search_key == "" else search_key
                elem.send_keys(search_key)
                elem.send_keys(Keys.ENTER)

                return self.driver.page_source

        def search_python(self):
                page_info = self.baidu_search("python")
                if "No results found" in page_info:
                        msg = "search python success"
                else:
                        msg = "search php success"

                utils.record_log(msg)

        def search_php(self):
                page_info = self.baidu_search("python")
                if "No results found" in page_info:
                        msg = "search python success"
                else:
                        msg = "search php success"

                utils.record_log(msg)

        def run_jobs(self):
                self.search_php()
                self.search_python()
