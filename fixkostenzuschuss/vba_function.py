

def FKZ_800(sales_19, sales_20, fixed_cost):
    #TODO: Test sales_19 and sales_20 and fixed_costs have the same length
    
    possible_combination = __starting_combination([[i] for i in range(len(sales_19))])
    valid_combination = [__valid_combination(i) for i in possible_combination]
    combination = [i for (i, v) in zip(possible_combination, valid_combination) if v]
    sum_s19 = [sum([sales_19[i] for i in x]) for x in combination]
    sum_s20 = [sum([sales_20[i] for i in x]) for x in combination]
    sum_fc = [sum([fixed_cost[i] for i in x]) for x in combination]
    rs = [fc * (1 - s20 / s19) for (s19, s20, fc) in zip(sum_s19, sum_s20, sum_fc)]

    rs_max = max(rs)
    rs_comb = combination[rs.index(rs_max)]

    return((rs_max, rs_comb))


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

sales_19 = [100, 110, 120, 1123, 123, 4235, 5346, 456 ,456, 4656 ,567, 7567, 768, 3456, 345, 345, 4645,345, 123, 2345]
[100, 110, 120, 1123, 123, 4235, 5346, 456 ,456, 4656 ,567, 7567, 768, 3456, 345, 345, 4645,345, 123, 2345]
sales_20 = [123, 123, 243, 456 ,1234, 234, 234, 345,345, 123, 2345, 345, 345 ,345, 3546, 3546, 345, 345,356,3456]
[123, 123, 243, 456 ,1234, 234, 234, 345,345, 123, 2345, 345, 345 ,345, 3546, 3546, 345, 345,356,3456]
fixed_cost = [123,324,1233,432,234, 345,345,453,345,324,234,452,234,2345,234,45,434,234,34,5436]
[123,324,1233,432,234, 345,345,453,345,324,234,452,234,2345,234,45,434,234,34,543]

FKZ_800(sales_19,sales_20,fixed_cost)