def bfs(graph, start_node): #스택을 사용한 bfs탐색
    visited =[]     # 방문기록 생성
    queue =[]   # 스택 생성

    queue.append(start_node)    # 시작 노드를 queue에 저장

    while queue:    # queue안에 노드가 있는 동안
        node = queue.pop(0) # node 지정
        if node not in visited: # 한번도 간적없으면
            visited.append(node)    # 방문기록 남기고
            queue.extend(graph[node])   # node의 value값들을 queue에 추가. 그리고 while문 다시 반복
    return visited

def dfs(graph, start_node): # stack을 이용한 dfs 탐색
    visit ={}   # 방문기록 dictionary로 생성. 이유는 리스트로 하면 아래 21번째 라인에서 시간복잡도 O(n)이 소요. 근데 딕셔너리를 사용해 해시로 구현하면 O(1)로 효율 높일수 있음
    stack = []

    stack.append(start_node)    # 시작 노드를 stack에 추가 해줌
    while stack:    # stack에 노드가 있는동안 반복
        node = stack.pop()  # bfs달리 제일 마지막꺼를 pop해서 node로 지정
        if node not in visit:   # 한번도 간적 없으면
            visit[node] = True  # visit에 저장
            stack.extend(graph[node]) # node의 values들을 stack에 추가 후 반복
    return visit

def dfs(graph, start): # 재귀를 통한 dfs 탐색
   visited[start] = True   # 시작 지점을 방문기록에 남김. 함수 밖에서 미리 visit 생성을 해줘야함. 함수의 매개변수로도 줄 수 있다.
   for node in graph[start]:    # 시작 지점의 values값들만큼 반복. 그 값들 중 한번더 탐색 안한곳은 visit에 기록 후에 그 값들로 다시 함수 실행
        if node not in visited:
            visited[node] = True
            dfs(graph, node)
    return visited



graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}
visited = {}
print(dfs(graph, 'A'))