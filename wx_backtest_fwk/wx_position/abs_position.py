#!/usr/bin/env python 
# -*- coding:utf-8 -*-


class AbsPosition(object):
    def __init__(self, code):
        self._code = code
        self._total_cost = 0
        self._holding_num = 0
        self._num_of_trades = 0

    @property
    def total_cost(self):
        return self._total_cost

    @total_cost.setter
    def total_cost(self, total_cost):
        if isinstance(total_cost, int):
            self._total_cost = total_cost
        else:
            raise TypeError("Total cost for holding positions should be integer")
