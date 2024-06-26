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

归并排序的时间复杂度是 $O(n \log_2(n))$，则这个时间复杂度是稳定的，不随需要排序的序列的不同而产生波动。假设我们需要对一个包含 $n$ 个数的序列使用归并排序，并且使用的是递归的实现方式，那么过程如下：

- 递归的第一层，将 $n$ 个数划分为 $2$ 个子区间，每个子区间的数字个数为 $n/2$；
- 递归的第二层，将 $n$ 个数划分为 $4$ 个子区间，每个子区间的数字个数为 $n/4$；
- 递归的第三层，将 $n$ 个数划分为 $8$ 个区间，每个子区间的数字个数为 $n/8$；
- ......
- 递归的第 $\log_2(n)$ 层，将 $n$ 个数划分为 $n$ 个子区间，每个子区间的数字个数为1；

归并排序的过程中，需要对当前区间进行对半划分，直到区间的长度为1。也就是说，每一层的子区间，长度都是上一层的 $1/2$。这也就意味着，当划分到第 $\log_2(n)$的时候，子区间的长度就是1了。而归并的“治”操作，则是从最底层开始（子区间为1的层），对相邻的两个子区间进行合并，过程如下：

- 在第 $\log_2(n)$ 层（最底层），每个子区间的长度为1，共 $n$ 个子区间，每相邻两个子区间进行合并，总共合并 $n/2$次。$n$ 个数字都会被遍历一遍，所以这一层的总时间复杂度为 $O(n)$；
- ......
- 在第二层，每个子区间长度为 $n/4$，总共有 $4$ 子区间，每相邻两个子区间进行合并，总共合并 $2$ 次。$n$ 个数字都会被遍历一次，所以这一层的总时间复杂度为 $O(n)$；
- 在第一层，每个子区间长度为 $n/2$，总共有 $2$ 个子区间，只需要合并一次。$n$ 个数字都会被遍历一次，所以这一层的总时间复杂度为 $O(n)$；

通过上面的操作可以发现，对于每一层来说，在合并所有子区间的过程中，$n$ 个元素都会被操作一次，所以每一层的时间复杂度都是 $O(n)$。归并排序化分子区间，将子区间划分为只剩 $1$ 个元素，需要化分 $\log_2(n)$ 次。每一层的时间复杂度为 $O(n)$，共有 $\log_2(n)$ 层，所以归并排序的时间复杂度是 $\Omega(n \log_2(n))$、$\Theta(n \log_2(n))$、$O(n \log_2(n))$。

## 四、空间复杂度的分析

这是因为归并排序的合并函数，在合并两个有序数组为一个有序数组时，需要借助额外的存储空间。如果我们继续按照分析递归时间复杂度的方法，通过递推公式来求解，那整个归并过程需要的空间复杂度就是 $O(n \log_2(n))$。实际上，递归代码的空间复杂度并不能像时间复杂度那样累加。最重要的一点，尽管每次合并操作都需要申请额外的内存空间，但在合并完成之后，临时开辟的内存空间就被释放掉了。在任意时刻，CPU 只会有一个函数在执行，也就只会有一个临时的内存空间在使用。临时内存空间最大也不会超过 $n$ 个数据的大小，所以空间复杂度是 $O(n)$。

## 五、算法实现

### 递归实现

```python
def merge_sort(array: list, reverse: bool=False) -> list:
    '''
    array: 支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    reverse: 是否降序, 默认采用升序。
    '''
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right, reverse=reverse)

def merge(l: int, r: int, reverse: bool=False) -> list:
    '''
    l: 数据左侧游标(整型), r: 数据右侧游标(整型)
    '''
    result = []
    i = 0
    j = 0
    while i < len(l) and j < len(r):
        if (l[i] > r[j] if reverse else l[i] <= r[j]):
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
    result += l[i:]
    result += r[j:]
    return result
```

### 非递归实现

```python
def merge(array: list, low: int, mid: int, high: int, reverse: bool=False) -> None:
    '''
    low: 数据低侧游标(整型), mid: 数据中间游标(整型), high: 数据高侧游标(整型)
    '''
    left = array[low: mid]
    right = array[mid: high]
    i = 0
    j = 0
    result = []
    while i < len(left) and j < len(right):
        if (left[i] > right[j] if reverse else left[i] <= right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    array[low: high] = result

def merge_sort(array: list, reverse: bool=False) -> None:
    '''
    array: 支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    reverse: 是否降序, 默认采用升序。
    '''
    i = 1
    while i < len(array):
        low = 0
        while low < len(array):
            mid = low + i
            high = min(low + 2 * i, len(array))
            if mid < high:
                merge(array, low, mid, high, reverse=reverse)
            low += 2 * i
        i *= 2
```