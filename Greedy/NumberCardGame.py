'''개인 풀이'''
n, m = map(int, input().split()) # 입력
ans = 0
for i in range(n): # 행의 갯수만큼 반복
	data = min(map(int, input().split())) # 해당 행에서 가장 작은 값 저장
	ans = max(data, ans) # data와 현재 답중 더 큰 것을 고름
print(ans) # 출력

'''예시 답안 유사'''
