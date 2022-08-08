from typing import List

# while循环
def whilediv(array: List[int], reverse: bool=False) -> None:
    '''
    array: 仅支持全为整数类型的数据。
    reverse: 是否降序, 默认采用升序。
    '''
    if not array:
        return None
    arrmin = min(array)
    arrmax = max(array)
    count = [0] * (arrmax - arrmin + 1)
    for value in array:
        count[value - arrmin] += 1
    pos = len(array) - 1 if reverse else 0 # 游标
    for index in range(arrmin, arrmax + 1): # 从最小的数开始
        amount = count[index - arrmin]
        while amount >= 1:
            array[pos] = index
            amount -= 1
            pos = pos - 1 if reverse else pos + 1

# enumerate方法
def forenum(array: List[int], reverse: bool=False) -> None:
    '''
    array: 仅支持全为整数类型的数据。
    reverse: 是否降序, 默认采用升序。
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
            _ = array.insert(0, index + arrmin) if reverse else array.append(index + arrmin)

# 反向填充
def reverfill(array: List[int], reverse: bool=False) -> List[int]:
    '''
    仅支持全为整数类型的数据。
    reverse: 是否降序, 默认采用升序。
    '''
    if not array:
        return array
    arrmin = min(array)
    arrmax = max(array)
    length = len(array)
    count = [0] * (arrmax - arrmin + 1)
    result = [0] * length
    for value in array:
        count[value - arrmin] += 1
    for index in range(1, arrmax - arrmin + 1):
        count[index] += count[index - 1]
    for index in range(length - 1, -1, -1):
        result[length - count[array[index] - arrmin] if reverse else count[array[index] - arrmin] - 1] = array[index]
        count[array[index] - arrmin] -= 1
    return result