from collections import deque

r = [-1, 1, 0, 0]
c = [0, 0, -1, 1]

def bfs(sy,sx):
    visited = [[0]*N for _ in range(N)]
    queue = deque()
    queue.append((sy,sx))
    visited[sy][sx] = 1


    while queue:
        y, x = queue.popleft()
        for t in range(4):
            ny = y + r[t]
            nx = x + c[t]
            if ny >= 0 and ny<N and nx>=0 and nx<N and visited[ny][nx] ==0:
                if M[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x]+1
                    queue.append((ny,nx))
                elif M[ny][nx] == 1:
                    continue
                elif M[ny][nx] == 2:
                    return visited[y][x]
    return 0



T = int(input())
for t in range(1, T+1):
    N = int(input())
    M = [list(map(int, input())) for _ in range(N)]
    ans = 0
    for y in range(N):
        for x in range(N):
            if M[y][x] == 3:
                ans = bfs(y,x)
    if ans == 0:
        pass
    else:
        ans -=1
    print("#{} {}".format(t,ans))
