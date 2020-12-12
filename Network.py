#! usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author: Haitao yue
Description: Define the network
"""
import networkx as nx
from Arcs import arcs
from matplotlib import pyplot as plt
from random import random
from math import exp


class Network():
    def __init__(self):
        self.__demand = 40
        self.__G = nx.DiGraph()
        self.__totalTimeHorizon = 50
        self.__maintainableArc = ["arc_" + str(_) for _ in range(1, 25)]
        self.Monte_Carlo_Times = 10000

        #  ini network
        for key, val in arcs.items():
            self.__G.add_edge(u_of_edge=val["from"], v_of_edge=val["to"], label="key", capacity=val["capacity"])

    def __get_max_flow(self):
        flow_value, flow_dict = nx.maximum_flow(self.__G, "s", "d")
        return flow_value

    def __is_satisfy_demand(self):
        maximum_flow = self.__get_max_flow()
        assert maximum_flow <= self.__demand
        return maximum_flow == self.__demand

    def draw(self):
        nx.draw(self.__G, with_labels=True)
        plt.show()

    def is_satisfy_demand(self, broken_arcs=None):
        for break_arc in broken_arcs:
            assert break_arc in self.__maintainableArc
            self.__G[arcs[break_arc]["from"]][arcs[break_arc]["to"]]["capacity"] = 0
        res = self.__is_satisfy_demand()
        for break_arc in broken_arcs:
            assert break_arc in self.__maintainableArc
            self.__G[arcs[break_arc]["from"]][arcs[break_arc]["to"]]["capacity"] = arcs[break_arc]["capacity"]
        return res

    def __get_broken_arcs(self, interval=1.0):
        res = []
        # prob_list = []
        for arc in self.__maintainableArc:
            prob = 1 - exp(-1 * arcs[arc]["fail_rate"] * interval)
            # prob_list.append(prob)
            if prob >= random():
                res.append(arc)
        # print(prob_list)
        return res

    def reliability(self, interval=1.0):
        success_times = 0
        for index in range(self.Monte_Carlo_Times):
            broken_arcs = self.__get_broken_arcs(interval)
            success_times = success_times + 1 if self.is_satisfy_demand(broken_arcs) else success_times
        return success_times / self.Monte_Carlo_Times

    def maintenance_cost(self, interval=1.0):
        res = 0
        for arc in self.__maintainableArc:
            res += (1 - 0.5 * exp(-1 * arcs[arc]["fail_rate"] * interval)) * arcs[arc]["maintain_cost"]
        return res * self.__totalTimeHorizon / interval
