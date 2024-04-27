# Copyright (c) 2024 linjing-lab

from joblib import Parallel, delayed
from sortingx.sorting import Iterable, Callable, Optional, _T, SupportsRichComparison, List, generate, convert, verify
import sortingx, random

'''
Provide all cases about how to accelerate functions when define function to process the predefined buffers.
'''

data = [[random.randint(0, 10), random.randint(0, 10)] for _ in range(10000)]

def bubble(__iterable: Iterable[_T], key: Optional[Callable[[_T], SupportsRichComparison]]=None, reverse: bool=False) -> List[_T]:
    '''
    :param __iterable: iterable data, mainly refers to `list`, `tuple`, `set`, `dict`, `str`, `zip`, `range`.
    :param key: callable function, for example: key=lambda x: x[1], key=lambda x: (x[0], x[1]), key=str.lower.
    :param reverse: whether to use descending order. The default is ascending order.

    :return: bubble's sorted result in a list.
    '''
    __iterable: List[_T] = convert(__iterable)
    compare: List[_T] = generate(__iterable, key)
    def acc(i: int):
        for j in range(length - i - 1):
            if (compare[j] < compare[j + 1] if reverse else compare[j] > compare[j+1]):
                __iterable[j], __iterable[j + 1] = __iterable[j + 1], __iterable[j]
                if key != None:
                    compare[j], compare[j + 1] = compare[j + 1], compare[j]
    if compare and not verify(compare):
        length: int = len(__iterable)
        Parallel(n_jobs=-1, backend="threading", prefer="threads")(delayed(acc)(i) for i in range(length - 1))
    return __iterable # miss break in "for i in range(length - 1)"

def insert(__iterable: Iterable[_T], key: Optional[Callable[[_T], SupportsRichComparison]]=None, reverse: bool=False) -> List[_T]:
    '''
    :param __iterable: iterable data, mainly refers to `list`, `tuple`, `set`, `dict`, `str`, `zip`, `range`.
    :param key: callable function, for example: key=lambda x: x[1], key=lambda x: (x[0], x[1]), key=str.lower.
    :param reverse: whether to use descending order. The default is ascending order.

    :return: insert's sorted result in a list.
    '''
    __iterable: List[_T] = convert(__iterable)
    compare: List[_T] = generate(__iterable, key)
    def acc(index: int):
        keyc: _T = compare[index]
        keya: _T = __iterable[index]
        low : int = 0
        high: int = index - 1
        while low <= high: # sequence conforming to monotonicity
            mid: int = (low + high) // 2
            if (keyc <= compare[mid] if reverse else keyc >= compare[mid]):
                low: int = mid + 1
            else:
                high: int = mid - 1
        for pre in range(index, low, -1): # from back to front
            __iterable[pre] = __iterable[pre - 1]
            if key != None:
                compare[pre] = compare[pre - 1]
        __iterable[low] = keya
        if key != None:
            compare[low] = keyc
    if compare and not verify(compare):
        length: int = len(__iterable)
        Parallel(n_jobs=-1, backend="threading", prefer="threads")(delayed(acc)(i) for i in range(1, length))
    return __iterable

def shell(__iterable: Iterable[_T], key: Optional[Callable[[_T], SupportsRichComparison]]=None, reverse: bool=False) -> List[_T]:
    '''
    :param __iterable: iterable data, mainly refers to `list`, `tuple`, `set`, `dict`, `str`, `zip`, `range`.
    :param key: callable function, for example: key=lambda x: x[1], key=lambda x: (x[0], x[1]), key=str.lower.
    :param reverse: whether to use descending order. The default is ascending order.

    :return: shell's sorted result in a list.
    '''
    __iterable: List[_T] = convert(__iterable)
    compare: List[_T] = generate(__iterable, key)
    if compare and not verify(compare):
        length: int = len(__iterable)
        gap: int = 1
        while gap < length / 3:
            gap: int = int(3 * gap + 1)
        def acc(index: int):
            next: int = index
            while next >= gap and (compare[next - gap] < compare[next] if reverse else compare[next - gap] > compare[next]):
                __iterable[next], __iterable[next - gap] = __iterable[next - gap], __iterable[next]
                if key != None:
                    compare[next], compare[next - gap] = compare[next - gap], compare[next]
                next -= gap
        while gap >= 1:
            Parallel(n_jobs=-1, backend="threading", prefer="threads")(delayed(acc)(i) for i in range(gap, length))
            gap: int = int(gap / 3)
    return __iterable

