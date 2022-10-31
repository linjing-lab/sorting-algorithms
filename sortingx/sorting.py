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

__all__ = ['bubble', 'insert', 'shell', 'heap', 'quick', 'merge']

from ._utils import core, generate
from ._typing import Iterable, Callable

def bubble(array: Iterable, key: Callable=None, reverse: bool=False) -> None:
    '''
    :param array: iterable data, support numeric data, such as mixing integer and floating point data; support all data of string type; mixing string and numeric types is not supported on the same column.
    :param key: callable function, for example: key=lambda x: x[1], key=lambda x: (x[0], x[1]).
    :param reverse: whether to use descending order. The default is ascending order.
    '''
    compare = generate(array, key)
    for i in range(len(array) - 1):
        flag = False # early stop by adding a bool value named flag
        for j in range(len(array) - i - 1):
            if core(compare[j], compare[j + 1], key, reverse):
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = True
                if key != None:
                    compare[j], compare[j + 1] = compare[j + 1], compare[j]
        if not flag:
            break

def insert(array: Iterable, key: Callable=None, reverse: bool=False) -> None:
    '''
    :param array: iterable data, support numeric data, such as mixing integer and floating point data; support all data of string type; mixing string and numeric types is not supported on the same column.
    :param key: callable function, for example: key=lambda x: x[1], key=lambda x: (x[0], x[1]).
    :param reverse: whether to use descending order. The default is ascending order.
    '''
    compare = generate(array, key)
    for index in range(1, len(array)):
        keyc, keya = compare[index], array[index]
        low, high = 0, index - 1
        while low <= high: # sequence conforming to monotonicity
            mid = (low + high) // 2
            if core(keyc, compare[mid], key, reverse):
                low = mid + 1
            else:
                high = mid - 1
        for pre in range(index, low, -1): # from back to front
            array[pre] = array[pre - 1]
            if key != None:
                compare[pre] = compare[pre - 1]
        array[low] = keya
        if key != None:
            compare[low] = keyc

def shell(array: Iterable, key: Callable=None, reverse: bool=False) -> None:
    '''
    :param array: iterable data, support numeric data, such as mixing integer and floating point data; support all data of string type; mixing string and numeric types is not supported on the same column.
    :param key: callable function, for example: key=lambda x: x[1], key=lambda x: (x[0], x[1]).
    :param reverse: whether to use descending order. The default is ascending order.
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

def heap(array: Iterable, key: Callable=None, reverse: bool=False) -> None:
    '''
    :param array: iterable data, support numeric data, such as mixing integer and floating point data; support all data of string type; mixing string and numeric types is not supported on the same column.
    :param key: callable function, for example: key=lambda x: x[1], key=lambda x: (x[0], x[1]).
    :param reverse: whether to use descending order. The default is ascending order.
    '''
    compare = generate(array, key)
    def build(root: int, end: int) -> None:
        '''
        Root: cursor indicating the root node (integer), end: cursor indicating the end of the array (integer)
        '''
        piv = root
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

def quick(array: Iterable, key: Callable=None, reverse: bool=False) -> None:
    '''
    :param array: iterable data, support numeric data, such as mixing integer and floating point data; support all data of string type; mixing string and numeric types is not supported on the same column.
    :param key: callable function, for example: key=lambda x: x[1], key=lambda x: (x[0], x[1]).
    :param reverse: whether to use descending order. The default is ascending order.
    '''
    compare = generate(array, key)
    def solve(l: int, r: int) -> None:
        '''
        main
        '''
        if l < r:
            mid = partition(l, r)
            solve(l, mid - 1)
            solve(mid + 1, r)

    def partition(l: int, r: int) -> int:
        '''
        l: The left cursor of array (integer), r: The right cursor of array (integer)
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
    solve(0, len(array)-1)

def merge(array: Iterable, key: Callable=None, reverse: bool=False) -> None:
    '''
    :param array: iterable data, support numeric data, such as mixing integer and floating point data; support all data of string type; mixing string and numeric types is not supported on the same column.
    :param key: callable function, for example: key=lambda x: x[1], key=lambda x: (x[0], x[1]).
    :param reverse: whether to use descending order. The default is ascending order.
    '''
    compare = generate(array, key)
    def merge(low: int, mid: int, high: int) -> None:
        '''
        low: The low-side cursor of array (integer), mid: The middle-side cursor of array (integer), high: The high-side cursor of array (integer)
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
        main
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