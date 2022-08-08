from typing import List

# 普通版本
def normal(array: list, reverse: bool=False) -> None:
    '''
    array: 支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    reverse: 是否降序, 默认采用升序。
    '''
    for i in range(len(array) - 1): # loop to access each array element
        for j in range(len(array) - i - 1): # loop to compare array elements
        # compare two adjacent elements and change > to < to sort in descending order
            if (array[j] < array[j + 1] if reverse else array[j] > array[j + 1]):
                # swapping elements if elements are not in the intended order
                array[j], array[j + 1] = array[j + 1], array[j]

# 添加旗帜
def flag(array: list, reverse: bool=False) -> None:
    '''
    array: 支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    reverse: 是否降序, 默认采用升序。
    '''
    for i in range(len(array) - 1):
        flag = False # 旗帜
        for j in range(len(array) - i - 1):
            if (array[j] < array[j + 1] if reverse else array[j] > array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = True
        if not flag:
            break

# 双向排序
def bidirect(array: list, reverse: bool=False) -> None:
    '''
    array: 支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    reverse: 是否降序, 默认采用升序。
    '''
    for i in range(len(array) - 1):
        flag = False
        for j in range(len(array) - i - 1):
            if (array[j] < array[j + 1] if reverse else array[j] > array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = True
        if flag: # 反向排序
            flag = False
            for j in range(len(array) - i - 2, 0, -1):
                if (array[j - 1] < array[j] if reverse else array[j - 1] > array[j]):
                    array[j], array[j - 1] = array[j - 1], array[j]
                    flag = True
        if not flag:
            break