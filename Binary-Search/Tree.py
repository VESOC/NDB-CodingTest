'''
트리(자료구조):
	트리는 부모와 자식 노드로 이루어짐
	최상단 노드는 루트 노드, 최하단 노드는 단말 노드
	계층적이며 정렬된 데이터를 다루는데 적합
	파일 시스템은 대표적인 트리 구조이다
	이진 탐색 트리는 자식노드의 값이 (0, 1, 2) 중 하나
		왼쪽 노드 < 부모 노드 < 오른쪽 노드 형태이다
		가장 작은 노드는 왼쪽 최하단, 가장 큰 노드는 오른쪽 최하단
	이진 탐색 트리는 중복 값이 없다
'''
class Node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data
	
	def insert(self, data):
		if self.data: # 부모 노드가 존재한다면
			if data < self.data: # 부모 노드보다 작으면
				if self.left is None: # 더 작은 노드가 없을 때
					self.left = Node(data)
				else: # 더 작은 노드가 있을 때
					self.left.insert(data)
			elif data > self.data: # 부모 노드보다 크면
				if self.right is None: # 더 큰 노드가 없을 때
					self.right = Node(data)
				else: # 더 큰 노드가 있을 때
					self.right.insert(data)
		else: # 부모 노드가 없으면
			self.data = data

	def PrintTree(self):
		if self.left:
			self.left.PrintTree()
		print(self.data, end=' ')
		if self.right:
			self.right.PrintTree()
	'''
	이진 탐색을 가능하게 하는 코드
		최대한 작은 값을 찾을때까지 왼쪽으로 내려간다
		만약 타겟이 값보다 크다면 오른쪽으로 내려간다
		값이 같다면 출력
		값을 못 찾을 경우:
			찾아야하는 값이 현재 값보다 작은데 왼쪽 노드가 없거나
			현재 값보다 큰데 오른쪽 노드가 없을때
	'''
	def findval(self, val):
		if val < self.data: # 값이 더 작으면
			if self.left is None: # 현재 노드가 가장 작은 값이면
				return str(val) + ' Not Found'
			return self.left.findval(val) # 더 작은 값이 있으면
		elif val > self.data: # 값이 더 크다면
			if self.right is None: # 더 큰 값이 없다면
				return str(val) + ' Not Found'
			return self.right.findval(val) # 더 큰 값이 있다면
		else:
			return str(self.data) + ' is Found' # 값을 찾으면


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

print(root.findval(7))
print(root.findval(14))

root.PrintTree()
print()
'''완성된 트리 모습
    12
  6   14
3
'''