# BIRTHDAY GIFT

'''
Abhishek and Gaurav are the best friends, today is Gaurav's birthday, but Abhishek forgot to buy a gift for him. Gaurav is very angry with him. Abhishek has an idea for a gift. 
Gaurav likes coding very much. So Abhishek gave him a problem to solve as his gift. Gaurav likes everything infinitely. Abhishek gave him a sequence problem, such that its first element is equal to 
A(S1=A), and the difference between any two adjacent elements is (Si - Si−1 = C. In particular, Gaurav wonders if his favorite integer B
appears in this sequence, that is, there exists a positive integer i, such that Si = B. Gaurav is busy at his birthday party, he asks you to solve this problem.
 
Input Format
The first line contains an integer T denoting the number of test cases.
In the first line of each test case, the input contains three integers A, B and C. 
A is the first element of the sequence, B is Gaurav’s favorite number and the C is the difference between any two adjacent elements of the sequence, respectively.

Output Format
If B appears in the sequences print YES, otherwise print NO. '''

'''
Read the number of test cases (T) from the input.

Iterate over the test cases:
Read the values of A, B, and C from the input.
If C is 0, check if A is equal to B. If true, print "YES"; otherwise, print "NO" and move to the next test case.
If C is not 0:
Calculate the difference between B and A: diff = B - A.
If diff is divisible by C and the result is non-negative, print "YES"; otherwise, print "NO".'''


def birthday_gift(A,B,C):
    if C==0 and A==B:
        return "Yes"
    else:
      if (B - C)%C==0 and (B-C)//C>=0:
         return "Yes"
      return "No"
    
T=int(input())
while T>0:
   A,B,C=map(int,input().split())
   print(birthday_gift(A,B,C))
   T-=1