###https://leetcode.com/problems/two-sum/submissions/



class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            temp=target-nums[i]
            if(temp in nums[i+1:]):
                print(i+1 ,   temp)
                
                return [i,nums[i+1:].index(temp)+1+i]
