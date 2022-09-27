# -*- coding: utf-8 -*-
# @Time    : 2022/9/27 23:01
# @Author  : Tong Huaqing
# @File    : plot_csv.py
# @Comment :

from data_csv import DataCsv
import typing

import matplotlib.pyplot as plt


class PlotCSV(object):
    def __init__(self):
        self.csv_list: typing.List[DataCsv] = []
        pass

    def add_csv(self, csv_obj: DataCsv):
        self.csv_list.append(csv_obj)

    def plot(self, title, xlabel, ylabel):
        param = []
        for csv_obj in self.csv_list:
            param.append(csv_obj.x)
            param.append(csv_obj.y)

        plt.plot(*param)
        plt.title(title, fontsize=12)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        plt.show()


if __name__ == "__main__":
    csv_obj = DataCsv(path='test_data/test.csv')
    plot = PlotCSV()
    plot.add_csv(csv_obj)
    plot.plot('Test', 'freq', 'phase noise')
