
import pytest

@pytest.mark.parametrize('HDL_level, expected', [(85, 'normal'), (50, 'borderline low'), (30, 'low')])


def test_check_HDL(HDL_level, expected):
    from blood_calculator import check_HDL
    answer = check_HDL(HDL_level)
    assert answer == expected


@pytest.mark.parametrize('LDL_level, expected', [(100, 'normal'), (140, 'borderline high'), (170, 'high'), (200, 'very high')])

def test_check_LDL(LDL_level, expected):
    from blood_calculator import check_LDL
    answer = check_LDL(LDL_level)
    assert answer == expected


@pytest.mark.parametrize('chol_level, expected', [(150, 'normal'), (220, 'borderline high'), (300, 'high')])

def test_check_cholesterol(chol_level, expected):
    from blood_calculator import check_cholesterol
    answer = check_cholesterol(chol_level)
    assert answer == expected   


