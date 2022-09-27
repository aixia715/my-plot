# -*- coding: utf-8 -*-
# @Time    : 2022/2/2 9:07 PM
# @Author  : Tong Huaqing
# @File    : PathUtils.py
# @Comment :

import os


def is_path(file):
    return "/" in file or "\\" in file


def ext(file):
    """
    获取文件的扩展名
    :param file: 文件名或路径
    :return: 文件的扩展名(不包含".")
    """
    base, ex = os.path.splitext(file)
    ext_sep_len = len(os.path.extsep)
    return ex[ext_sep_len:]


def filename_without_ext(path):
    """
    从文件路径当中获取不含扩展名的文件名
    :param path:
    :return:
    """
    filename_ext = os.path.basename(path)
    filename, _ = os.path.splitext(filename_ext)
    return filename
