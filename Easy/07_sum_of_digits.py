#Sum of Digits

'''
your friend gave you a number X and asks you to find the sum of the digits present in the number.

Input format
One integer is provided denoting the value of X.

Output format
Print the sum of digits of X.

Constraints
1<=X<=10^6

Time Limit
1 second

Example
Input
102345

Output
15

Sample test case explanation
Sum of digit  =1+0+2+3+4+5=15'''

N=int(input())
sum=0
while N>0:
    sum+=N%10
    N=N//10
print(sum)