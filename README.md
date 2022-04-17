# 排序算法的实现与对比🎢
<div align="center">
    <img src="./images/排序算法对比.webp">
</div>

## 快速排序（Quicksort）

`基本思想`：本质上是一种分而治之的思想，原地排序。

1. 选定Pivot中心轴
2. 将大于Pivot的数字放在Pivot的右边
3. 将小于Pivot的数字放在Pivot的左边
4. 分别对左右子序列重复前三步操作，直到各子序列中的元素个数为1

### 一行实现

```python
quick_sort = lambda array: array if len(array) <= 1 else quick_sort([item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort([item for item in array[1:] if item > array[0]])
# quick_sort(data)
```

### 递归实现

```python
def quick_sort(array, l, r):
    if l < r:
        q = 
```
