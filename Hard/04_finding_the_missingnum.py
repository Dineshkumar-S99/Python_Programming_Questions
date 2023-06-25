T = int(input())
while T>0:
    N = int(input())
    arr = list(map(int, input().split()))
    
    total_xor = 0 
    for i in range(1, N+1):
        total_xor ^= i
    
    array_xor = 0 
    for num in arr:
        array_xor ^= num
    
    missing_number = total_xor ^ array_xor
    print(missing_number)