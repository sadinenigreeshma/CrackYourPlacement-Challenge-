###https://leetcode.com/problems/integer-to-roman/submissions/

class Solution(object):
    def intToRoman(self, num):
        d={1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        st_n=str(num)
        st=""
        for i in range(len(st_n)-1,-1,-1):
            q=num//10**i
            if (q==9)|(q==4):
                st += d[10**i]+d[(q+1)*(10**i)]
            elif (q>5):
                st += d[5*(10**i)]+d[10**i]*(q-5)
            elif q==5 :
                st += d[5*(10**i)]
            else:
                st += d[10**i]*q    
            num=num%10**i
        return(st)
