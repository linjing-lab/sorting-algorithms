from utils import core, generate

# choose flag version for its best performance.
def bubble_sort(array: list, key=None, reverse: bool=False) -> None:
    '''
    array: 同一数据维度下，支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    key: lambda函数, 仅含一个参量，用于关键字排序, 例如: key=lambda x: x[1], key=lambda x: (x[0], x[1])。
    reverse: 是否降序, 默认采用升序。
    '''
    compare = generate(array, key)
    for i in range(len(array) - 1): # loop to access each array element
        flag = False # 旗帜
        for j in range(len(array) - i - 1): # loop to compare array elements
        # compare two adjacent elements and change > to < to sort in descending order
            if core(compare[j], compare[j + 1], key, reverse):
                # swapping elements if elements are not in the intended order
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = True # 旗帜
                if key != None:
                    compare[j], compare[j + 1] = compare[j + 1], compare[j]
        if not flag:
            break

# choose binary version for its optimization.
def insertion_sort(array: list, key=None, reverse: bool=False) -> None:
    '''
    array: 支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    key: lambda函数, 仅含一个参量，用于关键字排序, 例如: key=lambda x: x[1], key=lambda x: (x[0], x[1])。
    reverse: 是否降序, 默认采用升序。
    '''
    compare = generate(array, key)
    for index in range(1, len(array)):
        keyc, keya = compare[index], array[index]
        low, high = 0, index - 1
        while low <= high: # 符合单调性的序列
            mid = (low + high) // 2
            if core(keyc, compare[mid], key, reverse):
                low = mid + 1
            else:
                high = mid - 1
        for pre in range(index, low, -1): # 从后往前
            array[pre] = array[pre - 1]
            if key != None:
                compare[pre] = compare[pre - 1]
        array[low] = keya
        if key != None:
            compare[low] = keyc

# choose knuth version for its smallest time.
def shell_sort(array: list, key=None, reverse: bool=False) -> None:
    '''
    array: 支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    key: lambda函数, 仅含一个参量，用于关键字排序, 例如: key=lambda x: x[1], key=lambda x: (x[0], x[1])。
    reverse: 是否降序, 默认采用升序。
    '''
    compare = generate(array, key)
    length = len(array)
    gap = 1
    while gap < length / 3:
        gap = int(3 * gap + 1)
    while gap >= 1:
        for index in range(gap, length):
            next = index
            while next >= gap and core(compare[next - gap], compare[next], key, reverse):
                array[next], array[next - gap] = array[next - gap], array[next]
                if key != None:
                    compare[next], compare[next - gap] = compare[next - gap], compare[next]
                next -= gap
        gap = int(gap / 3)