from collections import Counter


def check_pairs(list_count):
    tuple_count = Counter(tuple(pair) for pair in list_count)
    result = [[*pair, count] for pair, count in tuple_count.items()]
    return result


def test_check_pairs():
    TEST_DATA = [['665587', 2], ['669532', 1], ['669537', 2], ['669532', 1], ['665587', 1]]
    TEST_RESULT = [['665587', 2, 1], ['669532', 1, 2], ['669537', 2, 1], ['665587', 1, 1]]
    assert check_pairs(TEST_DATA) == TEST_RESULT
