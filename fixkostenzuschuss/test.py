from itertools import combinations, chain, compress
from typing import List, Tuple
import numpy as np

def function_1():
    sales_19 = [100, 110, 120, 1123, 123, 4235, 5346, 456 ,456, 4656 ,567, 7567, 768, 3456, 345, 345, 4645,345, 123, 2345]
    sales_19_np = np.asarray(sales_19)
    y = range(len(sales_19_np))

    x = chain.from_iterable(combinations(y, r) for r in range(1,len(y)+1))
    valid_combination = np.array([np.array(i) for i in x if np.sum(np.diff(np.array(i))-1 > 0) < 2])
    return(valid_combination)

def function_2():
    sales_19 = [100, 110, 120, 1123, 123, 4235, 5346, 456 ,456, 4656 ,567, 7567, 768, 3456, 345, 345, 4645,345, 123, 2345]
    sales_19_np = np.asarray(sales_19)
    y = range(len(sales_19_np))

    x = chain.from_iterable(combinations(y, r) for r in range(1,len(y)+1))
    x = np.array([i for i in x])

    pad = len(max(x, key=len))
    q = np.array([list(j) + [0]*(pad-len(j)) for j in x])
    x = x[np.sum(np.diff(q, n=1, axis=1) - 1 > 0, axis=1)<2]
    return(x)



def __starting_combination(arr):
    lst = []
    for i in range(len(arr)):
        x = __combination(arr[(i+1):])
        for q in range(len(x)):
            x[q] = sorted(x[q] + arr[i])
        lst += x

    return(lst)


def __combination(arr):
    if len(arr) <= 0:
        return([[]])
    
    cs = []
    c = __combination(arr[1:])
    for i in range(len(c)):
        cs.append(c[i])
        sort_arr = list(c[i] + arr[0])
        cs.append(sort_arr)
    return(cs)

def __valid_combination(arr):
    gap_counter = 0
    if len(arr) > 2:
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] > 1:
                gap_counter += 1
    return(gap_counter<=1)


def function_3():
    sales_19 = [100, 110, 120, 1123, 123, 4235, 5346, 456 ,456, 4656 ,567, 7567, 768, 3456, 345, 345]
    possible_combination = __starting_combination([[i] for i in range(len(sales_19))])
    valid_combination = [__valid_combination(i) for i in possible_combination]
    combination = [i for (i, v) in zip(possible_combination, valid_combination) if v]
    return(combination)

def function_4():
    sales_19 = [100, 110, 120, 1123, 123, 4235, 5346, 456 ,456, 4656 ,567, 7567, 768, 3456, 345, 345, 4645,345, 123, 2345, 2343]
    possible_combination = chain.from_iterable(combinations(sales_19, r) for r in range(1,len(sales_19)+1))
    valid_combination = [__valid_combination(i) for i in possible_combination]
    combination = [i for (i, v) in zip(possible_combination, valid_combination) if v]
    return(combination)


def function_5():
    sales_19 = [100, 110, 120, 1123, 123, 4235, 5346, 456 ,456, 4656 ,567, 7567, 768, 3456, 345, 345, 4645,345, 123, 2345, 2343]
    possible_combination = chain.from_iterable(map(lambda x: combinations(sales_19, x), range(1,len(sales_19)+1)))
    valid_combination = [__valid_combination(i) for i in possible_combination]
    combination = [i for (i, v) in zip(possible_combination, valid_combination) if v]
    return(combination)

def function_6():
    sales_19 = [100, 110, 120, 1123, 123, 4235, 5346, 456 ,456, 4656 ,567, 7567, 768, 3456, 345, 345, 4645,345, 123, 2345, 2343]
    possible_combination = chain.from_iterable(map(lambda x: combinations(sales_19, x), range(1,len(sales_19)+1)))
    valid_combination = [__valid_combination(i) for i in possible_combination]
    combination = compress(possible_combination, valid_combination)
    return(combination)

def function_7():
    sales_19 = [100, 110, 120, 1123, 123, 4235, 5346, 456 ,456, 4656 ,567, 7567, 768, 3456, 345, 345, 4645,345, 123, 2345, 2343]
    possible_combination = chain.from_iterable(map(lambda x: combinations(sales_19, x), range(1,len(sales_19)+1)))
    combination = [i for i in possible_combination if __valid_combination(i)]
    return(combination)


