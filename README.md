# 排序算法的实现与对比🎢
<div align="center">
    <img src="./images/排序算法对比.webp" width="50%">
</div>

## 快速排序（Quicksort）

`基本思想`：本质上是一种分而治之的思想，原地排序。

1. 选定Pivot中心轴
2. 将大于Pivot的数字放在Pivot的右边
3. 将小于Pivot的数字放在Pivot的左边
4. 分别对左右子序列重复前三步操作，直到各子序列中的元素个数为1

### 一行实现（Lambda）

```python
quick_sort = lambda array: array if len(array) <= 1 else quick_sort([item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort([item for item in array[1:] if item > array[0]])
```

### 递归实现（Recursion）

```python
def quick_sort(array, l, r):
    if l < r:
        mid = partition(array, l, r)
        quick_sort(array, l, mid - 1)
        quick_sort(array, mid + 1, r)

def partition(array, l, r):
    value = array[r]
    index = l - 1
    for ind in range(l, r):
        if array[ind] <= value:
            index += 1
            array[index], array[j] = array[j], array[index]
    array[index + 1], array[r] = array[r], array[index + 1]
    return index + 1
```

## 非递归实现（Stack）

```python
def quick_sort(array, l, r):
    if l >= r:
        return
    stack = []
    stack.append(l)
    stack.append(r)
    while stack:
        low = stack.pop(0)
        high = stack.pop(0)
        if high - low <= 0:
            continue
        value = array[high]
        index = low - 1
        for ind in range(low, high):
            if array[ind] <= value:
                index += 1
                array[index], array[j] = array[j], array[index]
        array[index + 1], array[high] = array[high], array[index + 1]
        stack.extend([low, index, index+2, high])
```

## 快速排序实现算法的对比
```python
from galley.quick_sort import Lambda, Recursion, Stack
def test_Quicksort(array, l=0, r=9999):
    method_list = ["Lambda", "Recursion", "Stack"]
    dictionary = {}
    for method in method_list:
        times = time.time()
        function = eval(method)
        arr = copy.deepcopy(array)
        if method == "Lambda":
            function(arr) # 深度复制
        else:
            function(arr, l, r)
        timee = time.time()
        gap = round(timee - times, 2)
        gap_list = [gap]
        dictionary[method] = gap_list
    df = pl.DataFrame(dictionary)
    return df
print(test_Quicksort(data))
```
```textile
shape: (1, 3)
┌────────┬───────────┬───────┐
│ Lambda ┆ Recursion ┆ Stack │
│ ---    ┆ ---       ┆ ---   │
│ f64    ┆ f64       ┆ f64   │
╞════════╪═══════════╪═══════╡
│ 0.11   ┆ 0.15      ┆ 0.16  │
└────────┴───────────┴───────┘
```