#Print Float Numbers

'''
You are given two float numbers N and M. You have to print both numbers N and M separated by a space.

Note:- Print the output till 2 digits after decimal point.

Input Format
The first line of input contains two float numbers N and M.

Output Format
Print both the number N and M separated by a space. 

Constraints
1<=N,M<=100

Time Limit 0.5 second

Example
Sample Input
10.20 2.35

Sample Output
10.20 2.35
'''

N,M,ch=input().split()
N=int(N)
M=float(M)
print("%d$%.2f$%c"%(N,M,ch))