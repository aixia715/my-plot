# -*- coding: utf-8 -*-
# @Time    : 2022/9/27 23:01
# @Author  : Tong Huaqing
# @File    : plot_csv.py
# @Comment :

from data_csv import DataCsv
import typing
import matplotlib.cm as cm
import numpy as np
import matplotlib.pyplot as plt


class PlotCSV(object):
    def __init__(self):
        self.csv_list: typing.List[DataCsv] = []
        self.plot_param = None
        pass

    def add_csv(self, csv_obj: DataCsv):
        self.csv_list.append(csv_obj)

    def set_plot_param(self, title, xlabel, ylabel, grid=False, figsize=None):
        self.plot_param = {'title': title, 'xlabel': xlabel, 'ylabel': ylabel, 'grid': grid, 'figsize': figsize}

    def semilogx(self):
        # 绘制x坐标为对数的图
        colors = cm.rainbow(np.linspace(0, 1, len(self.csv_list)))
        assert self.plot_param is not None
        plt.figure(figsize=self.plot_param['figsize'])  # 新建图
        plt.grid(self.plot_param['grid'])
        plt.title(self.plot_param['title'], fontsize=12)
        plt.xlabel(self.plot_param['xlabel'])
        plt.ylabel(self.plot_param['ylabel'])
        for i, csv_obj in enumerate(self.csv_list):
            plt.semilogx(csv_obj.x, csv_obj.y, color=colors[i])

        plt.show()


if __name__ == "__main__":
    csv_obj = DataCsv(path='test_data/test.csv')
    plot = PlotCSV()
    plot.add_csv(csv_obj)
    plot.set_plot_param(
        title='Test',
        xlabel='freq',
        ylabel='phase noise',
        grid=True,
        figsize=(12, 6)
    )
    plot.plot('Test', 'freq', 'phase noise')
