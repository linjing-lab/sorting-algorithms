# 标准版本
def normal(array: list, run: int=32, reverse: bool=False) -> None:
    '''
    array: 支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    run: 运行大小, 默认是32, 最好是2的幂数。
    reverse: 是否降序, 默认采用升序。
    '''
    def inser(l: int, r: int) -> None:
        '''
        l: 数据左侧游标(整型), r: 数据右侧游标(整型)
        '''
        for index in range(l + 1, r + 1):
            key = array[index]
            pre = index - 1
            while pre >= l and (key > array[pre] if reverse else key < array[pre]):
                array[pre + 1] = array[pre]
                pre -= 1
            array[pre + 1] = key
    
    def merge(low: int, mid: int, high: int) -> None:
        '''
        low: 数据低侧游标(整型), mid: 数据中间游标(整型), high: 数据高侧游标(整型)
        '''
        left = array[low: mid]
        right = array[mid: high]
        i = 0
        j = 0
        result = []
        while i < len(left) and j < len(right):
            if (left[i] > right[j] if reverse else left[i] <= right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        array[low: high] = result
    
    # choose run
    length = len(array)
    for index in range(0, length, run):
        inser(index, min(index + run - 1, length - 1))

    # merge run
    size = run
    while size < length:
        for low in range(0, length, 2 * size):
            mid = low + size
            high = min(low + 2 * size - 1, length - 1) + 1
            merge(low, mid, high)
        size = 2 * size

# binary
def binary(array: list, run: int=32, reverse: bool=False) -> None:
    '''
    array: 支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    run: 运行大小, 默认是32, 最好是2的幂数。
    reverse: 是否降序, 默认采用升序。
    '''
    def inser(l: int, r: int) -> None:
        '''
        l: 数据左侧游标(整型), r: 数据右侧游标(整型)
        '''
        for index in range(l + 1, r + 1):
            key = array[index]
            low, high = l, index - 1
            while low <= high: # 符合单调性的序列
                mid = (low + high) // 2
                if (key < array[mid] if reverse else key > array[mid]):
                    low = mid + 1
                else:
                    high = mid - 1
            for pre in range(index, low, -1): # 从后往前
                array[pre] = array[pre - 1]
            array[low] = key
    
    def merge(low: int, mid: int, high: int) -> None:
        '''
        low: 数据低侧游标(整型), mid: 数据中间游标(整型), high: 数据高侧游标(整型)
        '''
        left = array[low: mid]
        right = array[mid: high]
        i = 0
        j = 0
        result = []
        while i < len(left) and j < len(right):
            if (left[i] > right[j] if reverse else left[i] <= right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        array[low: high] = result
    
    # choose run
    length = len(array)
    for index in range(0, length, run):
        inser(index, min(index + run - 1, length - 1))

    # merge run
    size = run
    while size < length:
        for low in range(0, length, 2 * size):
            mid = low + size
            high = min(low + 2 * size - 1, length - 1) + 1
            merge(low, mid, high)
        size = 2 * size