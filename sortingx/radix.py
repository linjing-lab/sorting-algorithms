from typing import List

# 按低位排序
def lsd(array: List[int], reverse: bool=False) -> List[int]:
    '''
    array: 支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    reverse: 是否降序, 默认采用升序。
    '''
    if not array:
        return array
    numbers = len(str(max(array))) # note the length of the biggest num
    for step in range(numbers):
        container = [[] for _ in range(10)] # 0~9
        for value in array:
            pos = value // (10 ** step) % 10
            container[9 - pos if reverse else pos].append(value) # 取个位
        array.clear()
        array = [value for index in container for value in index]
    return array

# 按高位排序
def msd(array: List[int], radix: int=6, reverse: bool=False) -> List[int]:
    '''
    array: 支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    radix: 基数大小, 最好取用最大数的位数。
    reverse: 是否降序, 默认采用升序。
    '''
    if not array or radix <= 0:
        return array
    container, num, k = [[] for _ in range(10)], [0] * 10, pow(10, radix - 1)
    for value in array:
        pos = value // k % 10
        container[pos].append(value)
        num[pos] += 1 # 计数器
    array.clear()
    for index in range(10):
        if num[index] == 1:
            array.append(container[index][0])
        elif num[index] > 1:
            con = msd(container[index], radix - 1)
            array.extend(con)
    if reverse:
        array.reverse()
    return array

a = [1, 2, 3, 4, 5, 6, 5]
print(msd(a, 6, reverse=True))