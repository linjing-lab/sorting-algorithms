# 树形排序（Tree Sort）

## 一、基本思想

树排序是一种在线排序算法。它使用二叉搜索树数据结构来存储元素。通过按顺序遍历二叉搜索树，可以按排序顺序检索元素。由于它是一种在线排序算法，因此插入的元素始终按排序顺序进行维护。

## 二、实现逻辑

假设使用一组未排序的数组 `array` 包含 `n` 个元素。

算法主体的步骤：
1. 通过在二叉搜索树中插入数组中的元素来构建二进制搜索树；
2. 在树上执行顺序遍历，以使元素按排序顺序返回。

插入排序的步骤：
1. 创建一个BST节点，其值等于数组元素 `array[i]`；
2. Insert(node, key): 如果 `root` == null，那么返回新形成的节点；如果 `root->data` < `key`，那么 `root->right` = `insert(root->right, key)`；如果 `root->data` > `key`，那么 `root->left` = `insert(root->left, key)`；
3. 返回指向原始根结点的游标。

顺序遍历操作：遍历左子树 → 访问根结点 → 遍历右子树。

## 三、时间复杂度的分析

在平均情况下，在BST中插入n个节点的时间复杂度为 $\Theta(n \log_2(n))$ 量级。当形成的BST是平衡BST时，会发生这种情况。因此，时间复杂度为 $\Theta(n \log_2(n))$ 量级。

最坏的情况发生在数组排序时，并形成最大高度为 $O(n)$ 的非平衡二叉搜索树。与高度 $\log_2(n)$ 的常规BST情况下的 $O(\log_2(n))$ 时间相比，它需要 $O(n)$ 时间进行遍历和 $O(n^2)$ 时间进行插入。最坏情况下的时间复杂度是 $O(n^2)$。可以使用自平衡数据结构（如AVL树、红黑树等）将其缩减为 $O(n \log_2(n))$。

最佳情况发生在形成的二叉搜索树平衡时。时间复杂度的最佳情况是 $\Omega(n \log_2(n))$。这与平均案例时间复杂度相同。

## 四、空间复杂度的分析

该算法的空间复杂度为：$O(n)$，因为必须为二叉搜索树中的每个元素创建 $n$ 个节点。

## 五、算法实现

```python
class node():
    def __init__(self, val): # BST data structure
        self.val = val
        self.left = None
        self.right = None
    
    def insert(self, val) -> None:
        if self.val:
            if val < self.val: # 若逆序此处可以变为 val > self.val
                if self.left is None:
                    self.left = node(val)
                else:
                    self.left.insert(val)
            else:
                if self.right is None:
                    self.right = node(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

def inorder(root: node, result: list) -> None:
    '''
    root: 存储插入序列的根节点指示。
    result: 存储遍历结果的数组.
    '''
    if root:
        inorder(root.left, result)
        result.append(root.val)
        inorder(root.right, result)        

def tree(array: list, reverse: bool=False) -> list:
    '''
    array: 支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    reverse: 是否降序, 默认采用升序。
    '''
    if not array:
        return array
    root = node(array[0]) # Initial
    for index in range(1, len(array)): # Build
        root.insert(array[index])
    result = []
    inorder(root, result) # Traverse BST in order
    if reverse:
        result.reverse()
    return result
```