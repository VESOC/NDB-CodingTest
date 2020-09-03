'''개인 풀이'''
n, m = map(int, input().split())
mold = [list(map(int, input())) for _ in range(n)]

def dfs(x, y):
	global mold # 전역 변수-얼음 틀
	if x == n or x < 0 or y == m or y < 0: # 배열 밖으로 갈 경우
		return False
	
	if mold[x][y] == 0: # 해당 좌표를 방문하지 않았을때-dfs를 수행해 연결된 모든 좌표 확인
		mold[x][y] = 1 # 방문처리
		dfs(x+1, y)
		dfs(x-1, y)
		dfs(x, y+1)
		dfs(x, y-1)
		return True # 해당 좌표에 대한 True 반환
	return False # 이미 방문했다면 False 반환

cnt = 0
for i in range(n):
	for j in range(m):
		if dfs(i, j) == True: # 해당 좌표가 방문되지 않았을때
			cnt += 1

print(cnt) # 출력

'''예시 답안 복사'''