# Angle between the Two hands in an Analogue Watch

#Finds the shortest Angle Formed between two hands

'''
Input format
The first line contains the number of test cases T
Each test case contains two integers h and m representing the time in hour and minute format.

Output format
For each test case on a new line, print the required shorter angle.

Constraints
1<=T<=5
All valid times'''


#first formula
# angle= 30*h - 5.5*m (i.e: 30*12=360 for h and 11/2*min math formula -> 5.5*m)

#but the hour moves for minutes too, if 4.30 the hour hand will be in between 4 and 5 i.e:extra 15 deg

#so will convert hr into min and find them
# formula : (0.5*(60*h+m))-(6*m) 

T=int(input())
if T>=1 and T<=5:
  while T>0:
    h,m=map(int,input().split())
    angle=abs((0.5*(60*h+m))-(6*m))
    diff_angle=min(angle,360-angle)
    print(int(diff_angle))
    T-=1


#using function
def angle_between(h,m):
  angle=abs((0.5*(60*h+m))-(6*m))
  diff_angle=min(angle,360-angle)
  return diff_angle

T=int(input())
h,m=map(int,input())
while T>0:
  print(angle_between(h,m))