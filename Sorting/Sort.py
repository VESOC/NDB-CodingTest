array = [7, 5, 0, 9, 3, 1, 2, 6, 4, 8]
result = sorted(array)
print(result)
print(array)
array.sort()
print(array)

kv = [('바나나', 2), ('사과', 5), ('당근', 3)]
def setting(data):
	return data[1]
result = sorted(kv, key=setting)
print(result)