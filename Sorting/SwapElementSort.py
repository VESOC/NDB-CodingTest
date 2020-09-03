n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for _ in range(k):
	if min(a) < max(b):
		a[a.index(min(a))], b[b.index(max(b))] = b[b.index(max(b))], a[a.index(min(a))]
	else:
		break
print(sum(a))