# 归并排序（Merge Sort)

## 一、基本思想

归并排序是一种稳定的排序方法。将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。

## 二、实现逻辑

对于一个待排序的数组，首先进行分解，将整个待排序数组以 $mid$ 中间位置为界，一分为二，随后接着分割，直至最小单位无法分割；开始进行“治”的操作，将每两个小部分进行排序，并逐步合并；直至合并成整个数组的大小。

算法步骤：

1. 将一个序列从中间位置分成两个序列；
2. 在将这两个子序列按照第一步继续二分下去；
3. 直到所有子序列的长度都为1，不可以再二分截止，再两两合并成一个有序序列。

## 三、时间复杂度的分析

## 四、空间复杂度的分析

## 五、算法实现

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