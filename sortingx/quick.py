from typing import List

# lambda实现
def lamb(array: List) -> List:
	quick_sort = lambda array: array if len(array) <= 1 else quick_sort([item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort([item for item in array[1:] if item > array[0]])
	return quick_sort(array)

# 递归实现
def recursion(array: List, l: int, r: int) -> None:
	def quick_sort(array: List, l: int, r: int) -> None:
		if l < r:
			mid = partition(array, l, r)
			quick_sort(array, l, mid - 1)
			quick_sort(array, mid + 1, r)
	
	def partition(array: List, l: int, r: int) -> int:
		value = array[r]
		index = l - 1
		for ind in range(l, r):
			if array[ind] <= value:
				index += 1
				array[index], array[ind] = array[ind], array[index]
		array[index + 1], array[r] = array[r], array[index + 1]
		return index + 1
	quick_sort(array, l, r)

# 非递归实现
def stack(array: List, l: int, r: int) -> None:
	if l >= r:
		return
	stack = []
	stack.append(l)
	stack.append(r)
	while stack:
		low = stack.pop(0)
		high = stack.pop(0)
		if high - low <= 0:
			continue
		value = array[high]
		index = low - 1
		for ind in range(low, high):
			if array[ind] <= value:
				index += 1
				array[index], array[ind] = array[ind], array[index]
		array[index + 1], array[high] = array[high], array[index + 1]
		stack.extend([low, index, index+2, high])