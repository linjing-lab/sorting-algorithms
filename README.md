# sorting-algorithms🎢

<div align="center">

|Algorithm||Time Complexity||Space Complexity|
|--|--|--|--|--|
|---|Best|Average|Worst|Worst|
|[Quicksort](./docs/Quicksort.md)|$\Omega(n \log(n))$|$\Theta(n \log(n))$|$O(n^2)$|$O(\log(n))$|
|[Mergesort](./docs/Mergesort.md)|$\Omega(n \log(n))$|$\Theta(n \log(n))$|$O(n \log(n))$|$O(n)$|
|Timsort|$\Omega(n)$|$\Theta(n \log(n))$|$O(n \log(n))$|$O(n)$|
|Heapsort|$\Omega(n \log(n))$|$\Theta(n \log(n))$|$O(n \log(n))$|$O(1)$|
|Bubble Sort|$\Omega(n)$|$\Theta(n^2)$|$O(n^2)$|$O(1)$|
|Insertion Sort|$\Omega(n)$|$\Theta(n^2)$|$O(n^2)$|$O(1)$|
|Selection Sort|$\Omega(n^2)$|$\Theta(n^2)$|$O(n^2)$|$O(1)$|
|Tree Sort|$\Omega(n \log(n))$|$\Theta(n \log(n))$|$O(n^2)$|$O(n)$|
|Shell Sort|$\Omega(n \log (n))$|$\Theta(n(\log (n))^2)$|$O(n(\log (n))^2)$|$O(1)$|
|Bucket Sort|$\Omega(n + k)$|$\Theta(n + k)$|$O(n^2)$|$O(n)$|
|Radix Sort|$\Omega(nk)$|$\Theta(nk)$|$O(nk)$|$O(n+k)$|
|Counting Sort|$\Omega(n + k)$|$\Theta(n + k)$|$O(n + k)$|$O(k)$|
|Cubesort|$\Omega(n)$|$\Theta(n \log(n))$|$O(n \log(n))$|$O(n)$|

</div>

## 归并排序（merge_sort)

`基本思想`：归并排序采用分治法，先递归拆分数组，再合并数组，一种非原地排序方法。

### 递归实现（Recursion）

```python
def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)

def merge(l, r):
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
```

### 非递归实现（Stack）

非递归版本不需要额外的空间。直接在原数组上进行切割合并。

```python
def merge(array, low, mid, high):
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

def merge_sort(array):
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
```

### 排序时间对比

```python
# 归并排序算法的对比
from collection.merge_sort import Recursion, Stack
def test_Mergesort(array):
    method_list = ["Recursion", "Stack"]
    dictionary = {}
    for method in method_list:
        function = eval(method)
        if method == "Recursion":
            times = time.time()
            function(array)
            timee = time.time()
        else:
            arr = copy.deepcopy(array) # 深度复制
            times = time.time()
            function(arr)
            timee = time.time()
        gap = round(timee - times, 2)
        gap_list = [gap]
        dictionary[method] = gap_list
    df = pl.DataFrame(dictionary)
    return df
print(test_Mergesort(data))
```

```textile
shape: (1, 2)
┌───────────┬───────┐
│ Recursion ┆ Stack │
│ ---       ┆ ---   │
│ f64       ┆ f64   │
╞═══════════╪═══════╡
│ 0.07      ┆ 0.07  │
└───────────┴───────┘
```

## LICENSE

[MIT LICENSE](./LICENSE)