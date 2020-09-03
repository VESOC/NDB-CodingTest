'''
이진 탐색:
	정렬된 데이터에서만 사용 가능
	시작, 중간, 끝점 활용
	중간점의 값과 타겟값을 비교하며 탐색
'''
'''이진 탐색-재귀함수'''
def binary_search(array, target, start, end):
	if start > end:
		return None
	mid = (start + end) // 2
	if array[mid] == target:
		return mid
	elif array[mid] > target:
		return binary_search(array, target, start, mid-1)
	else:
		return binary_search(array, target, mid+1, end)

n, target = map(int, input().split())
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
	print('Target not found.')
else:
	print(result+1)
