#ARRAY ROTATION

'''
your friend has recently heard about something called Array Rotation and wants you to write a code for rotating an array. So what happens in array rotation is, you are given an integer array 
A of size N and an integer K, you have to rotate the array in the right direction by K steps(See test cases for better understanding). The task is to print the rotated array.

Input Format
The first line contains an integer T denoting the number of test cases.Each test case consists of two lines.
The first line contains N, number of elements in the array and K number of steps.
The Second line contains N space-separated integers.

Output Format
For each test case on a new line, print the rotated array.

Constraints
1<=T<=20
1<=N<=10^5
0<=K<=10^6
0<=A[i]<=10^6

Time limit1 second

Example
Input
1
5 2
1 2 3 4 5

Output
4 5 1 2 3

Sample test case explanation
Array = [1 2 3 4 5]
K=2

First right rotation
Array = [5 1 2 3 4]

Second right rotation
Array = [4 5 1 2 3]'''

T=int(input())
while T>0:
    N,K=map(int,input().split())
    arr=list(map(int,input().split()))
    new_arr=[]
    val=0
    for i in range(1,N+1):
        if i<=(N-K):
            new_arr.append(arr[i-1])
        else:
            new_arr.insert(val,arr[i-1])
            val+=1
    print(new_arr)
    T-=1


#or
T=int(input())
while T>0:
    N,K=map(int,input().split())
    arr=list(map(int,input().split()))
    #new_arr=[]
    for i in range(0,K):
        arr.insert(0,arr.pop(-1))
    for i in arr:
        print(i,end=" ")
    print()
    T-=1

#still above one has time complexity
T=int(input())
while T>0:
    N,K=map(int,input().split())
    arr=list(map(int,input().split()))
    val=K%N
    for i in range(0,val):
        arr.insert(0,arr.pop(-1))
    for i in arr:
        print(i,end=" ")
    print()
    T-=1