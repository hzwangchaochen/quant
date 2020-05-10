#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import threading


class PositionManager(object):
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with PositionManager._instance_lock:
                if not hasattr(cls, '_instance'):
                    PositionManager._instance = super().__new__(cls)
        return PositionManager._instance

    def __init__(self):
        self.positions = []

    def add_products(self, product_list):
        pass

    def add_product_positions(self, product_code):
        pass

    def remove_product_position(self):
        pass
