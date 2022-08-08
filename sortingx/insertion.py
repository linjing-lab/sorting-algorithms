# 直接插入
def direct(array: list, reverse: bool=False) -> None:
    '''
    array: 支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    reverse: 是否降序, 默认采用升序。
    '''
    for index in range(1, len(array)):
        key = array[index]
        pre = index - 1
        while pre >= 0 and key > array[pre] if reverse else key < array[pre]:
            array[pre + 1] = array[pre]
            pre -= 1
        array[pre + 1] = key

# 折半插入
def binary(array: list, reverse: bool=False) -> None:
    '''
    array: 支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    reverse: 是否降序, 默认采用升序。
    '''
    for index in range(1, len(array)):
        key = array[index]
        low, high = 0, index - 1
        while low <= high: # 符合单调性的序列
            mid = (low + high) // 2
            if key < array[mid] if reverse else key > array[mid]:
                low = mid + 1
            else:
                high = mid - 1
        for pre in range(index, low, -1): # 从后往前
            array[pre] = array[pre - 1]
        array[low] = key