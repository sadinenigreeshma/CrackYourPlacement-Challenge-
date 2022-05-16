###https://leetcode.com/problems/find-the-duplicate-number/

class Solution(object):
def findDuplicate(self, nums):
"""
:type nums: List[int]
:rtype: int
"""
for i in range(len(nums)):
if(nums[0]!=nums[nums[0]]):
nums[nums[0]],nums[0]=nums[0],nums[nums[0]]
else:
return nums[0]
