# 算法模块
from sortings.insertion import Direct, Binary
from sortings.counting import Whiledivide, Forenumerate, Reversefill
from sortings.bubble import Doubleloop, Flag, Bidirection
from sortings.merge import Recursion, Stack
from sortings.quick import Lambda, Recursion, Stack

# 其他模块
import time
from numpy import array
import polars as pl
import random
import copy

# 生成测试数据
data = [random.randint(0, 100) for i in range(10000)]

# 快速排序算法对比
def Quicksort(array, l=0, r=9999):
    method_list = ["Lambda", "Recursion", "Stack"]
    dictionary = {}
    for method in method_list:
        function = eval(method)
        if method == "Lambda":
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
    method_list = ["Recursion", "Stack"]
    dictionary = {}
    for method in method_list:
        function = eval(method)
        if method == "Recursion":
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
    method_list = ["Doubleloop", "Flag", "Bidirection"]
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
    method_list = ["Whiledivide", "Forenumerate", "Reversefill"]
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
    method_list = ["Direct", "Binary"]
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