# coding=utf8

import base_easy
import ConfigParser
import time

class Easy_58(base_easy.Base_Easy):
        def __init__(self):
                base_easy.Base_Easy.__init__(self)

                cf = ConfigParser.ConfigParser()
                cf.read('./config.ini.bk')
                self.visit_url = cf.get('58', 'visit_url')

        def visit_url_job(self):
                for i in range(500):
                        go_url = self.visit_url + str(i+505)
                        print go_url

                        self.driver.get(go_url)
                        time.sleep(3)

        def run_all_job(self):
                self.visit_url_job()


if __name__ == '__main__':
        import easy_58

        easy_58.Easy_58().run_all_job()
