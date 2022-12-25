# Copyright 2022 linjing-lab
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ._utils import core, generate, convert
from ._typing import Iterable, Callable, Optional, _T, SupportsRichComparison, List

def bubble(__iterable: Iterable[_T], key: Optional[Callable[[_T], SupportsRichComparison]]=None, reverse: bool=False) -> List[_T]:
    '''
    :param __iterable: iterable data.
    :param key: callable function, for example: key=lambda x: x[1], key=lambda x: (x[0], x[1]).
    :param reverse: whether to use descending order. The default is ascending order.
    '''
    __iterable: List[_T] = convert(__iterable)
    compare: List[_T] = generate(__iterable, key)
    for i in range(len(__iterable) - 1):
        flag: bool = False # early stop by adding a bool value named flag
        for j in range(len(__iterable) - i - 1):
            if core(compare[j], compare[j + 1], key, reverse):
                __iterable[j], __iterable[j + 1] = __iterable[j + 1], __iterable[j]
                flag: bool = True
                if key != None:
                    compare[j], compare[j + 1] = compare[j + 1], compare[j]
        if not flag:
            break
    return __iterable

def insert(__iterable: Iterable[_T], key: Optional[Callable[[_T], SupportsRichComparison]]=None, reverse: bool=False) -> List[_T]:
    '''
    :param __iterable: iterable data.
    :param key: callable function, for example: key=lambda x: x[1], key=lambda x: (x[0], x[1]).
    :param reverse: whether to use descending order. The default is ascending order.
    '''
    __iterable: List[_T] = convert(__iterable)
    compare: List[_T] = generate(__iterable, key)
    for index in range(1, len(__iterable)):
        keyc: _T = compare[index]
        keya: _T = __iterable[index]
        low : int = 0
        high: int = index - 1
        while low <= high: # sequence conforming to monotonicity
            mid: int = (low + high) // 2
            if core(keyc, compare[mid], key, reverse):
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
    return __iterable

def shell(__iterable: Iterable[_T], key: Optional[Callable[[_T], SupportsRichComparison]]=None, reverse: bool=False) -> List[_T]:
    '''
    :param __iterable: iterable data.
    :param key: callable function, for example: key=lambda x: x[1], key=lambda x: (x[0], x[1]).
    :param reverse: whether to use descending order. The default is ascending order.
    '''
    __iterable: List[_T] = convert(__iterable)
    compare: List[_T] = generate(__iterable, key)
    length: int = len(__iterable)
    gap: int = 1
    while gap < length / 3:
        gap: int = int(3 * gap + 1)
    while gap >= 1:
        for index in range(gap, length):
            next: int = index
            while next >= gap and core(compare[next - gap], compare[next], key, reverse):
                __iterable[next], __iterable[next - gap] = __iterable[next - gap], __iterable[next]
                if key != None:
                    compare[next], compare[next - gap] = compare[next - gap], compare[next]
                next -= gap
        gap: int = int(gap / 3)
    return __iterable
    
def heap(__iterable: Iterable[_T], key: Optional[Callable[[_T], SupportsRichComparison]]=None, reverse: bool=False) -> List[_T]:
    '''
    :param __iterable: iterable data.
    :param key: callable function, for example: key=lambda x: x[1], key=lambda x: (x[0], x[1]).
    :param reverse: whether to use descending order. The default is ascending order.
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
        if left < end and core(compare[left], compare[root], key, reverse):
            piv: int = left
        if right < end and core(compare[right], compare[piv], key, reverse):
            piv: int = right
        if piv != root:
            __iterable[root], __iterable[piv] = __iterable[piv], __iterable[root]
            if key != None:
                compare[root], compare[piv] = compare[piv], compare[root]
            build(piv, end)
    
    length: int = len(__iterable)
    for root in range(length // 2 - 1 , -1, -1):
        build(root, length)
    for end in range(length - 1, 0, -1):
        __iterable[0], __iterable[end] = __iterable[end], __iterable[0]
        if key != None:
            compare[0], compare[end] = compare[end], compare[0]
        build(0, end)
    return __iterable

def quick(__iterable: Iterable[_T], key: Optional[Callable[[_T], SupportsRichComparison]]=None, reverse: bool=False) -> List[_T]:
    '''
    :param __iterable: iterable data.
    :param key: callable function, for example: key=lambda x: x[1], key=lambda x: (x[0], x[1]).
    :param reverse: whether to use descending order. The default is ascending order.
    '''
    __iterable: List[_T] = convert(__iterable)
    compare: List[_T] = generate(__iterable, key)
    def solve(l: int, r: int) -> None:
        '''
        main
        '''
        if l < r:
            mid: int = partition(l, r)
            solve(l, mid - 1)
            solve(mid + 1, r)

    def partition(l: int, r: int) -> int:
        '''
        :param l: The left cursor of __iterable (int).
        :param r: The right cursor of __iterable (int).
        '''
        val: _T = compare[r]
        index: int = l - 1
        for ind in range(l, r):
            if core(val, compare[ind], key, reverse):
                index += 1
                __iterable[index], __iterable[ind] = __iterable[ind], __iterable[index]
                if key != None:
                    compare[index], compare[ind] = compare[ind], compare[index]
        __iterable[index + 1], __iterable[r] = __iterable[r], __iterable[index + 1]
        if key != None:
            compare[index + 1], compare[r] = compare[r], compare[index + 1]
        return index + 1
    solve(0, len(__iterable) - 1)
    return __iterable

def merge(__iterable: Iterable[_T], key: Optional[Callable[[_T], SupportsRichComparison]]=None, reverse: bool=False) -> List[_T]:
    '''
    :param __iterable: iterable data.
    :param key: callable function, for example: key=lambda x: x[1], key=lambda x: (x[0], x[1]).
    :param reverse: whether to use descending order. The default is ascending order.
    '''
    __iterable: List[_T] = convert(__iterable)
    compare: List[_T] = generate(__iterable, key)
    def merg(low: int, mid: int, high: int) -> None:
        '''
        :param low: The low-side cursor of __iterable (int).
        :param mid: The middle-side cursor of __iterable (int).
        :param high: The high-side cursor of __iterable (int).
        '''
        left: List[_T] = __iterable[low: mid]
        lc: List[_T] = compare[low: mid]
        right: List[_T] = __iterable[mid: high]
        rc: List[_T] = compare[mid: high]
        i: int = 0
        j: int = 0
        result: List[_T] = []
        store: List[_T] = []
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
        __iterable[low: high]: List[_T] = result
        compare[low: high]: List[_T] = store

    def solve() -> None:
        '''
        main
        '''
        i: int = 1
        while i < len(__iterable):
            low: int = 0
            while low < len(__iterable):
                mid: int = low + i
                high: int = min(low + 2 * i, len(__iterable))
                if mid < high:
                    merg(low, mid, high)
                low += 2 * i
            i *= 2
    solve()
    return __iterable

__all__ = [bubble, insert, shell, heap, quick, merge]