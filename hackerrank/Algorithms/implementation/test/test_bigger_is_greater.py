from hackerrank.Algorithms.implementation.src.bigger_is_greater import Permutation
import pytest

task = Permutation()

def test_simple_test():
    assert 2 == 2


def test_word_size():
    assert task.word_size('a') == 1
    assert task.word_size('abc') == 6


def test_letter_size():
    assert task.letter_size('b') == 2


def test_word_to_array():
    assert task.word_to_array('abc') == ['a', 'b', 'c']


def test_longest_suffix():
    assert task.longest_suffix('abcde') == 'e'
    assert task.longest_suffix('edcba') == 'edcba'
    assert task.longest_suffix('cabc') == 'c'
    assert task.longest_suffix('abcabc') == 'c'
    assert task.longest_suffix('a') == 'a'
    assert task.longest_suffix('bb') == 'bb'
    assert task.longest_suffix('abcfdda') == 'fdda'
    assert task.longest_suffix('0125330') == '5330'


def test_pivot():
    assert task.pivot('edcba', 'edcba') == 0
    assert task.pivot('e', 'abcde') == 'd'
    assert task.pivot('c', 'abcabc') == 'b'
    assert task.pivot('fdda', 'abcfdda') == 'c'
    assert task.pivot('5330', '0125330') == '2'


def test_swap():
    assert task.swap('e', 'ebcd') == 'debce'
    assert task.swap('d', 'e') == 'ed'
    assert task.swap('f', 'aafff') == 'aaffff'
    assert task.swap('c', 'fdda') == 'dfdca'
    assert task.swap('2', '5330') == '35320'


def test_reverse():
    assert task.reverse('abcd') == 'dcba'
    assert task.reverse(('ddbba')) == 'abbdd'
    assert task.reverse('fdca') == 'acdf'
    assert task.reverse(('5320')) == '0235'


def test_collect_all():
    assert task.collect_all('abc', 'b', 'c') == 'abc'
    assert task.collect_all('abasdf', 'b', 'qwer') == 'abqwer'
    assert task.collect_all('aaabcbc', 'a', 'abcbc') == 'aaabcbc'

