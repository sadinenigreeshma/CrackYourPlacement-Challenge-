###https://leetcode.com/problems/majority-element/submissions/



class Solution(object):
    def majorityElement(self, nums):
        for i in range(len(nums)):
            if(nums[i] in nums[:i]):
                continue
            elif(nums.count(nums[i])>(len(nums))/2):
                return nums[i]
