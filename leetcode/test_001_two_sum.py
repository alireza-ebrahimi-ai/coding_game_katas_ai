from leetcode.alg_001_two_sum import Solution


solution = Solution()


def test_case_0():
    assert solution.twoSum([1, 2, 3], 3)


def test_case_1():
    assert 0 in solution.twoSum([1, 2, 3], 3)
    assert 1 in solution.twoSum([1, 2, 3], 3)


def test_case_2():
    assert 0 not in solution.twoSum([1, 2, 3, 4, 5, 6], 11)
    assert 4 in solution.twoSum([1, 2, 3, 4, 5, 6], 11)
