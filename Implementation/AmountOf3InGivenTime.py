'''개인 풀이'''
n = int(input()) # 입력
ocr_3_in_hour = 0 # 한시간에 3이 등장하는 경우의 수
for m in range(60): # ocr_3_in_hour의 값 계산
	for s in range(60):
		ocr_3_in_hour += 1 if '3' in f'{m}{s}' else 0
ans = (n+1) * ocr_3_in_hour + (3600-ocr_3_in_hour if n >= 3 else 0) # n+1(0 포함)만큼 3이 등장하는 경우의 수를 곱하고 3시가 끼어있다면 한시간의 경우의 수에서 3이 등장하는 경우의 수를 뺀 만큼 더함(이미 3의 경우는 더했으므로)
print(ans) # 출력

'''예시 답안'''
# H를 입력받기
h = int(input())

count = 0
for i in range(h + 1):
  for j in range(60):
    for k in range(60):
      # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
        if '3' in str(i) + str(j) + str(k):
          count += 1

print(count)