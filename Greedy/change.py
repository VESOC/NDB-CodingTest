'''개인 풀이'''
money = int(input()) # 거스름돈 입력
amt_of_coin = 0 # 동전의 갯수
type_of_coins = [500, 100, 50, 10] # 동전의 종류

for c in type_of_coins: # 동전의 종류 별로 반복
	amt_of_coin += money//c # 해당 종류로 거스를 수 있는 최대 갯수만큼 동전의 갯수에 더함
	money %= c # 해당 종류로 거스르고 남은 거스름돈

print(amt_of_coin) # 동전의 갯수 출력

'''예시 답안 동일'''