from typing import List

# 普通版本
def normal(array: List) -> None:
    '''
    原址排序：支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    '''
    length = len(array)
    for index in range(length - 1):
        mind = index # 标记最小关键字位置
        for next in range(index + 1, length): # 搜索
            if array[mind] > array[next]:
                mind = next
        array[index], array[mind] = array[mind], array[index]

# 标记最大值
def withmax(array: List) -> None:
    '''
    原址排序：支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    '''
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