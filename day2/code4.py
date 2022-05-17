###https://leetcode.com/problems/find-all-duplicates-in-an-array/submissions/


class Solution(object):
    def findDuplicates(self, nums):
        nums.sort()
        l=[]
        i=0
        while(i<len(nums)-1):
            if(nums[i]==nums[i+1]):
                l.append(nums[i])
                i+=1
            i+=1
        return l
