'''
DFS(깊이 우선 탐색):
	탐색 알고리즘
	-어떤 경로를 탐색중 조건이 맞으면 현재 갈 수 있는 가장 깊은 노드를 방문한 후 다시 원위치로 돌아가 경로 탐색을 재개
	스택 자료구조 사용
	과정:
		시작 노드를 스택에 삽입 -> 방문 처리
		스택의 최상단 노드에 방문하지 않은 인접 노드가 존재하면 해당 노드를 스택에 넣음 -> 방문 처리 -> 방문하지 않은 인접 노드가 없으면 스택의 최상단 노드를 꺼냄
		위의 과정을 실행하지 못 할때까지 실행
		-낮은 순서부터 처리(관행) 
'''

'''인접 행렬(Adjacency Matrix)'''
INF = 999999999

graph_m = [
	[0, 7, 5],
	[7, 0, INF],
	[5, INF, 0]
]

print(graph_m)

# 데이터 소모 상, 노드 연결 상태 속도 상

'''인접 리스트(Adajcency List)'''
graph_l = [[] for _ in range(3)]

graph_l[0].append((1, 7))
graph_l[0].append((2, 5))

graph_l[1].append((0, 7))

graph_l[2].append((0, 5))

print(graph_l)

# 데이터 소모 하, 인접 노드 순회 속도 상

'''DFS'''

def dfs(graph, v, visited):
	visited[v] = True # 방문 처리
	print(v, end=' ')

	for i in graph[v]:
		if not visited[i]: # 방문하지 않았을때
			dfs(graph, i, visited) # 더 깊은 노드 탐색

graph = [
	[],
	[2, 3, 8],
	[1, 7],
	[1, 4, 5],
	[3, 5],
	[3, 4], 
	[7], 
	[2, 6, 8],
	[1, 7]
]

visited = [False] * 9

dfs(graph, 1, visited) # 1 2 7 6 8 3 4 5 
