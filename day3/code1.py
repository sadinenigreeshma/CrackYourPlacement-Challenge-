###https://leetcode.com/problems/3sum/submissions/
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        l=[]
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            k=[]
            if(i!=0):
                if(nums[i]==nums[i-1]):
                    continue
            while(left<right):
                sum=nums[i]+nums[left]+nums[right]
                if(sum==0):
                    k=[nums[i],nums[left],nums[right]]
                    print(k)
                    if(k not in l):
                        l.append(k)
                    left+=1
                    right-=1
                elif(sum>0):
                    right-=1
                else:
                    left+=1
        return l
 
