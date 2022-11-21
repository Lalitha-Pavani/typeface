def findLastOccur(s1,s2):
    lastc = s2[-1]
    count=0
    for ch in s1:
        if ch==lastc:
            count+=1 
    return count

s1 = input()
s2 = input()
print("Number of occurence of ",s2[-1]," in",s1," is",findLastOccur(s1,s2))
