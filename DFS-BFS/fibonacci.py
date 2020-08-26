fibo = [0, 1, 1]
def fibonacci(n):
	global fibo
	if n < 0:
		return 0
	if n > len(fibo)-1:
		fibo.append(fibonacci(n-1) + fibonacci(n-2))
	return fibo[n]

print(fibonacci(10))
print(fibo)