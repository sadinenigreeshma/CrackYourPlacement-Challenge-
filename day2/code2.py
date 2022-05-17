###https://www.geeksforgeeks.org/chocolate-distribution-problem/

l=[7, 3, 2, 4, 9, 12, 56]
l.sort()
m=3
mini=100000
for i in range(len(l)-m+1):
    mini=min(mini,l[i+m-1]-l[i])
print(mini)

