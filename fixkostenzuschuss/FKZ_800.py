from itertools import combinations, chain
from typing import List, Tuple, Union

MIN_PERCENTAGE_LOSS = 0.4
MIN_BENEFIT_PAY = 500
MAX_GAP = 1


def FKZ_800(
    sales_19: List[Union[int, float]],
    sales_20: List[Union[int, float]],
    fixed_cost: List[Union[int, float]],
) -> Tuple[float, Tuple[int]]:
    """Calculates which month to choose to maximize the austrian governmental
    company subsidy called "Fixkostenzuschuss 800.000"

    Args:
        sales_19 (List[Union[int, float]]): monthly Sales of 2019
        sales_20 (List[Union[int, float]]): monthly Sales of 2020
        fixed_cost (List[Union[int, float]]): monthly fixed cost of

    Returns:
        Tuple[float, List[int]]:
        Returns a Tuple with the first entry the maximized governmental support
        and the second which month leads to this reult
    """

    if not (len(sales_19) == len(sales_20) == len(fixed_cost)):
        raise DifferentLenghtError(
            "The Input Vectors sales_19, sales_20 and fixed_cost are not equal length"
        )
    length = len(sales_19)
    possible_combination = chain.from_iterable(
        combinations(range(length), r) for r in range(1, length + 1)
    )

    rs, combination = [], []
    for x in possible_combination:
        if _valid_combination(x):
            sum_s19, sum_s20, sum_fc = 0, 0, 0
            for i in x:
                sum_s19 += sales_19[i]
                sum_s20 += sales_20[i]
                sum_fc += fixed_cost[i]
            percentage_loss = 1 - sum_s20 / sum_s19
            benefit = sum_fc * percentage_loss
            if (percentage_loss >= MIN_PERCENTAGE_LOSS) & (benefit >= MIN_BENEFIT_PAY):
                combination.append(x)
                rs.append(benefit)
    if len(rs) > 0:
        rs_max = max(max(rs), 0)
        rs_comb = combination[rs.index(rs_max)]
    else:
        rs_max = 0
        rs_comb = ()

    return (rs_max, rs_comb)


def _valid_combination(arr: Union[List[int], Tuple[int, ...]]) -> bool:
    """Checks if the vector arr is a possible month combination for the governmental support.
    This means the vector is only allowed to have two consecutive periods e.g. [2,3,4,6,7,8]

    Args:
        arr (Union[List[int], Tuple[int, ...]]): A Vector with numerated month combination

    Returns:
        bool: If it is a valid combination or not
    """
    arr = sorted(arr)
    gap_counter = 0
    if len(arr) > 2:
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] > 1:
                gap_counter += 1
    return gap_counter <= MAX_GAP


class DifferentLenghtError(Exception):
    pass
