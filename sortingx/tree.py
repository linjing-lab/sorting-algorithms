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