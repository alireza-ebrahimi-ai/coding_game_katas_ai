from src.kuy4.matrix_determinatant import determinant


def test_0day_1():
    assert determinant([1]) == 1


def test_0day_71():
    assert determinant([71]) == 71


def test_2x2():
    assert determinant([[1,3],[2,5]]) == -1


def test3x3():
        assert determinant([[2,5,3], [1,-2,-1], [1, 3, 4]]) == -20
