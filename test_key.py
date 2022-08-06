from typing import List
from utils import cmp

def bubble_sort(array: List, key=None, reverse: bool=False) -> None:
    '''
    array: 同一数据维度下，支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    key: lambda函数, 仅含一个参量，用于关键字排序, 例如: key=lambda x: x[1], key=lambda x: (x[0], x[1])
    reverse: 是否降序, 默认采用升序。
    '''
    compare = list(map(key, array)) if key != None else array
    compare = ([[value] for value in compare] if compare and compare[0] is not list else compare) if key != None else array
    for i in range(len(array) - 1): # loop to access each array element
        for j in range(len(array) - i - 1): # loop to compare array elements
        # compare two adjacent elements and change > to < to sort in descending order
            if (compare[j] < compare[j + 1] if reverse else compare[j] > compare[j + 1]) if not key else cmp(compare[j], compare[j + 1], reverse):
                # swapping elements if elements are not in the intended order
                array[j], array[j + 1] = array[j + 1], array[j]
                if key != None:
                    compare[j], compare[j + 1] = compare[j + 1], compare[j]