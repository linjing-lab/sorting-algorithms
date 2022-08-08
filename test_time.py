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
        self.part = part # 
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
            gap = round(timee-times, digit)
            self.dict[value] = [gap]
        return 'The Process of Collection Is Over!'
    
    def ouput(self) -> str:
        '''
        测试日志
        '''
        return 'The Time Record of {0} is: \n{1}'.format(self.method, pl.DataFrame(self.dict))

# 测试实例1
Counting = Timer('counting', ['whilediv', 'forenum', 'reverfill'])
print(Counting.generate(0, 100, 10000, 1))
print(Counting.collect(3))
print(Counting.ouput())

# 输出样例
'''
The Test Data Is Generated!
The Process of Collection Is Over!
The Time Record of sortingx.counting is:
shape: (1, 3)
┌──────────┬─────────┬───────────┐
│ whilediv ┆ forenum ┆ reverfill │
│ ---      ┆ ---     ┆ ---       │
│ f64      ┆ f64     ┆ f64       │
╞══════════╪═════════╪═══════════╡
│ 0.002    ┆ 0.002   ┆ 0.004     │
└──────────┴─────────┴───────────┘
'''

# 测试实例2
Quick = Timer('quick', ['lamb', 'recur', 'stack'], [False, True, True])
print(Quick.generate(0, 100, 10000, 1))
print(Quick.collect(3))
print(Quick.ouput())

# 输出样例
'''
The Test Data Is Generated!
The Process of Collection Is Over!
The Time Record of sortingx.quick is: 
shape: (1, 3)
┌───────┬───────┬────────┐
│ lamb  ┆ recur ┆ stack  │
│ ---   ┆ ---   ┆ ---    │
│ f64   ┆ f64   ┆ f64    │
╞═══════╪═══════╪════════╡
│ 0.117 ┆ 0.146 ┆ 12.033 │
└───────┴───────┴────────┘
'''