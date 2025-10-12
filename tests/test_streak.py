from streak import longest_positive_streak

def test_empty_list():
    assert longest_positive_streak([]) == 0

def test_multiple_streaks():
    assert longest_positive_streak([1, 2, 0, 4, 5, 6, 0, 1]) == 3

def test_with_negatives():
    assert longest_positive_streak([-1, -2, 1, 2, 3, -4, 1, 2]) == 3

def test_with_zeros():
    assert longest_positive_streak([0, 0, 1, 2, 0, 1, 2, 3, 0]) == 3

def test_all_positive():
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_all_negative():
    assert longest_positive_streak([-1, -2, -3, -4, -5]) == 0

def test_no_streak():
    assert longest_positive_streak([0, -1, 0, -2, 0]) == 0
