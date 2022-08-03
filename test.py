# 导包
import time
import polars as pl
import random
import copy

from sklearn.decomposition import DictionaryLearning

# 生成测试数据
data = [random.randint(0, 100) for i in range(10000)]

# 快速排序算法对比
from collection.quick_sort import Lambda, Recursion, Stack
def test_Quicksort(array, l=0, r=9999):
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
print(test_Quicksort(data))

# 归并排序算法的对比
from collection.merge_sort import Recursion, Stack
def test_Mergesort(array):
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
print(test_Mergesort(data))

# 冒泡排序算法的对比
from collection.bubble_sort import Doubleloop, Flag, Bidirection
def test_Bubblesort(array):
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
print(test_Bubblesort(data))