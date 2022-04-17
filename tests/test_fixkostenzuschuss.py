from fixkostenzuschuss.FKZ_800 import FKZ_800, _valid_combination


def test_valid_combination():
    assert _valid_combination([]) == True
    assert _valid_combination([1, 2]) == True
    assert _valid_combination([1, 2, 4, 5]) == True
    assert _valid_combination([1, 2, 4, 5, 7, 8]) == False
    assert _valid_combination([1, 2, 4, 5, 7, 9]) == False
    assert _valid_combination([2, 4, 5]) == True


def test_basis_FKZ_800():
    assert FKZ_800(
        sales_19=[2000, 2000, 2000],
        sales_20=[1000, 1000, 1000],
        fixed_cost=[500, 1000, 500],
    ) == (1000, (0, 1, 2))
    assert FKZ_800(
        sales_19=[2000, 2000, 2000],
        sales_20=[500, 3000, 3000],
        fixed_cost=[1000, 1000, 500],
    ) == (750.0, (0,))
    assert FKZ_800(
        sales_19=[2000, 2000, 2000],
        sales_20=[3000, 3000, 3000],
        fixed_cost=[500, 1000, 500],
    ) == (0, ())


def test_different_input_FKZ_800():
    assert FKZ_800(
        sales_19=[2000.5, 3000.5, 2000.5],
        sales_20=[1000, 2000, 3000],
        fixed_cost=[500.60, 1500.45, 500.30],
    ) == (800.6600779844033, (0,1))

