from typing import List

# 递归实现
def recur(array: List) -> List:
    '''
    非原址排序：支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    '''
    def merge_sort(array: List) -> List:
        if len(array) <= 1:
            return array
        mid = len(array) // 2
        left = merge_sort(array[:mid])
        right = merge_sort(array[mid:])
        return merge(left, right)

    def merge(l: int, r: int) -> List:
        '''
        l: 数据左侧游标(整型), r: 数据右侧游标(整型)
        '''
        result = []
        i = 0
        j = 0
        while i < len(l) and j < len(r):
            if(l[i] <= r[j]):
                result.append(l[i])
                i += 1
            else:
                result.append(r[j])
                j += 1
        result += l[i:]
        result += r[j:]
        return result
    return merge_sort(array)

# 非递归实现
def stack(array: List) -> None:
    '''
    原址排序：支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    '''
    def merge(array: List, low: int, mid: int, high: int) -> None:
        '''
        low: 数据低侧游标(整型), mid: 数据中间游标(整型), high: 数据高侧游标(整型)
        '''
        left = array[low: mid]
        right = array[mid: high]
        i = 0
        j = 0
        result = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        array[low: high] = result

    def merge_sort(array: List) -> None:
        i = 1
        while i < len(array):
            low = 0
            while low < len(array):
                mid = low + i
                high = min(low + 2 * i, len(array))
                if mid < high:
                    merge(array, low, mid, high)
                low += 2 * i
            i *= 2
    merge_sort(array)