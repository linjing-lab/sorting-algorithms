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

# choose recursion version for its best performance.
def heap_sort(array: list, key=None, reverse: bool=False) -> None:
    '''
    array: 支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    key: lambda函数, 仅含一个参量，用于关键字排序, 例如: key=lambda x: x[1], key=lambda x: (x[0], x[1])。
    reverse: 是否降序, 默认采用升序。
    '''
    compare = generate(array, key)
    def build(root: int, end: int) -> None:
        '''
        root: 指示根节点的游标(整型), end: 指示数组末尾的游标(整型)
        '''
        piv = root # 根据reverse
        left = 2 * root + 1
        right = 2 * root + 2
        if left < end and core(compare[left], compare[root], key, reverse):
            piv = left
        if right < end and core(compare[right], compare[piv], key, reverse):
            piv = right
        if piv != root:
            array[root], array[piv] = array[piv], array[root]
            if key != None:
                compare[root], compare[piv] = compare[piv], compare[root]
            build(piv, end)
    
    length = len(array)
    for root in range(length // 2 - 1 , -1, -1):
        build(root, length)
    for end in range(length - 1, 0, -1):
        array[0], array[end] = array[end], array[0]
        if key != None:
            compare[0], compare[end] = compare[end], compare[0]
        build(0, end)

# choose recursion version for its best performance.
def quick_sort(array: list, l: int, r: int, key=None, reverse: bool=False) -> None:
    '''
    array: 支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    l: 数据左侧游标(整型), r: 数据右侧游标(整型)
    key: lambda函数, 仅含一个参量，用于关键字排序, 例如: key=lambda x: x[1], key=lambda x: (x[0], x[1])。
    reverse: 是否降序, 默认采用升序。
    '''
    compare = generate(array, key)
    if l >= r:
        return None
    def solve(l: int, r: int) -> None:
        '''
        算法主体
        '''
        if l < r:
            mid = partition(l, r)
            solve(l, mid - 1)
            solve(mid + 1, r)

    def partition(l: int, r: int) -> int:
        '''
        array: 数据(列表), l: 数据左侧游标(整型), r: 数据右侧游标(整型)
        '''
        val = compare[r]
        index = l - 1
        for ind in range(l, r):
            if core(val, compare[ind], key, reverse):
                index += 1
                array[index], array[ind] = array[ind], array[index]
                if key != None:
                    compare[index], compare[ind] = compare[ind], compare[index]
        array[index + 1], array[r] = array[r], array[index + 1]
        if key != None:
            compare[index + 1], compare[r] = compare[r], compare[index + 1]
        return index + 1
    solve(l, r)

# choose stack version for its smallest time.
def merge_sort(array: list, key=None, reverse: bool=False) -> None:
    '''
    array: 支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    key: lambda函数, 仅含一个参量，用于关键字排序, 例如: key=lambda x: x[1], key=lambda x: (x[0], x[1])。
    reverse: 是否降序, 默认采用升序。
    '''
    compare = generate(array, key)
    def merge(low: int, mid: int, high: int) -> None:
        '''
        low: 数据低侧游标(整型), mid: 数据中间游标(整型), high: 数据高侧游标(整型)
        '''
        left, lc = array[low: mid], compare[low: mid]
        right, rc = array[mid: high], compare[mid: high]
        i = 0
        j = 0
        result, store = [], []
        while i < len(left) and j < len(right):
            if core(rc[j], lc[i], key, reverse):
                result.append(left[i])
                store.append(lc[i])
                i += 1
            else:
                result.append(right[j])
                store.append(rc[j])
                j += 1
        result += left[i:]
        store += lc[i:]
        result += right[j:]
        store += rc[j:]
        array[low: high] = result
        compare[low: high] = store

    def solve() -> None:
        '''
        算法主体
        '''
        i = 1
        while i < len(array):
            low = 0
            while low < len(array):
                mid = low + i
                high = min(low + 2 * i, len(array))
                if mid < high:
                    merge(low, mid, high)
                low += 2 * i
            i *= 2
    solve()