###https://leetcode.com/problems/spiral-matrix/submissions/

class Solution(object):
    def spiralOrder(self, matrix):
        left,right=0,len(matrix[0])
        top,bottom=0,len(matrix)
        l=[]
        while(left<right and top<bottom):
            k=left
            k3=bottom
            while(k!=right):
                l.append(matrix[top][k])
                k+=1
            top+=1
            k1=top
            while(k1!=bottom):
                l.append(matrix[k1][right-1])
                k1+=1
            right-=1
            k2=right
            if not (left<right and top<bottom):
                break
            while(k2!=left):
                k2-=1
                l.append(matrix[bottom-1][k2])
            bottom-=1
            k3=bottom
            while(k3!=top):
                k3-=1
                l.append(matrix[k3][left])
            left+=1
        return l
