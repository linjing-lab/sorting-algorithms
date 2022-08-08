from typing import List

# Donald Shell
def donald(array: List, reverse: bool=False) -> None:
    '''
    array: 支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    reverse: 是否降序, 默认采用升序。
    '''
    length = len(array)
    gap = length // 2 # set gap
    while gap >= 1:
        for index in range(gap, length):
            next = index
            while next >= gap and array[next - gap] < array[next] if reverse else array[next - gap] > array[next]: # insertion sort
                array[next], array[next - gap] = array[next - gap], array[next]
                next -= gap
        gap //= 2 # renew

# 修改增量
def mobase(array: List, base: int=2, reverse: bool=False) -> None:
    '''
    array: 支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    reverse: 是否降序, 默认采用升序。
    '''
    length = len(array)
    gap = length // base
    while gap >= 1:
        for index in range(gap, length):
            next = index
            while next >= gap and array[next - gap] < array[next] if reverse else array[next - gap] > array[next]:
                array[next], array[next - gap] = array[next - gap], array[next]
                next -= gap
        gap //= base

