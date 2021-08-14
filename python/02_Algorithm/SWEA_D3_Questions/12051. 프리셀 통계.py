T = int(input())
for t in range(1, T + 1):
    N, PD, PG = map(int, input().split())
    ans = 'Possible'
    if (PD != 100 and PG == 100) or (PD != 0 and PG == 0):
        ans = 'Broken'
    elif N < 100:
        for i in range(1, N + 1):
            if (PD *i)%100==0:
                break
        else:
            ans= "Broken"
    print(f'#{t} {ans}')