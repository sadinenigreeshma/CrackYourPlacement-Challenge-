###https://leetcode.com/problems/move-zeroes/


class Solution(object):
    def moveZeroes(self, nums):
        ins=nums.count(0)
        for i in range(ins):
            nums.remove(0)
            nums.append(0)
        return nums
