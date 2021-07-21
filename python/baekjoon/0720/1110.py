T = int(input())


for i in range(1, T+1):
    total = 0
    a = list(map(int, input().split()))
    for d in a:
        if d % 2 == 1:
            total += d
    print("#{} {}".format(i, total))
