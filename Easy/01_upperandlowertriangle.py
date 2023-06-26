#UpperTriangle
def UpperTriangle(mat1,n,m):
  for i in range(n):
    for j in range(m):
      if i>j:
        print("0", end=" ")
      else:
        print(mat1[i][j],end=" ")
    print()
    
    
#LowerTriangle
def LowerTriangle(mat1,n,m):
  for i in range(n):
    for j in range(m):
      if i<j:
        print("0", end=" ")
      else:
        print(mat1[i][j],end=" ")
    print()


def main():
  n,m = map(int,input().split())
  mat1 = []
  for i in range(n):
    mat1.append(list(map(int,input().split())))
  LowerTriangle(mat1,n,m)
  UpperTriangle(mat1,n,m)
    
if __name__ =="__main__":
  main()