n = int(input())
data = []
for _ in range(n):
	p, q = input().split()
	data.append((p, int(q)))
data.sort(key = lambda x: x[1])
[print(i[0], end=' ') for i in data]
