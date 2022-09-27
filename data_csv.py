# -*- coding: utf-8 -*-
# @Time    : 2022/9/27 22:13
# @Author  : Tong Huaqing
# @File    : data_csv.py
# @Comment :


import csv


class DataCsv:
    def __init__(self, path):
        self.path = path
        l = []
        with open(path, 'rt', encoding='utf-8-sig') as f:
            cr = csv.DictReader(f)
            for row in cr:
                l.append(row)
        pass


if __name__ == '__main__':
    data = DataCsv(path='test_data/test.csv')
    pass
