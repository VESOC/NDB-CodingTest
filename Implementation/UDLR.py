'''개인 풀이'''
n = int(input()) # 행의 갯수 입력
path = input() # 이동 계획 입력
x, y = 1, 1 # 좌표-x가 열이고 y가 행
for i in path: # 이동 계획에 따라 반복
	if i == 'U': # ----위 
		if y-1 == 0: # 행 감소했을때 범위를 벗어나면 무시
			continue
		else:
			y -= 1
	elif i == 'D': # ----아래
		if y+1 == n: # 행 증가했을때 범위를 벗어나면 무시
			continue
		else:
			y += 1
	elif i == 'L': # ----왼
		if x-1 == 0: # 열 감소했을때 범위를 벗어나면 무시
			continue
		else:
			x -= 1
	elif i == 'R': # ----오
		if x+1 == n: # 열 증가했을때 범위를 벗어나면 무시
			continue
		else:
			x += 1
print(y, x)


'''예시 답안'''
# N 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)