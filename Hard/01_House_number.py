'''T=int(input())
while T>0:
    n=int(input())
    digits=""
    for i in range(1,n+1):
        digits+=str(i)
    print(len(digits))
    T-=1'''


#above one has time complexity another solution could be!
'''T=int(input())
while T>0:
    n = int(input())
    digits = 0
    for i in range(1, n + 1):
        digits += len(str(i))
    print(digits)
    T-=1'''


def finddigits(N):
  num_of_digits=0
  for i in range(1,N,10):
    num_of_digits+=(N-i+1)
  return num_of_digits

T=int(input())
while T>0:
  N=int(input())
  print((finddigits(N))+1)
  T=T-1
