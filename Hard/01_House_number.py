T=int(input())
while T>0:
    n=int(input())
    digits=""
    for i in range(1,n+1):
        digits+=str(i)
    print(len(digits))
    T-=1


#above one has time complexity another solution could be!