def heap(__iterable: Iterable[_T], key: Optional[Callable[[_T], SupportsRichComparison]]=None, reverse: bool=False) -> List[_T]:
    '''
    :param __iterable: iterable data, mainly refers to `list`, `tuple`, `set`, `dict`, `str`, `zip`, `range`.
    :param key: callable function, for example: key=lambda x: x[1], key=lambda x: (x[0], x[1]), key=str.lower.
    :param reverse: whether to use descending order. The default is ascending order.

    :return: heap's sorted result in a list.
    '''
    __iterable: List[_T] = convert(__iterable)
    compare: List[_T] = generate(__iterable, key)
    def build(root: int, end: int) -> None:
        '''
        :param root: cursor indicating the root node (int).
        :param end: cursor indicating the end of the __iterable (int).
        '''
        piv: int = root
        left: int = 2 * root + 1
        right: int = 2 * root + 2
        if left < end and (compare[left] < compare[root] if reverse else compare[left] > compare[root]):
            piv: int = left
        if right < end and (compare[right] < compare[piv] if reverse else compare[right] > compare[piv]):
            piv: int = right
        if piv != root:
            __iterable[root], __iterable[piv] = __iterable[piv], __iterable[root]
            if key != None:
                compare[root], compare[piv] = compare[piv], compare[root]
            build(piv, end)
    if compare and not verify(compare):
        length: int = len(__iterable)
        def acc(end: int):
            if compare[0] != compare[end]:
                __iterable[0], __iterable[end] = __iterable[end], __iterable[0]
                if key != None:
                    compare[0], compare[end] = compare[end], compare[0]
            build(0, end)
        Parallel(n_jobs=-1, backend="threading", prefer="threads")(delayed(build)(root, length) for root in range(length // 2 - 1 , -1, -1))
        Parallel(n_jobs=-1, backend="threading", prefer="threads")(delayed(acc)(end) for end in range(length - 1, 0, -1))
    return __iterable

def merge(__iterable: Iterable[_T], key: Optional[Callable[[_T], SupportsRichComparison]]=None, reverse: bool=False) -> List[_T]:
    '''
    :param __iterable: iterable data, mainly refers to `list`, `tuple`, `set`, `dict`, `str`, `zip`, `range`.
    :param key: callable function, for example: key=lambda x: x[1], key=lambda x: (x[0], x[1]), key=str.lower.
    :param reverse: whether to use descending order. The default is ascending order.

    :return: merge's sorted result in a list.
    '''
    __iterable: List[_T] = convert(__iterable)
    compare: List[_T] = generate(__iterable, key)
    def merg(low: int, mid: int, high: int) -> None:
        '''
        :param low: The low cursor of __iterable (int).
        :param mid: The middle cursor of __iterable (int).
        :param high: The high cursor of __iterable (int).
        '''
        left: List[_T] = __iterable[low: mid]
        lnl: int = len(left)
        lc: List[_T] = compare[low: mid]
        right: List[_T] = __iterable[mid: high]
        lnr: int = len(right)
        rc: List[_T] = compare[mid: high]
        i: int = 0
        j: int = 0
        result: List[_T] = []
        store: List[_T] = []
        while i < lnl and j < lnr:
            if (rc[j] <= lc[i] if reverse else rc[j] >= lc[i]):
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
        __iterable[low: high]: List[_T] = result
        compare[low: high]: List[_T] = store

    def solve() -> None:
        '''
        main
        '''
        i: int = 1
        length: int = len(__iterable)
        def acc(low: int):
            mid: int = low + i
            high: int = min(low + 2 * i, length)
            if mid < high:
                merg(low, mid, high)
        while i < length:
            low: int = 0
            Parallel(n_jobs=-1, backend="threading", prefer="threads")(delayed(acc)(low) for low in range(low, length, 2*i))
            i *= 2
    if compare and not verify(compare):
        solve()
    return __iterable

def quick_test():
    quick_data = [data for _ in range(7)]
    Parallel(n_jobs=-1, backend="loky", prefer="processes")(delayed(sortingx.quick)(data, lambda x: x[1], True) for data in quick_data)

def other_test():
    # data = [('Alex', 97, 90, 98, 95), ('Jack', 97, 88, 98, 92), ('Peter', 92, 95, 92, 96), ('Li', 97, 89, 98, 92), ('IO', 98, 92, 93, 91), ('IY', 98, 92, 90, 91), ('OP', 97, 92, 90, 91), ('YT', 97, 92, 93, 90)] # list
    output = merge(data, lambda x: x[1], reverse=True)
    print(output)

quick_test()
# other_test()