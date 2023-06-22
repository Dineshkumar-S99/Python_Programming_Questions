#FIT SQUARE

'''
Your friend provided you with a rectangular board of M x N dimension. Also, he provided an unlimited number of small blocks of 2x1
size. You are allowed to rotate the block. You are asked to place as many blocks as possible on the board to meet the following conditions:
1. Each block completely covers two squares.
2. No two blocks overlap.
3. Each block lies entirely inside the board. It is allowed to touch the edges of the board.
Find the maximum number of blocks, which can be placed under these restrictions.

Input format
The first line contains an integer 
T denoting the number of test cases.In each of the next T lines, you are given two integers M and N

Output format
Print the maximal number of blocks, which can be placed.

Constraints
1<=T<=15
1≤M≤N≤16

Example
Input
1
2 5

Output
5
'''



T = int(input())
for _ in range(T):
  M, N = map(int, input().split())
  total_squares = M * N
  if total_squares % 2 != 0:
    total_squares -= 1
    max_blocks = total_squares // 2
  print(max_blocks)