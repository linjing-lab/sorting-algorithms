# 导包
import time
import polars as pl
import random
import copy

# 生成测试数据
data = [random.randint(0, 100) for i in range(10000)]

# 快速排序算法对比
from galley.quick_sort import Lambda, Recursion, Stack
def test_Quicksort(array, l=0, r=9999):
	method_list = ["Lambda", "Recursion", "Stack"]
	dictionary = {}
	for method in method_list:
	    times = time.time()
	    function = eval(method)
	    arr = copy.deepcopy(array)
	    if method == "Lambda":
	    	function(arr) # 深度复制
	    else:
	    	function(arr, l, r)
	    timee = time.time()
	    gap = round(timee - times, 2)
	    gap_list = [gap]
	    dictionary[method] = gap_list
	df = pl.DataFrame(dictionary)
	return df
print(test_Quicksort(data))