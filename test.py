# 导包
import time
from numpy import array
import polars as pl
import random
import copy

# 生成测试数据
data = [random.randint(0, 100) for i in range(10000)]

# 快速排序算法对比
def Quicksort(array, l=0, r=9999):
    from sortings.quick import lamb, recursion, stack
    method_list = ["lamb", "recursion", "stack"]
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
def Mergesort(array):
    from sortings.merge import recursion, stack
    method_list = ["recursion", "stack"]
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
def Bubblesort(array):
    from sortings.bubble import doubleloop, flag, bidirection
    method_list = ["doubleloop", "flag", "bidirection"]
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
def Countingsort(array):
    from sortings.counting import whilediv, forenum, reverfill
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
def Insertionsort(array):
    from sortings.insertion import direct, binary
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