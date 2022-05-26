###https://leetcode.com/problems/minimum-window-substring/submissions/



class Solution(object):
    def minWindow(self, s, t):
        ins={}
        for i in range(len(t)):
           ins[t[i]]=t.count(t[i])
        j=0
        i=0
        count=len(ins)
        mini=len(s)+1
        found=False
        left=0
        right=0
        if(len(t)>len(s)):
            return ""
        while(j<len(s)):
            if(s[j] in ins.keys()):
                ins[s[j]]-=1
                if(ins[s[j]]==0):
                    count-=1
            j+=1
            if(count>0):
                continue
            while(count<1):
                if(s[i] in ins.keys()):
                    ins[s[i]]+=1
                    if(ins[s[i]]>0):
                        count+=1
                i+=1
            if (j-i)<mini:
                left=i
                right=j
                mini=j-i
                found=True
        print(s[left:right])
        if(found==False):
            return ""
        else:
            return s[left-1:right]
        
  
