# 插入排序（Insertion Sort）

## 一、基本思想

插入排序的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。插入排序在实现上，通常采用`in-place`排序（即只需用到O(1)的额外空间的排序），因而在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。

## 二、实现逻辑

有一组数字：`｛5, 2, 4, 6, 1, 3｝`，将这组数字从小到大进行排列。从第二个数字开始，将其认为是新增加的数字，第二个数字只需与其左边的第一个数字比较后排好序；在第三个数字，认为前两个已经排好序的数字为手里整理好的牌，那么只需将第三个数字与前两个数字比较即可；以此类推，直到最后一个数字与前面的所有数字比较结束，插入排序完成。

算法步骤：
1. 从第一个元素开始，该元素可以认为已经被排序；
2. 取出下一个元素，在已经排序的序列中从后向前扫描；
3. 如果已排序序列中的某元素大于新元素，则将该元素移到下一位置；
4. 重复步骤 3，直到找到已排序的元素小于或等于新元素的位置；
5. 将新元素**插入**到该位置；
6. 重复步骤 2 ~ 5。

## 三、时间复杂度的分析

如果插入排序的目标是把 $n$ 个元素的序列升序排序，那么：
- 若序列已经是升序排列，只需要比较 $n-1$ 次即可，即最好时间复杂度为：$\Omega(n)$；
- 若序列是降序排列，那么由于序列至多有 $n(n-1)/2$ 对逆序，即最坏时间复杂度为：$O(n^2)$。

对于平均时间复杂度而言，长度为 $n$ 的序列有 $n!$ 种排列，故每一种序列的排列平均有 $n(n-1)/4$ 对逆序，故有平均时间复杂度为：$\Theta(n^2)$。


## 四、空间复杂度的分析

由于算法采用的是`in-place`排序方法，不会额外开辟 $O(n)$ 的数组空间（`out-place`排序），所以空间复杂度为：$O(1)$。

## 五、算法实现

### 直接插入

```python
def insertion_sort(array: List, reverse: bool=False) -> None:
    '''
    支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    reverse: 是否降序, 默认采用升序。
    '''
    for index in range(1, len(array)):
        key = array[index]
        pre = index - 1
        while pre >= 0 and (key > array[pre] if reverse else key < array[pre]):
            array[pre + 1] = array[pre]
            pre -= 1
        array[pre + 1] = key
```

### 折半插入

```python
def insertion_sort(array: List, reverse: bool=False) -> None:
    '''
    支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    reverse: 是否降序, 默认采用升序。
    '''
    for index in range(1, len(array)):
        key = array[index]
        low, high = 0, index - 1
        while low <= high: # 符合单调性的序列
            mid = (low + high) // 2
            if (key < array[mid] if reverse else key > array[mid]):
                low = mid + 1
            else:
                high = mid - 1
        for pre in range(index, low, -1): # 从后往前
            array[pre] = array[pre - 1]
        array[low] = key
```