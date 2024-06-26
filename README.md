# sorting-algorithms🎢

Theory analysis and code implementation of common array sorting algorithms.

## 📍 start from galley

First, You need to click the [`fork`](https://github.com/linjing-lab/sorting-algorithms/fork) button to create your own sub repository, or use the following command to synchronize the repository to the local folder:

```git
git clone https://github.com/linjing-lab/sorting-algorithms.git
```

Second, I have put different implemented versions of various sorting algorithms in the [`galley`](./docs/galley/) folder, everyone can import it with the underlying command:

```python
import galley as ge
```

For example, If I use the `bubble` sorting algorithm to sort a real data in reverse, use the following commands:

```python
import random 
data = [random.randint(0, 100) for _ in range(10000)]
ge.bubble.flag(data, reverse=True)
print(data)
```

Lastly, many algorithms are *in-place* sorting, and a few are *out-place*, you should pay attention to it during the study, so that you can distinguish between `print(data)` and `print(method)`. I mainly use `if... else...` to implement the reverse order of sorting algorithms in gallery and the partition of some algorithms.

## 📊 sorting complexity

<div align="center">

|Algorithm||Time Complexity||Space Complexity|
|--|--|--|--|--|
|---|Best|Average|Worst|Worst|
|[Quicksort](./docs/Quicksort.md)|$\Omega(n \log(n))$|$\Theta(n \log(n))$|$O(n^2)$|$O(\log(n))$|
|[Mergesort](./docs/Mergesort.md)|$\Omega(n \log(n))$|$\Theta(n \log(n))$|$O(n \log(n))$|$O(n)$|
|[Timsort](./docs/Timsort.md)|$\Omega(n)$|$\Theta(n \log(n))$|$O(n \log(n))$|$O(n)$|
|[Heapsort](./docs/Heapsort.md)|$\Omega(n \log(n))$|$\Theta(n \log(n))$|$O(n \log(n))$|$O(1)$|
|[Bubble Sort](./docs/Bubblesort.md)|$\Omega(n)$|$\Theta(n^2)$|$O(n^2)$|$O(1)$|
|[Insertion Sort](./docs/Insertionsort.md)|$\Omega(n)$|$\Theta(n^2)$|$O(n^2)$|$O(1)$|
|[Selection Sort](./docs/Selectionsort.md)|$\Omega(n^2)$|$\Theta(n^2)$|$O(n^2)$|$O(1)$|
|[Tree Sort](./docs/Treesort.md)|$\Omega(n \log(n))$|$\Theta(n \log(n))$|$O(n^2)$|$O(n)$|
|[Shell Sort](./docs/Shellsort.md)|$\Omega(n \log (n))$|$\Theta(n(\log (n))^2)$|$O(n(\log (n))^2)$|$O(1)$|
|[Bucket Sort](./docs/Bucketsort.md)|$\Omega(n + k)$|$\Theta(n + k)$|$O(n^2)$|$O(n)$|
|[Radix Sort](./docs/Radixsort.md)|$\Omega(nk)$|$\Theta(nk)$|$O(nk)$|$O(n+k)$|
|[Counting Sort](./docs/Countingsort.md)|$\Omega(n + k)$|$\Theta(n + k)$|$O(n + k)$|$O(k)$|
|Cubesort|$\Omega(n)$|$\Theta(n \log(n))$|$O(n \log(n))$|$O(n)$|

</div>

## 🙋 test description

I test the performance of the sorting algorithm after adding the [*keyword*](./keyword_sorting.py) sorting in the [*test_key*](./test_key.py) file (The [*utils*](./utils.py) file stores the most core function for keyword sorting), test the time accumulation of the sorting algorithm with respect to the large data set in the [*test_time*](./test_time.py) file, and test whether the reverse parameter of the sorting algorithms is designed correctly in the [*test_reverse*](./test_reverse.py) file, including the robustness of these.

The design of reverse sorting of all methods is completely correct, and the design of keyword sorting is feasible, which is consistent with the usage of *sorted* parameter officially released by Python.

The example of keyword sorting are underlying:

```python
data = [('Alex', 100, 90, 98, 95), ('Jack', 97, 88, 98, 92), ('Peter', 92, 95, 92, 96), ('Li', 97, 89, 98, 92)]
insertion_sort(data, key=lambda x: (x[1], x[2]), reverse=False)
# sorted(data, key=lambda x: (x[1], x[2]), reverse=False)
print(data)

'''
reverse=False: 
[('Peter', 92, 95, 92, 96), ('Jack', 97, 88, 98, 92), ('Li', 97, 89, 98, 92), ('Alex', 100, 90, 98, 95)]

reverse=True: 
[('Alex', 100, 90, 98, 95), ('Li', 97, 89, 98, 92), ('Jack', 97, 88, 98, 92), ('Peter', 92, 95, 92, 96)]
'''
```

you can see more 5 methods in [*keyword_sorting*](./keyword_sorting.py) file.

## 🎒 pip install

As you can see, I create a core function to drive keyword sorting just by opening up an array with the size of k (k = nums of keyword), and the type of sorting implemented by Python officially released is Timsort, which is more complicated than the other algorithms in my released packages in the future.

```python
!pip install sortingx # in jupyter
pip install sortingx # in cmd
```
sortingx can do whatever `list.sort()` do, and support more methods and more data types.

explain:
- [sortingx-1.1.0](https://github.com/linjing-lab/sorting-algorithms/tree/v1.1.0) is the first version aligned with the `list.sort()` usage method.
- [sortingx-1.1.1](https://github.com/linjing-lab/sorting-algorithms/tree/v1.1.1) is the first stable version accelerated with typing_extensions.
- [sortingx-1.1.2](https://github.com/linjing-lab/sorting-algorithms/tree/v1.1.2) is the first stable version that has a return value and extends the iterable data types.
- [sortingx-1.1.3](https://github.com/linjing-lab/sorting-algorithms/tree/v1.1.3) is the version that complete the typing of local variables and align with `sorted()` usage method.
- [sortingx-1.2.0](https://github.com/linjing-lab/sorting-algorithms/tree/v1.2.0) is the end version of sorting series, which optimize the kernel of generate.
- [sortingx-1.2.1](https://github.com/linjing-lab/sorting-algorithms/tree/v1.2.1) is the portable version that comparison is faster than ever, the generate is more portable.

By the way, I didn't complete all the iterative data types, in order to develop a more targeted scenario. If you are **interested** in other iterative data types, please add them in the `convert` function of the `_utils.py` file, for example: bytes, bytearray, range, zip. If you need to deal with `dict_keys`, `dict_values`, `dict_items`, please use `list()` to convert the variables of these data types before using any method of sortingx.

- [sortingx-1.2.2](https://github.com/linjing-lab/sorting-algorithms/tree/v1.2.2) is the package that support `range`, `zip`, `dict_keys`, `dict_values`, `dict_items` additionally, you can choose what suitable data you want to input.
- [sortingx-1.2.3](https://github.com/linjing-lab/sorting-algorithms/tree/v1.2.3) is the package that corrected the situation where elements are equal in `compare`, support more input data, like data as `[['Jack', (98, 100)], ['Bob', (98, 99)], ['Jessi', (98, 97)]]` and key as `lambda x: x[1][0]`.
- [sortingx-1.3.0](https://github.com/linjing-lab/sorting-algorithms/tree/v1.3.0) is the final version that fully aligned with the `sorted`', reduces redundant data exchanging. like data as `[('Alex', 97, 90, 98, 95), ('Jack', 97, 88, 98, 92), ('Peter', 92, 95, 92, 96), ('Li', 97, 89, 98, 92)]` and key as `key=lambda x: x[1]`.
- [sortingx-1.3.1](https://github.com/linjing-lab/sorting-algorithms/tree/v1.3.1) is the improved version from v1.3.0, and pre-operations from `_utils` are more conise to reduce shallow copy in Runtime.
- [sortingx-1.3.2](https://github.com/linjing-lab/sorting-algorithms/tree/v1.3.2) is the optimized version from v1.3.1, and shrink the returns of calling intrinsic function named `__len__` to get length of `__iterable`.

refer to [this](./README_release.md) for downloaded info.

## LICENSE

[Apache 2.0](./LICENSE)