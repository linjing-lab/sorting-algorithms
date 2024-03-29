# lambda实现
def lamb(array: list, reverse: bool=False) -> list:
	'''
	array: 支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
	reverse: 是否降序, 默认采用升序。
	'''
	quick_sort = lambda array: array if len(array) <= 1 else quick_sort([item for item in array[1:] if (item > array[0] if reverse else item <= array[0])]) + [array[0]] + quick_sort([item for item in array[1:] if (item <= array[0] if reverse else item > array[0])])
	return quick_sort(array)

# 递归实现
def recur(array: list, l: int, r: int, reverse: bool=False) -> None:
	'''
	array: 支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
	l: 数据左侧游标(整型), r: 数据右侧游标(整型)
	reverse: 是否降序, 默认采用升序。
	'''
	if l >= r:
		return None
	def quick_sort(l: int, r: int) -> None:
		'''
		算法主体
		'''
		if l < r:
			mid = partition(l, r)
			quick_sort(l, mid - 1)
			quick_sort(mid + 1, r)
	
	def partition(l: int, r: int) -> int:
		'''
		array: 数据(列表), l: 数据左侧游标(整型), r: 数据右侧游标(整型)
		'''
		value = array[r]
		index = l - 1
		for ind in range(l, r):
			if (array[ind] > value if reverse else array[ind] <= value):
				index += 1
				array[index], array[ind] = array[ind], array[index]
		array[index + 1], array[r] = array[r], array[index + 1]
		return index + 1
	quick_sort(l, r)

# 非递归实现
def stack(array: list, l: int, r: int, reverse: bool=False) -> None:
	'''
	array: 支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
	l: 数据左侧游标(整型), r: 数据右侧游标(整型)
	reverse: 是否降序, 默认采用升序。
	'''
	if l >= r:
		return None
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
			if (array[ind] > value if reverse else array[ind] <= value):
				index += 1
				array[index], array[ind] = array[ind], array[index]
		array[index + 1], array[high] = array[high], array[index + 1]
		stack.extend([low, index, index+2, high])