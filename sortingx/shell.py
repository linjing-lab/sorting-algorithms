from typing import List

# 标准版本
def standard(array: List, reverse: bool=False) -> None:
    '''
    array: 支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    reverse: 是否降序, 默认采用升序。
    '''
    length = len(array)
    gap = length // 2 # set gap
    while gap >= 1:
        for index in range(length):
            next = index
            while next >= gap and array[next - gap] < array[next] if reverse else array[next - gap] > array[next]: # insertion sort
                array[next], array[next - gap] = array[next - gap], array[next]
                next -= gap
        gap //= 2 # renew

# 