from typing import List

# 普通版本
def normal(array: List) -> None:
    length = len(array)
    for index in range(length - 1):
        mind = index # 标记最小关键字位置
        for next in range(index + 1, length): # 搜索
            if array[mind] > array[next]:
                mind = next
        array[index], array[mind] = array[mind], array[index]

# 标记最大值
def withmax(array: List) -> None:
    length = len(array)
    for index in range(length // 2):
        mind = index
        maxd = length - index - 1
        for next in range(index, length - index):
            if array[mind] > array[next]:
                mind = next
            if array[maxd] < array[next]:
                maxd = next
        array[mind], array[index] = array[index], array[mind]
        array[maxd], array[length - index - 1] = array[length - index - 1], array[maxd]