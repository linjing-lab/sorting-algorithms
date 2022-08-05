from typing import List

# 固定的base
def numeric(array: List[float]) -> None:
    '''
    原址排序：支持数值型数据，如整型与浮点型混合；不支持含有字符串类型元素的数据。
    '''
    if not array:
        return None
    arrmin = min(array)
    arrmax = max(array)
    length = len(array)
    capacity = int(arrmax - arrmin + 1) // length + 1
    bucket = [[] for _ in range(capacity)] # Construct buckets
    for value in array:
        bucket[int(value - arrmin) // length].append(value)
    array.clear()
    for index in bucket:
        if index:
            for value in sorted(index): # TimSort
                array.append(value)

# 基数越大，桶数越小
def mobase(array: List[float], base: int=5) -> None:
    '''
    原址排序：支持数值型数据，如整型与浮点型混合；不支持含有字符串类型元素的数据。
    base: 根据需要调节，base 越小，桶数越大。
    '''
    if not array:
        return None
    assert base > 0
    arrmin = min(array)
    arrmax = max(array)
    capacity = int(arrmax - arrmin + 1) // base + 1
    bucket = [[] for _ in range(capacity)]
    for value in array:
        bucket[int(value - arrmin) // base].append(value)
    array.clear()
    for index in bucket:
        if index:
            for value in sorted(index): # TimSort
                array.append(value)