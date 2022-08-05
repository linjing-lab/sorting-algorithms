from typing import List

# while循环
def whilediv(array: List[int]) -> None:
    '''
    原址排序：仅支持全为整数类型的数据。
    '''
    if not array:
        return None
    arrmin = min(array)
    arrmax = max(array)
    count = [0] * (arrmax - arrmin + 1)
    for value in array:
        count[value - arrmin] += 1
    pos = 0 # 游标
    for index in range(arrmin, arrmax + 1): # 从最小的数开始
        while count[index - arrmin] >= 1:
            array[pos] = index
            count[index - arrmin] -= 1
            pos += 1

# enumerate方法
def forenum(array: List[int]) -> None:
    '''
    原址排序：仅支持全为整数类型的数据。
    '''
    if not array:
        return None
    arrmin = min(array)
    arrmax = max(array)
    count = [0] * (arrmax - arrmin + 1)
    for value in array:
        count[value - arrmin] += 1
    array.clear()
    for index, val in enumerate(count):
        for _ in range(val):
            array.append(index + arrmin)

# 反向填充
def reverfill(array: List[int]) -> List[int]:
    '''
    非原址排序：仅支持全为整数类型的数据。
    '''
    if not array:
        return array
    arrmin = min(array)
    arrmax = max(array)
    count = [0] * (arrmax - arrmin + 1)
    result = [0] * len(array)
    for value in array:
        count[value - arrmin] += 1
    for index in range(1, arrmax - arrmin + 1):
        count[index] += count[index - 1]
    for index in range(len(array) - 1, -1, -1):
        result[count[array[index] - arrmin] - 1] = array[index]
        count[array[index] - arrmin] -= 1
    return result