
import pytest

@pytest.mark.parametrize('HDL_level, expected', [(85, 'normal'), (50, 'borderline   low'), (30, 'low')])


def test_check_HDL(HDL_level, expected):
    from blood_calculator import check_HDL
    answer = check_HDL(HDL_level)
    assert answer == expected


