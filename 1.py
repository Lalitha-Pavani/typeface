def tobase3(n):
    res=''
    while n!=0:
        rem = n%3 
        n = n//3 
        res = str(rem)+res
    return int(res)
 
    
    
num = int(input())
print(tobase3(num))
