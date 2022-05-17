   ###https://leetcode.com/problems/container-with-most-water/submissions/ 
  
  def maxArea(self, height):
        left=0
        nums=height
        right=len(height)-1
        maxi=0
        while(left<right):
            ans=min(nums[left],nums[right])*(right-left)
            maxi=max(ans,maxi)
            temp=max(nums[left],nums[right])
            if(temp==nums[left]):
                right-=1
            else:
                left+=1
        return maxi
