tc = int(input())
for t in range(1,tc+1):
    N= int(input())
    box = list(map(int, input().split()))

    max_len= 0
    for x in range(N):
        cnt  = 0
        for j in range(x+1, N):
            if box[x] > box[j]:
                cnt +=1
        if cnt > max_len:
            max_len = cnt
    print(f'#{t} {max_len}')