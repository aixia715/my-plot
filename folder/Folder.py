# -*- coding: utf-8 -*-
# @Time    : 2022/2/2 5:38 PM
# @Author  : Tong Huaqing
# @File    : Folder.py
# @Comment : 处理文件夹

from .PathUtils import *


class Folder:
    def __init__(self, path: str):
        self._path = os.path.abspath(path)  # 一开始就转换为绝对路径, 使后面不需要进行判断

    @property
    def path(self):
        return self._path

    @property
    def absolute_path(self):
        return os.path.abspath(self.path)

    def _file_full_path(self, file):
        if not is_path(file):
            full_path = os.path.join(self.absolute_path, file)
        else:
            full_path = file
        return full_path

    def iter_all(self, path=False):
        """
        获取所有文件和文件夹的迭代器
        :param path: TRUE返回路径, false返回文件名
        :return: 文件(文件夹)文件名或路径
        """
        for file in os.listdir(self.path):
            if path:
                file = os.path.join(self.path, file)
            yield file

    def iter_file(self, path=False):
        """
        获取所有文件的迭代器
        :param path: TRUE返回路径, false返回文件名
        :return: 文件的文件名或路径
        """
        for file in self.iter_all(path):
            full_path = self._file_full_path(file)
            if os.path.isfile(full_path):
                yield file

    def iter_dir(self, path=False):
        """
        获取所有文件夹的迭代器
        :param path: TRUE返回路径, false返回文件名
        :return: 文件夹名或路径
        """
        for file in self.iter_all(path):
            full_path = self._file_full_path(file)
            if os.path.isdir(full_path):
                yield file

    def iter_ext_file(self, ext, path=False):
        """
        获取指定扩展名的文件的迭代器
        :param ext: 扩展名(没有".")
        :param path: TRUE返回路径, false返回文件名
        :return: 文件文件名或路径
        """
        for file in self.iter_file(path):
            _, file_ext = os.path.splitext(file)
            if file_ext == os.path.extsep + ext:
                yield file

    def iter_ext_list_file(self, ext_list, path=False):
        """
        遍历扩展名列表当中的文件
        :param ext_list: 扩展名列表(没有".")
        :param path: TRUE返回路径, false返回文件名
        :return: 文件文件名或路径
        """
        for ext in ext_list:
            for file in self.iter_ext_file(ext, path):
                yield file


if __name__ == '__main__':
    fo = Folder("../log")
    for file in fo.iter_ext_file("xlsx", True):
        print(file)
