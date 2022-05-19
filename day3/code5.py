###https://leetcode.com/problems/jump-game/submissions/



class Solution(object):
    def canJump(self, nums):
        ins=0
        if(nums.count(0)==0):
            return True
        for i in range(len(nums)):
            if(ins<i):
                return False
            else:
                ins=max(ins,i+nums[i])
        return True
