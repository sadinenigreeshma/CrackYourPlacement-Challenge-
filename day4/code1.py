


###https://leetcode.com/problems/valid-parentheses/submissions/


class Solution(object):
    def isValid(self, s):
        l=[]
        l.append(s[0])
        if(len(s)==0 or len(s)==1):
            return False
        for i in range(1,len(s)):
            if(len(l)>len(s[i:])):
                return False
            if(len(l)==0 and (s[i]==')' or s[i]==']' or s[i]=='}')):
                return False
            elif(s[i]=='(' or s[i]=='[' or s[i]=='{'):
                l.append(s[i])
                k=i
            elif(l[-1]=='(' and s[i]==')'):
                l.pop()
                k=i
            elif(l[-1]=='[' and s[i]==']'):
                l.pop()
                k=i
            elif(l[-1]=='{' and s[i]=='}'):
                l.pop()
                k=i
            elif(s[i]==')' or s[i]==']' or s[i]=='}'):
                if(s[i]==')' and '(' not in l):
                    return False
                elif(s[i]==']' and '[' not in l):
                    return False
                elif(s[i]=='}' and '{' not in l):
                    return False
        if(len(l)==0 and k==len(s)-1):
            return True
        else:
            return False
