###https://leetcode.com/problems/integer-to-english-words/submissions/


class Solution(object):
    def numberToWords(self, num):
        res=''
        count=0
        ins=str(num)
        k1={0:'',1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten',11:'Eleven',12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',17:'Seventeen',18:'Eighteen',19:'Nineteen',20:'Twenty',30:'Thirty',40:'Forty',50:'Fifty',60:'Sixty',70:'Seventy',80:'Eighty',90:'Ninety'}
        if(len(str(num))==1 and num==0):
            return 'Zero'
        def k(n):
            j=str(n)
            ans=''
            i=0
            if(i==0 and len(j)==3):
                ans+=k1[int(j[0])]+' '+'Hundred'
                i+=1
                if(j[i:]!='00'):
                    ans+=' '  
            if(len(j)>0):
                if(int(j[i:])>20):
                    a=int(j[i:])//10
                    b=int(j[i:])%10
                    ans+=k1[a*10]
                    if(b!=0):
                        ans+=' '+k1[b]
                else:
                    ans+=k1[int(j[i:])]
            return ans
        if(len(ins)%3==0):
            b=len(ins)//3
        else:
            b=(len(ins)//3)+1
        while(count<b):
            n=num%1000
            ins1=k(n)
            num=num//1000
            if(count==0 and n!=0):
                res+=ins1
            elif(count==1 and n!=0):
                temp=res
                res=ins1+" "+'Thousand'
                if(temp!=""):
                    res+=" "+temp       
            elif(count==2 and n!=0):
                temp=res
                res=ins1+" "+'Million'
                if(temp!=""):
                    res+=" "+temp
            elif(count==3 and n!=0):
                temp=res
                res=ins1+' '+'Billion'
                if(temp!=""):
                    res+=" "+temp
            count+=1
        return res
