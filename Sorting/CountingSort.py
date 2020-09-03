'''계수 정렬-어떤 원소의 갯수를 샌 다음 출력'''
array = [7, 5 ,9 , 3, 1, 6, 2, 1, 9, 4, 8, 0, 5, 2]
count = [0]*(max(array)+1)
for i in range(len(array)):
	count[array[i]] += 1
for i in range(len(count)):
	for j in range(count[i]):
		print(i, end=' ')
'''개인 풀이'''
count = [0]*(max(array)+1)
for i in array:
	count[i] += 1
for idx, i in enumerate(count):
	print(f'{idx} '*i, end='')