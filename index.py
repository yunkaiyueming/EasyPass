# -*- coding:utf-8 -*-
import sys
import unittest
import easy_zhihu
import easy_baidu
import easy_yama
import easy_cnblogs


def run_all_job():
        # easy_yama.Easy_Yama().run_jobs()
        # easy_baidu.Easy_Baidu().run_jobs()
        easy_cnblogs.Easy_Cnblogs().run_jobs()
        # easy_zhihu.Easy_Zhihu().run_jobs()
        pass


def get_easy_name():
        all_class_names = []

        for module in sys.modules:
                if 'easy_' in module:
                        names = module.split("_")
                        class_name = ""
                        for name in names:
                                class_name += name.capitalize() + "_"
                        class_name = class_name[0:len(class_name) - 1]
                        all_class_names.append(module + "." + class_name)
        return all_class_names


if __name__ == "__main__":
        run_all_job()
