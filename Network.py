#! usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author: Haitao yue
Description: Define the network
"""
import networkx as nx
from Arcs import arcs
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

    def get_max_flow(self, broken_arcs=None):
        for break_arc in broken_arcs:
            assert break_arc in self.__maintainableArc
            self.__G[arcs[break_arc]["from"]][arcs[break_arc]["to"]]["capacity"] = 0
        res = self.__get_max_flow()
        for break_arc in broken_arcs:
            assert break_arc in self.__maintainableArc
            self.__G[arcs[break_arc]["from"]][arcs[break_arc]["to"]]["capacity"] = arcs[break_arc]["capacity"]
        return res

    def __is_satisfy_demand(self):
        maximum_flow = self.__get_max_flow()
        assert maximum_flow <= self.__demand
        return maximum_flow == self.__demand

    def draw(self):
        from matplotlib import pyplot as plt
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

    def _monte_carlo(self, times=1000, interval=1.0, is_success_times=True):
        assert times <= self.Monte_Carlo_Times
        if is_success_times:
            success_times = 0
            for index in range(times):
                broken_arcs = self.__get_broken_arcs(interval)
                success_times = success_times + 1 if self.is_satisfy_demand(broken_arcs) else success_times
            return success_times
        else:
            max_flow_list = [0] * times
            for index in range(times):
                broken_arcs = self.__get_broken_arcs(interval)
                max_flow_list[index] = self.get_max_flow(broken_arcs)
            return max_flow_list

    def get_reliability(self, interval=1.0, parallel=True):
        if not parallel:
            return self._monte_carlo(times=self.Monte_Carlo_Times, interval=interval) / self.Monte_Carlo_Times
        else:
            import multiprocessing as mp
            num_cores = int(mp.cpu_count())
            pool = mp.Pool(num_cores)
            results = [pool.apply_async(self._monte_carlo,
                                        args=(self.Monte_Carlo_Times // num_cores, interval, True))
                       for _ in range(num_cores)]
            results = [p.get() for p in results]
            pool.close()
            return sum(results) / self.Monte_Carlo_Times

    def get_outflows(self, interval=1.0, parallel=False):
        if not parallel:
            return self._monte_carlo(times=self.Monte_Carlo_Times, interval=interval, is_success_times=False)
        else:
            import multiprocessing as mp
            num_cores = int(mp.cpu_count())
            pool = mp.Pool(num_cores)
            results = [pool.apply_async(self._monte_carlo,
                                        args=(self.Monte_Carlo_Times // num_cores, interval, False))
                       for _ in range(num_cores)]
            output = []
            results = [output.extend(p.get()) for p in results]
            pool.close()
            return output

    def maintenance_cost(self, interval=1.0):
        res = 0
        for arc in self.__maintainableArc:
            res += (1 - 0.5 * exp(-1 * arcs[arc]["fail_rate"] * interval)) * arcs[arc]["maintain_cost"]
        return res * self.__totalTimeHorizon / interval

    def output(self, parallel=False, interval=1.0):
        from numpy import var, mean
        outflows = self.get_outflows(interval=interval, parallel=parallel)
        res = {
            "interval": interval,
            "isParallel": parallel,
            "Monte_Carlo_Times": self.Monte_Carlo_Times,
            "maintain_cost": self.maintenance_cost(interval=interval),
            "reliability": sum(_ >= self.__demand for _ in outflows) / outflows.__len__(),
            "time_spend": 0,
            "maximum_flow_mean": mean(outflows),
            "maximum_flow_variance": var(outflows),
        }
        return res
