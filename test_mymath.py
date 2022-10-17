

import pytest

@pytest.mark.parametrize('input_one, input_two, expected', [(1, 2, 3), (2, 3, 5), (4, -1, 3)])

def test_add(input_one, input_two, expected):
    from mymath import myadd
    answer = myadd(input_one, input_two)
    assert answer == expected


