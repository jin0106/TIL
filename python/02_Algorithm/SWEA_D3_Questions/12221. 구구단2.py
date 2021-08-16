T = int(input())
for t in range(1,T+1):
    A, B = map(int, input().split())
    if A >9 or B>9:
        print(f'#{t} -1')
    else:
        print(f'#{t} {A*B}')