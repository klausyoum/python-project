import pytest
from myproj.array import Array


@pytest.mark.parametrize(
    "array,expected",
    [
        pytest.param(Array('1 2 3 4 10 11'), 31),
        pytest.param(Array('1 2 3 4 10 15'), 35)
    ]
)
def test_sum(array, expected):
    result = array.sum(6)
    assert result == expected


def test_sum_raise_exception():
    array = Array('1 2 3 4 10 11')
    with pytest.raises(Exception):
        array.sum(5)
