from itertools import combinations, chain
from typing import List, Tuple
import numpy as np

def FKZ_800(sales_19, sales_20, fixed_cost):
    sales_19_np = np.asarray(sales_19)
    sales_20_np = np.asarray(sales_20)
    fixed_costs_np = np.asarray(fixed_cost)

    y = range(len(sales_19_np))

    x = chain.from_iterable(combinations(y, r) for r in range(1,len(y)+1))
    x = np.array([i for i in x])

    pad = len(max(x, key=len))
    q = np.array([list(j) + [0]*(pad-len(j)) for j in x])
    x = x[np.sum(np.diff(q, n=1, axis=1) - 1 > 0, axis=1)<2]
    #valid_combination = np.array([np.array(i) for i in x if np.sum(np.diff(np.array(i))-1 > 0) < 2])
    #valid = np.array([np.sum(np.diff(i)-1)<=1 for i in x])
    #valid_combination = x[valid]

    eum_s19 = np.array([np.sum(sales_19_np[i]) for i in valid_combination])
    sum_s20 = np.array([np.sum(sales_20_np[i]) for i in valid_combination])
    sum_fc = np.array([np.sum(fixed_costs_np[i]) for i in valid_combination])
    rs = sum_fc * (1 - sum_s20 / sum_s19)
    rs_max = np.max(rs)
    rs_comb = valid_combination[rs == rs_max]

    return((rs_max, rs_comb))


sales_19 = [100, 110, 120, 1123, 123, 4235, 5346, 456 ,456, 4656 ,567, 7567, 768, 3456, 345, 345, 4645,345, 123, 2345]
[100, 110, 120, 1123, 123, 4235, 5346, 456 ,456, 4656 ,567, 7567, 768, 3456, 345, 345, 4645,345, 123, 2345]
sales_20 = [123, 123, 243, 456 ,1234, 234, 234, 345,345, 123, 2345, 345, 345 ,345, 3546, 3546, 345, 345,356,3456]
[123, 123, 243, 456 ,1234, 234, 234, 345,345, 123, 2345, 345, 345 ,345, 3546, 3546, 345, 345,356,3456]
fixed_cost = [123,324,1233,432,234, 345,345,453,345,324,234,452,234,2345,234,45,434,234,34,5436]
[123,324,1233,432,234, 345,345,453,345,324,234,452,234,2345,234,45,434,234,34,543]

FKZ_800(sales_19,sales_20,fixed_cost)


i.shape
as.List()


import timing

@timing.MeasureTime
def function_1(sales_19_np):
    y = range(len(sales_19_np))

    x = chain.from_iterable(combinations(y, r) for r in range(1,len(y)+1))
    valid_combination = np.array([np.array(i) for i in x if np.sum(np.diff(np.array(i))-1 > 0) < 2])
    return(valid_combination)


def function_2(sales_19_np):
    y = range(len(sales_19_np))

    x = chain.from_iterable(combinations(y, r) for r in range(1,len(y)+1))
    x = np.array([i for i in x])

    pad = len(max(x, key=len))
    q = np.array([list(j) + [0]*(pad-len(j)) for j in x])
    x = x[np.sum(np.diff(q, n=1, axis=1) - 1 > 0, axis=1)<2]
    return(x)

def function_2(sales_19_np):
    y = range(len(sales_19_np))

    x = chain.from_iterable(combinations(y, r) for r in range(1,len(y)+1))
    x = np.array([i for i in x])

    pad = len(max(x, key=len))
    q = np.array([list(j) + [0]*(pad-len(j)) for j in x])
    x = x[np.sum(np.diff(q, n=1, axis=1) - 1 > 0, axis=1)<2]
    return(x)

def function_3(sales_19):
    possible_combination = __starting_combination([[i] for i in range(len(sales_19))])
    valid_combination = [__valid_combination(i) for i in possible_combination]
    combination = [i for (i, v) in zip(possible_combination, valid_combination) if v]
    return(combination)