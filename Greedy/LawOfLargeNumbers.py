'''개인 풀이'''
n, m, k = map(int, input().split()) # 조건 입력
nums = list(map(int, input().split())) # 데이터 입력
nums.sort() # 정령
data_set = [nums[-1]]*3 + [nums[-2]] # 연산이 반복될 수열 
result = 0
while True:
	if m > 0: # 연산 수가 남았을 때
		result += sum(data_set) # 수열의 합을 더함
		m -= len(data_set) # 수열의 길이만큼 연산 갯수에서 뺌
	elif m < 0: # 연산 수를 초과하였을때
		result -= sum(data_set[m:]) # 초과한 갯수만큼 수열의 뒤에서부터 총합에서 뺌
		break
	else: # 연산을 다 했을때
		break
print(result) # 출력


'''예시 답안'''
# N, M, K를 공백을 기준으로 구분하여 입력 받기
n, m, k = map(int, input().split())
# N개의 수를 공백을 기준으로 구분하여 입력 받기
data = list(map(int, input().split()))

data.sort() # 입력 받은 수들 정렬하기
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
# 순열의 길이로 나누었을때의 몫
count += m % (k + 1)
# 나누었을때의 나머지 만큼 가장 큰 값이 더해진다

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기
# count가 가장 큰 수의 갯수이므로 남은 갯수가 두번째로 큰 수

print(result) # 최종 답안 출력