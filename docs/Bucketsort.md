# 桶排序（Bucket Sort）

## 一、基本思想

桶排序的工作原理是将数组分到有限数量的桶里。每个桶在个别排序，对于桶的排序可能是使用别的排序算法或是以递归的方式继续使用桶排序进行排序。最后依次把各个桶中的记录列出来得到有序序列。

## 二、实现逻辑

桶排序是一种分治思想，假设待排序的一组数均匀独立的分布在一个范围内，并将这一范围划分为几个字范围（桶），然后基于某种映射函数 $fun$，将待排序列的关键字 $value$ 映射到第 $i$ 个桶中（即桶数组 $Bucket$ 的下标 $i$），那么该关键字 $value$ 作为 $Bucket[i]$ 中的元素。每个桶 $Bucket[i]$ 都是一组大小为 $N/M$ 的序列。

将各个桶中的数据有序的合并起来，对每个桶 $Bucket[i]$ 中的所有元素进行比较排序，然后依次枚举输出 $Bucket[0]...Bucket[M]$ 中的全部内容即是一个有序序列。

为了使桶排序更加高效，首先在额外空间充足的情况下，尽量增大桶的数量，而且尽量使用能够将输入的 $N$ 个数据均匀的分配到 $K$ 个桶中的映射函数；对于桶中元素的排序，选择何种比较排序算法对于性能的影响至关重要。

算法步骤：
1. 设置一个定量的数组当作空桶；
2. 遍历序列：将元素放置在对应的桶中；
3. 对于每个非空桶进行内部排序；
4. 从每个非空桶中将元素依次返回原来序列。

## 三、时间复杂度的分析

## 四、空间复杂度的分析

## 五、算法实现

### 合理映射

```python
def bucket_sort(array: List[float]) -> None:
    '''
    支持数值型数据，如整型与浮点型混合；不支持含有字符串类型元素的数据。
    '''
    if not array:
        return None
    arrmin = min(array)
    arrmax = max(array)
    length = len(array)
    capacity = int(arrmax - arrmin + 1) // length + 1
    bucket = [[] for _ in range(capacity)] # Construct buckets
    for value in array:
        bucket[int(value - arrmin) // length].append(value)
    array.clear()
    for index in bucket:
        if index:
            for value in sorted(index): # TimSort
                array.append(value)
```

### 优化基数

```python
def bucket_sort(array: List[float], base: int=5) -> None:
    '''
    支持数值型数据，如整型与浮点型混合；不支持含有字符串类型元素的数据。
    base: 根据需要调节，base 越小，桶数越大。
    '''
    if not array:
        return None
    assert base > 0
    arrmin = min(array)
    arrmax = max(array)
    capacity = int(arrmax - arrmin + 1) // base + 1
    bucket = [[] for _ in range(capacity)]
    for value in array:
        bucket[int(value - arrmin) // base].append(value)
    array.clear()
    for index in bucket:
        if index:
            for value in sorted(index): # TimSort
                array.append(value)
```