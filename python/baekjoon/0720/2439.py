N = int(input())
cnt = N-1
for i in range(1, N+1):
    print(" "*cnt+"*"*i)
    cnt -=1
    