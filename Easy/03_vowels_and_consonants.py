# Vowels and Consonants

'''
Let's take a simple problem. We all know what are vowels and consonants. Your task is pretty simple, given a string 
S, count number of vowels and consonants present in the string.

Input format
The first line contains an integer 
T, denoting the number of test cases.
Each test case consists of a string S containing only uppercase characters.

Output format
For each test case on a new line, print vowel count and consonant count separated by a space.

Constraints
1<=T<=15
1<=|S|<=10^7, where |S| denotes length of string S.

Time limit
1 second

Example
Input
2
PREPBYTES
FLY

Output
2 7
0 3
'''


T=int(input())
while T>0:
  given_str=input().lower()
  vowels=0
  consonants=0
  for val in given_str:
    if val=="a" or val=="e" or val=="i" or val=="o" or val=="u":
      vowels+=1
    else:
      consonants+=1
  print(vowels,consonants)
  T-=1