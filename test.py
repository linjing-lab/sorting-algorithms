# 导包
import time
import polars as pl
import random
import copy
from typing import List

# 生成测试数据
data = [random.randint(0, 100) for _ in range(10000)]

# 快速排序算法对比
def Quicksort(array: List, l: int=0, r: int=9999):
    from sortingx.quick import lamb, recur, stack
    method_list = ["lamb", "recur", "stack"]
    dictionary = {}
    for method in method_list:
        function = eval(method)
        if method == "lamb":
            times = time.time()
            function(copy.deepcopy(array))
            timee = time.time()
        else:
            times = time.time()
            function(copy.deepcopy(array), l, r)
            timee = time.time()
        gap = round(timee - times, 2)
        gap_list = [gap]
        dictionary[method] = gap_list
    df = pl.DataFrame(dictionary)
    return df

print(Quicksort(data))

# 归并排序算法的对比
def Mergesort(array: List):
    from sortingx.merge import recur, stack
    method_list = ["recur", "stack"]
    dictionary = {}
    for method in method_list:
        function = eval(method)
        if method == "recursion":
            times = time.time()
            function(array)
            timee = time.time()
        else:
            times = time.time()
            function(copy.deepcopy(array))
            timee = time.time()
        gap = round(timee - times, 2)
        gap_list = [gap]
        dictionary[method] = gap_list
    df = pl.DataFrame(dictionary)
    return df

print(Mergesort(data))

# 冒泡排序算法的对比
def Bubblesort(array: List):
    from sortingx.bubble import normal, flag, bidirect
    method_list = ["normal", "flag", "bidirect"]
    dictionary = {}
    for method in method_list:
        function = eval(method)
        times = time.time()
        function(copy.deepcopy(array))
        timee = time.time()
        gap = round(timee - times, 2)
        gap_list = [gap]
        dictionary[method] = gap_list
    df = pl.DataFrame(dictionary)
    return df

print(Bubblesort(data))

# 计数排序算法的对比
def Countingsort(array: List):
    from sortingx.counting import whilediv, forenum, reverfill
    method_list = ["whilediv", "forenum", "reverfill"]
    dictionary = {}
    for method in method_list:
        function = eval(method)
        times = time.time()
        function(copy.deepcopy(array))
        timee = time.time()
        gap = round(timee - times, 2)
        gap_list = [gap]
        dictionary[method] = gap_list
    df = pl.DataFrame(dictionary)
    return df

print(Countingsort(data))

# 插入排序算法的对比
def Insertionsort(array: List):
    from sortingx.insertion import direct, binary
    method_list = ["direct", "binary"]
    dictionary = {}
    for method in method_list:
        function = eval(method)
        times = time.time()
        function(copy.deepcopy(array))
        timee = time.time()
        gap = round(timee - times, 2)
        gap_list = [gap]
        dictionary[method] = gap_list
    df = pl.DataFrame(dictionary)
    return df

print(Insertionsort(data))

# 选择排序算法的对比
def Selectionsort(array: List):
    from sortingx.selection import normal, withmax
    method_list = ["normal", "withmax"]
    dictionary = {}
    for method in method_list:
        function = eval(method)
        times = time.time()
        function(copy.deepcopy(array))
        timee = time.time()
        gap = round(timee - times, 2)
        gap_list = [gap]
        dictionary[method] = gap_list
    df = pl.DataFrame(dictionary)
    return df

print(Selectionsort(data))

# 桶排序算法的对比
def Bucketsort(array: List):
    from sortingx.bucket import numeric, mobase
    method_list = ["numeric", "mobase"]
    dictionary = {}
    for method in method_list:
        function = eval(method)
        times = time.time()
        function(copy.deepcopy(array))
        timee = time.time()
        gap = round(timee - times, 2)
        gap_list = [gap]
        dictionary[method] = gap_list
    df = pl.DataFrame(dictionary)
    return df

print(Bucketsort(data))