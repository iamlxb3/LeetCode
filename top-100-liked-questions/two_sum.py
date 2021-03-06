# https://leetcode.com/problems/two-sum/description/


# -------------------------------------------------------------------------------------
# Description
# -------------------------------------------------------------------------------------
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# -------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------
# solution by others
# O(n)
# -------------------------------------------------------------------------------------
class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i
# -------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------
# my solution
# -------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------
