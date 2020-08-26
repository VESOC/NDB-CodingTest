'''개인 풀이'''
n, k = map(int, input().split()) # 입력
cnt = 0
while True:
	if k == 1: # 나누는 수가 1이라면 마이너스 1만 할 수 있으므로 n 출력 후 중단
		print(n)
		break
	if n == 1: # 종료 조건
		print(cnt)
		break
	elif n%k == 0: # k로 나뉘어지면 나눔
		n //= k
		cnt += 1
	else: # 안 나누어지면 1 감소
		n -= 1
		cnt += 1


'''예시 답안'''
# N, K공백을 기준으로 구분하여 입력 받기
n, k = map(int, input().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지만 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
		# result가 n%k로 두면 연산이 더 적음?
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)