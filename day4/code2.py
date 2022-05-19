
###https://leetcode.com/problems/implement-strstr/submissions/

class Solution(object):
    def strStr(self, haystack, needle):
        if len(needle)==0:
            return 0
        if(len(needle)>len(haystack)):
            return -1
        if(haystack.find(needle)==-1):
            return -1
        else:
            i=0
            while(i<len(haystack)):
                if(haystack[i:i+len(needle)]==needle):
                    return i
                i+=1
