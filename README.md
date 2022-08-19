# sorting-algorithms🎢

常见数组排序算法的原理分析与代码实现。

Theory analysis and code implementation of common array sorting algorithms.

## How to Use

First, You need to click the [`fork`](https://github.com/linjing-lab/sorting-algorithms/fork) button to create your own sub repository, and use the following command to synchronize the repository to the local folder:

```git
git clone /path/to/repository 
```

For example, If I want to participate in the translation of [polars-book-cn](https://github.com/pola-rs/polars-book-cn), I use this command to carry out my work:

```git
git clone https://github.com/linjing-lab/polars-book-cn
```

Second, I have put different implemented versions of various sorting algorithms in the [`sortingx`](./sortingx/) folder, everyone can import it with the underlying command:

```python
import sortingx as sx
```

For example, If I use the `bubble` sorting algorithm to sort a real data set in reverse order, use the following commands:

```python
import random 
data = [random.randint(0, 100) for _ in range(10000)]
sx.bubble(data, reverse=False)
print(data)
```

Lastly, many algorithms are *in-place* sorting, and a few are *out-place*, you should pay attention to this point during the study, so that you can distinguish between `print(data)` and `print(method)`.

## Index Sheet

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

## LICENSE

[MIT LICENSE](./LICENSE)