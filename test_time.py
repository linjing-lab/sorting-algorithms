# 导包
import sortingx
import time
import polars as pl
import random
from typing import List

# 测试
class Timer:
    def __init__(self, genre: str, method: List[str], part: List[bool]=None):
        '''
        genre: 类型名称; method: 方法列表; part: 方法是否含参数l与r.
        '''
        if part != None:
            assert len(part) == len(method)
        self.method = 'sortingx.' + genre
        self.call = method # genre.def
        self.part = part
        self.dict = {} # 训练日志 

    def generate(self, left: int=0, right: int=100, size: int=10000, seed: int=0) -> str:
        '''
        left: 数值范围左限, 默认值为0; right: 数值范围右限, 默认值为100; size: 数据大小, 默认值为10000; seed: 随机数种子, 默认值为0.
        '''
        if seed != None:
            random.seed(seed)
        self.data = [random.randint(left, right) for _ in range(size)]
        self.testing = [self.data for _ in range(len(self.call))]
        return 'The Test Data Is Generated!'
    
    def collect(self, digit: int=3) -> str:
        '''
        函数运行时间收集。digit: 控制小数点位数.
        '''
        for index, value in enumerate(self.call):
            func = eval(self.method + '.' + value)
            if self.part == None or self.part[index] == False:
                times = time.time()
                func(self.testing[index])
                timee = time.time()
            else:
                times = time.time()
                func(self.testing[index], 0, len(self.data) - 1)
                timee = time.time()
            self.dict[value] = [round(timee-times, digit)]
        return 'The Time Record of {0} is: \n{1}'.format(self.method, pl.DataFrame(self.dict))

# 测试实例1
'''
Counting = Timer('counting', ['whilediv', 'forenum', 'reverfill'])
print(Counting.generate(0, 100, 10000, 1))
print(Counting.collect(3))
'''

# 输出样例
'''
The Test Data Is Generated!
The Time Record of sortingx.counting is: 
shape: (1, 3)
┌──────────┬─────────┬───────────┐
│ whilediv ┆ forenum ┆ reverfill │
│ ---      ┆ ---     ┆ ---       │
│ f64      ┆ f64     ┆ f64       │
╞══════════╪═════════╪═══════════╡
│ 0.002    ┆ 0.003   ┆ 0.005     │
└──────────┴─────────┴───────────┘
'''

# 测试实例2
'''
Quick = Timer('quick', ['lamb', 'recur', 'stack'], [False, True, True])
print(Quick.generate(0, 100, 10000, 1))
print(Quick.collect(3))
'''

# 输出样例
'''
The Test Data Is Generated!
The Time Record of sortingx.quick is: 
shape: (1, 3)
┌───────┬───────┬────────┐
│ lamb  ┆ recur ┆ stack  │
│ ---   ┆ ---   ┆ ---    │
│ f64   ┆ f64   ┆ f64    │
╞═══════╪═══════╪════════╡
│ 0.122 ┆ 0.138 ┆ 12.465 │
└───────┴───────┴────────┘
'''

# 测试实例3
'''
Bubble = Timer('bubble', ['normal', 'flag', 'bidirect'])
print(Bubble.generate(0, 100, 10000, 1))
print(Bubble.collect(3))
'''

'''
The Test Data Is Generated!
The Time Record of sortingx.bubble is: 
shape: (1, 3)
┌────────┬───────┬──────────┐
│ normal ┆ flag  ┆ bidirect │
│ ---    ┆ ---   ┆ ---      │
│ f64    ┆ f64   ┆ f64      │
╞════════╪═══════╪══════════╡
│ 10.638 ┆ 0.001 ┆ 0.002    │
└────────┴───────┴──────────┘
'''

# 测试实例4
'''
Bucket = Timer('bucket', ['numeric', 'mobase'])
print(Bucket.collect(3))
'''

'''
The Test Data Is Generated!
The Time Record of sortingx.bucket is:
shape: (1, 2)
┌─────────┬────────┐
│ numeric ┆ mobase │
│ ---     ┆ ---    │
│ f64     ┆ f64    │
╞═════════╪════════╡
│ 0.008   ┆ 0.005  │
└─────────┴────────┘
'''

# 测试实例5
'''
Insertion = Timer('insertion', ['direct', 'binary'])
print(Insertion.generate(0, 100, 10000, 1))
print(Insertion.collect(3))
'''

'''
The Test Data Is Generated!
The Time Record of sortingx.insertion is: 
shape: (1, 2)
┌────────┬────────┐
│ direct ┆ binary │
│ ---    ┆ ---    │
│ f64    ┆ f64    │
╞════════╪════════╡
│ 5.481  ┆ 0.078  │
└────────┴────────┘
'''

# 测试实例6
'''
Merge = Timer('merge', ['recur', 'stack'])
print(Merge.generate(0, 100, 10000, 1))
print(Merge.collect(3))
'''

'''
The Test Data Is Generated!
The Time Record of sortingx.merge is: 
shape: (1, 2)
┌───────┬───────┐
│ recur ┆ stack │
│ ---   ┆ ---   │
│ f64   ┆ f64   │
╞═══════╪═══════╡
│ 0.063 ┆ 0.051 │
└───────┴───────┘
'''

# 测试实例7
'''
Selection = Timer('selection', ['normal', 'withmax'])
print(Selection.generate(0, 100, 10000, 1))
print(Selection.collect(3))
'''

'''
The Test Data Is Generated!
The Time Record of sortingx.selection is: 
shape: (1, 2)
┌────────┬─────────┐
│ normal ┆ withmax │
│ ---    ┆ ---     │
│ f64    ┆ f64     │
╞════════╪═════════╡
│ 5.347  ┆ 4.734   │
└────────┴─────────┘
'''

# 测试实例8
'''
Shell = Timer('shell', ['donald', 'knuth', 'hibbard', 'sedgewick'])
print(Shell.generate(0, 100, 10000, 1))
print(Shell.collect(3))
'''

'''
The Test Data Is Generated!
The Time Record of sortingx.shell is: 
shape: (1, 4)
┌────────┬───────┬─────────┬───────────┐
│ donald ┆ knuth ┆ hibbard ┆ sedgewick │
│ ---    ┆ ---   ┆ ---     ┆ ---       │
│ f64    ┆ f64   ┆ f64     ┆ f64       │
╞════════╪═══════╪═════════╪═══════════╡
│ 0.098  ┆ 0.014 ┆ 0.029   ┆ 0.017     │
└────────┴───────┴─────────┴───────────┘
'''