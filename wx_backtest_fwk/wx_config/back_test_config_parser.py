#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import os
import logging
from configparser import ConfigParser


class BackTestConfig(object):
    def __init__(self):
        self.config_parser = ConfigParser()
        self.config_parser.read(os.path.join(os.path.dirname(__file__), 'back_test_config.ini'),
                                encoding="utf-8")
        self.configs = {}
        self.init_configs()

    def init_configs(self):
        pass

    def init_account(self):
        if not self.config_parser.has_section("account"):
            logging.error("")
            exit(1)
        if not self.config_parser.has_option("account", "init_money"):
            logging.error("")
            exit(1)
        init_money = self.config_parser.get("account", "init_money")
        if not init_money.isdigit():
            logging.error("")
            exit(1)
        self.configs["init_money"] = int(init_money)

    def init_time(self):
        pass

    def init_trade(self):
        pass

    def get(self, param):
        self.configs.get(param)


if __name__ == '__main__':
    back_test_config = BackTestConfig()
