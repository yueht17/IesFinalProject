#! usr/bin/env python
# -*- coding:utf-8 -*-
import logging  # 引入logging模块
import os.path
import time
import json


class Saver():
    def __init__(self):
        self.__rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        self.__path = "./output/" + self.__rq
        self.__log_file = "./output/" + self.__rq + "/log.txt"
        self.__json_file = "./output/" + self.__rq + "/results.json"
        self.__init_path()
        self.__init_json_saver()
        self.__logger = logging.getLogger()
        self.__logger.setLevel(logging.INFO)
        self.__init_logger()

    def __init_path(self):
        if not os.path.isdir("./output"):
            os.mkdir("./output")
        if not os.path.isdir(self.__path):
            os.mkdir(self.__path)

    def __init_logger(self):
        if not os.path.isfile(self.__log_file):
            f = open(self.__log_file, "w", encoding='utf-8')
            f.close()
        fh = logging.FileHandler(self.__log_file, mode='w')
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        fh.setFormatter(formatter)
        self.__logger.addHandler(fh)

    def __init_json_saver(self):
        if not os.path.isfile(self.__json_file):
            f = open(self.__json_file, "w", encoding='utf-8')
            f.close()

    def info_log(self, log):
        self.__logger.info(log)

    def add_result(self, result):
        assert type(result) == dict
        self.info_log("Start saving result")
        with open(self.__json_file, "r+") as f:
            try:
                results = json.load(f)
            except json.decoder.JSONDecodeError:
                results = []
        results.append(result)
        with open(self.__json_file, "w+") as f:
            json.dump(results, f)
        self.info_log("End saving result")
