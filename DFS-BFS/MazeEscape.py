'''개인 풀이'''
from collections import deque # 덱 자료구조 

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

def bfs(x, y):
	global maze
	q = deque() # 덱/큐 생성
	q.append((x, y)) # 시작 인덱스(본 프로그램에서는 0,0으로 시작해도 됨)
	dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 상하좌우 이동 계획
	while q:
		x, y = q.popleft() # 현재 위치
		for i in range(4):
			cx, cy = x + dx[i] , y + dy[i] # 상하좌우 이동
			if 0 <= cx < n and 0 <= cy < m: # 미로 범위 내
				if maze[cx][cy] == 1: # 아직 방문하지 않았다면
					maze[cx][cy] = maze[x][y] + 1 # 직전의 좌표까지의 거리에 1을 더함
					if cx == n-1 and cy == m-1: # 만약 도착지점에 도달하면 더 이상의 코드실행을 멈추고 도착지점의 값을 반환
						return maze[-1][-1]
					q.append((cx, cy)) # 현재 위치를 큐에 저장
	return maze[-1][-1] # 도착 지점의 거리 반환

print(bfs(0,0)) # BFS 실행 및 결과 출력

'''예시 답안 복사'''