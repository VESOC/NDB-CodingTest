'''개인 풀이'''
n = int(input())
path = input()
x, y = 1, 1
for i in path:
	if i == 'U':
		if y-1 == 0:
			continue
		else:
			y -= 1
	elif i == 'D':
		if y+1 == n:
			continue
		else:
			y += 1
	elif i == 'L':
		if x-1 == 0:
			continue
		else:
			x -= 1
	elif i == 'R':
		if x+1 == n:
			continue
		else:
			x += 1
print(y, x)