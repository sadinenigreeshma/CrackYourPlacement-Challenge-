''' https://leetcode.com/problems/remove-duplicates-from-sorted-array/ '''

class Solution(object):
def removeDuplicates(self, nums):
"""
:type nums: List[int]
:rtype: int
"""
count=1
for i in range(1,len(nums)):
  if(nums[i-1]!=nums[i]):
    nums[count]=nums[i]
    count+=1
return count
