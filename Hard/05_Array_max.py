# ARRAY MAX

'''
Arnab is given n integers. Now he can choose a starting index ( i ) and then move to (i + k)th element and continue his journey hopping k
elements each time. Each index has a value arr[i] .Arnab should add the values which he chooses to the index he moves to.
He can stop moving to (i+k) at any time he wishes.
Find the maximum possible value in the array after Arnub stops.

Example if arnab chooses index 5 and k is 4
then the possible sequences are 
5 
5,9
5,9,13
5,9,13,17 etc 

and Arnab will not return with a negative-sum.
Note: Minimum value that sum can have is zero, it should never become negative throughout the calculation.

Input format
First line contains integer t ,no of testcase. 
For each test case :There are two integers n and k 
next line contains n integers

Output format
For each test case print the maximum sum
Constraints:
1<=t<=10
2<=k<=N<=10^4
-10^4<=A[i]<=10^4

Time Limit
1 second

Example
Input
1
5 2
1 2 3 4 5

Output
9

Sample test case explanation
n=5, k=2
Array =1,2,3,4,5

If Arnub starts from i=0, arr[i]=, next step is i+k, i.e index=2,
add at index 2 the value present at previous index,so arr[2]=3+1=4.
From index=2, next step is 2+2=4. Value at index=4, becomes arr[4]+ value present at previous index.
so arr[4]=5+4=9.'''


T=int(input())
while T>0:
    N,K=map(int,input().split())
    arr=list(map(int,input().split()))
    if N==len(arr):
      val=0
      for i in range(0,N,K):
        val+=arr[i]
      print(abs(val))
    T-=1