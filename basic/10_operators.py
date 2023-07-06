#Operators

'''
your friend wants you to get familiar with various Relational operators. He provides you with two numerical values 
X and Y and your task is to find the relation between them that is,
X is smaller than Y
X is greater than Y
X is equal to Y

Input format
Two space-separated integers are provided denoted by X and Y.

Output format
Print the relation between X and Y.

X is smaller than Y
X is greater than Y
X is equal to Y

Constraints
1<=X,Y<=100

Time Limit
1 second

Example
Input
4 6

Output
4 is smaller than 6

Sample test case explanation
Since 4<6, print 4 is smaller than 6 '''

num1,num2=map(int,input().split())
if num1==num2:
    print(f"{num1} is equal to {num2}")
elif num1<num2:
    print(f"{num1} is smaller than {num2}")
else:
    print(f"{num1} is greater than {num2}")

#or
if num1==num2:
    print("%d is equal to %d"%(num1,num2))
elif num1<num2:
    print("%d is smaller than %d"%(num1,num2))
else:
    print("%d is greater than %d"%(num1,num2))