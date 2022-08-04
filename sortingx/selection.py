from typing import List

from cv2 import norm

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
    scope = length // 2
    for index in range(scope):
        mind, maxd = index, index # 从一个方向搜索来保证单调性
        for next in range(index + 1, length - index):
            if array[mind] > array[next]:
                mind = next
            if array[maxd] < array[next]:
                maxd = next
        array[mind], array[index] = array[index], array[mind]
        maxd = mind if index == maxd else maxd
        array[maxd], array[length - index - 1] = array[length - index - 1], array[maxd]