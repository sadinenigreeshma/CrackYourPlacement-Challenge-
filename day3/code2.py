###https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/submissions/


class Solution(object):
    def maxScore(self, cardPoints, k):
        left=0
        right=len(cardPoints)-1
        ins=0
        sum1=0
        ins1=k
        nums=cardPoints
        while(ins<k):
            temp=nums[left:left+ins1:1]
            temp1=nums[right:right-ins1:-1]
            if(sum(temp)>sum(temp1)):
                sum1+=nums[left]
                left+=1
            else:
                sum1+=nums[right]
                right-=1
            ins+=1
            ins1-=1
        return sum1
