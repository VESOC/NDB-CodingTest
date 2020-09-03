'''
BFS(너비 우선 탐색):
	가까운 노드부터 탐색
	큐 자료구조 이용-구현 간단(deque)
	O(N) 탐색 시간
	과정:
		시작 노드를 큐에 삽입 후 방문 처리
		큐에서 노드를 꺼내 인접 노드 중 방문하지 않은 노드 모두 큐에 삽입
		위의 과정을 수행하지 못할 때까지 반복
'''
from collections import deque

def bfs(graph, start, visited):
	queue = deque([start]) # 해당 노드의 인접노드 큐
	visited[start] = True # 현재 노드 방문 처리
	
	while queue: # 인접 노드마다 실행
		v = queue.popleft() # 가장 작은 인접 노드 추출
		print(v, end=' ') # 출력
		for i in graph[v]: # 해당 노드의 인접 노드 마다 실행
			if not visited[i]: # 해당 인접 노드를 방문하지 않았을 시
				queue.append(i) # 인접 노드 큐에 추가
				visited[i] = True # 방문 처리

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

visited = [False] * 8

bfs(graph, 1, visited)