#! usr/bin/env python
# -*- coding:utf-8 -*-
from Network import Network
from time import time
from Saver import Saver

if __name__ == "__main__":

    net = Network()
    saver = Saver()
    net.Monte_Carlo_Times = 30000
    intervals = [_ / 365 for _ in range(1, 400)]
    for interval in intervals:
        saver.info_log("Starting simulation, interval" + str(interval))
        begin = time()
        res = net.output(parallel=True, interval=interval)
        res["time_spend"] = time() - begin
        print("output", res)
        saver.info_log("End simulation")
        saver.add_result(res)
