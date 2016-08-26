from hacker_rank.Algorithms.implementation.src.bigger_is_greater import Permutation


task = Permutation()

def test_simple_test():
    assert 2 == 2


def test_word_size():
    assert task.word_size('a') == 1
    assert task.word_size('abc') == 5


def test_letter_size():
    assert task.letter_size('b') == 2