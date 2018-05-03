"""
https://leetcode.com/problems/two-sum/description/

Given an array of integers, return indices of the two numbers such that they
 add up to a specific target.
You may assume that each input would have exactly one solution, and you may
 not use the same element twice.
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hash_table = {}
        for i in range(len(nums)):
            if target - nums[i] in hash_table:
                return [hash_table[target - nums[i]], i]
            hash_table[nums[i]] = i
