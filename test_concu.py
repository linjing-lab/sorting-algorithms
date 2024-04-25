from joblib import Parallel, delayed
from sortingx.sorting import Iterable, Callable, Optional, _T, SupportsRichComparison, List, generate, convert, verify

'''
Provide 2 cases about how to accelerate functions when define function to process the predefined buffers.
'''

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

data = [('Alex', 97, 90, 98, 95), ('Jack', 97, 88, 98, 92), ('Peter', 92, 95, 92, 96), ('Li', 97, 89, 98, 92)] # list
output = bubble(data, key=lambda x: x[1], reverse=True)