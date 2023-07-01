# Noble Vowel

'''
Given a string S your task is to find out whether a string is Noble Vowel string or not. 
A Nobel Vowel string is one in which there has to be a vowel after every consonant, 
but there can be any letter after any vowel. The only exception is a consonant n; 
after this letter, there can be any letter (not only a vowel) or there can be no letter at all.

Input format
The first line contains an integer T denoting the number of test cases.
Each test case consists of one string S consisting of lower case alphabets.

Output format
For each test case on a new line print YES if S is a Noble Vowel string else print NO.

Constraints:
1<=T<=10
1<=|S|<=1000

Time Limit
1 second

Example
Input
2
aeiou
cefduo

Output
YES
NO

Explanation
In the first string, every vowel is followed by another vowel or consonant. So the string is Noble Vowel.
In the second string, f is a consonant, which should be followed by a vowel but it is being followed by another consonant, so this string is not Noble Vowel.'''

'''T=int(input())
vowels=["a","e","i","o","u"]
while T>0:
    S=input().lower()
    val=0
    for i in range(len(S)):
        if S[i] not in vowels:
            if len(S)==1:
                print("YES")
            if i<(len(S)-1) and S[i+1] not in vowels:
                print("NO")
                break
        else:
            val+=1
        if i==len(S)-1 and val>0:
            print("YES")
    T-=1'''


T=int(input())
vowels=["a","e","i","o","u"]
while T>0:
    S=input().lower()
    val=0
    for i in range(len(S)):
        if len(S)==1:
            print("YES")
        if S[i] in vowels:
            if i<(len(S)-1) and S[i+1] in vowels:
                print("YES")
                break
        else:
            val+=1
        if i==len(S)-1 and val>0:
            print("YES")
    T-=1