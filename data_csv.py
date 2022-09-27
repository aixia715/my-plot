# -*- coding: utf-8 -*-
# @Time    : 2022/9/27 22:13
# @Author  : Tong Huaqing
# @File    : data_csv.py
# @Comment :


import csv
import numpy as np


class DataCsv:
    def __init__(self, path):
        self.path = path
        x = []
        y = []
        with open(path, 'rt', encoding='utf-8-sig') as f:
            cr = csv.reader(f)
            for i, row in enumerate(cr):
                if i == 0:
                    continue
                x.append(float(row[0]))
                y.append(float(row[1]))

        self.x = np.array(x)
        self.y = np.array(y)


if __name__ == '__main__':
    data = DataCsv(path='test_data/test.csv')
    pass
