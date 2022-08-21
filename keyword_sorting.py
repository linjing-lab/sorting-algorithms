from utils import cmp

# choose flag version for its best performance.
def bubble_sort(array: list, key=None, reverse: bool=False) -> None:
    '''
    array: 同一数据维度下，支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    key: lambda函数, 仅含一个参量，用于关键字排序, 例如: key=lambda x: x[1], key=lambda x: (x[0], x[1])。
    reverse: 是否降序, 默认采用升序。
    '''
    compare = list(map(key, array)) if key != None else array
    compare = ([[value] for value in compare] if compare and compare[0] is not list else compare) if key != None else array
    for i in range(len(array) - 1): # loop to access each array element
        flag = False # 旗帜
        for j in range(len(array) - i - 1): # loop to compare array elements
        # compare two adjacent elements and change > to < to sort in descending order
            if (compare[j] < compare[j + 1] if reverse else compare[j] > compare[j + 1]) if not key else cmp(compare[j], compare[j + 1], reverse):
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
    compare = list(map(key, array)) if key != None else array
    compare = ([[value] for value in compare] if compare and compare[0] is not list else compare) if key != None else array
    for index in range(1, len(array)):
        keyc, keya = compare[index], array[index]
        low, high = 0, index - 1
        while low <= high: # 符合单调性的序列
            mid = (low + high) // 2
            if (keyc < compare[mid] if reverse else keyc > compare[mid]) if not keyc else cmp(keyc, compare[mid], reverse):
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