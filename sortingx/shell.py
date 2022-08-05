from typing import List

# 标准版本
def standard(array: List, reverse: bool=False) -> None:
    '''
    支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    '''
    length = len(array)
    gap = length // 2 # set gap
    while gap >= 1:
        for index in range(length):
            next = index
            compare = array[next - gap] < array[next] if reverse else array[next - gap] > array[next]
            while next >= gap and compare: # insertion sort
                array[next], array[next - gap] = array[next - gap], array[next]
                next -= gap
        gap //= 2 # renew

# 