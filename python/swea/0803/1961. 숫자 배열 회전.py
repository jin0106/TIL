

def rotate(arr):
    new_list = [[0]*t for _ in range(t)]

    for j in range(t):
        for x in range(t):
            new_list[j][x] = arr[t-x-1][j]

    return new_list


T = int(input())
for i in range(1, T+1):
    t = int(input())
    my_list = [list(map(int, input().split()))for _ in range(t)]
    a = rotate(my_list)
    b = rotate(a)
    c = rotate(b)

    print(f'#{i}')
    for j in range(t):
        print(''.join(map(str, a[j])), ''.join(
            map(str, b[j])), ''.join(map(str, c[j])))
