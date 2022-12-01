from calories import calories_max
from calories_k import calories_max_k


def test_single_elf():
    assert calories_max([[2]]) == 2


def test_two_elfs():
    assert calories_max([[1], [2]]) == 2


def test_one_elf_with_multiple_food():
    assert calories_max([[1, 1]]) == 2


def test_one_elf_with_zero_foods():
    assert calories_max([[]]) == 0


def test_calories_max_k():
    assert calories_max_k([[10], [20], [30]]) == 60


def test_calories_max_k():
    assert calories_max_k([[10], [20], [30], [5]]) == 60
