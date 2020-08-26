'''개인 풀이'''
coord = input() # 입력
x, y = ord(coord[0]) - ord('a')+1, int(coord[1]) # 행과 열 저장(최소가 1이므로 x에 1을 더함)
res = 0 # 결과값
outcome = [
	(2, 1), (2, -1), (-2, 1), (-2, -1),
	(1, 2), (1, -2), (-1, 2), (-1, -2)
] # 나이트가 갈 수 있는 이동 계획
for i in outcome: # 이동 계획마다 반복
	dx, dy = x + i[0], y + i[1] # 해당 계획 실행
	if dx < 1 or dy < 1 or dx > 8 or dy > 8: # 체스판을 벗어나면 해당 반복 무시
		continue
	else: # 체스판 안이면 증가
		res += 1

print(res) # 출력


'''예시 답안 유사'''