tc = int(input())
for t in range(1,tc+1):
    lst= list(map(int, input().strip()))
    check = [0]*10
    for num in lst:
        check[num] += 1
    row = 0
    trip = 0
    i =0
    while i < 10:
        if check[i] >=3:
            check[i] -= 3
            trip += 1
            continue
        if i <= 7:
            if check[i] >=1 and check[i+1]>=1 and check[i+2]>= 1:
                row +=1
                check[i] -=1
                check[i+1] -=1
                check[i+2] -=1
                continue
        i +=1

    if row+trip ==2:
        print(f'#{t} Baby Gin')
    else:
        print(f'#{t} Lose')