def factorial(n):
	res = 1
	for i in range(2, n+1):
		res *= i 
	return res

def factorial_recur(n):
	if n == 1:
		return n
	else:
		return n * factorial_recur(n-1)

print(factorial(5))
print(factorial_recur(5))