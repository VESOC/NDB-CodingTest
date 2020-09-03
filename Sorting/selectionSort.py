'''선택 정렬-가장 작은 것을 골라 정렬'''
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
	min_id = i
	for j in range(i+1, len(array)):
		if array[min_id] > array[j]:
			min_id = j
	array[i], array[min_id] = array[min_id], array[i]
print(array)