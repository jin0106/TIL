T = int(input())
for t in range(1, T+1):
    A, B = map(int, input().split())
    cnt =0
    for i in range(A, B+1):
        a = (i**0.5)
        if a == int(a):
            a = int(a)
            a = str(a)
            b = str(i)
            if a == a[::-1] and b == b[::-1]:
                cnt+=1
    print(f'#{t} {cnt}')
