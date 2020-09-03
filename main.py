class Node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data
	
	def insert(self, data):
		if self.data:
			if data < self.data:
				if self.left is None:
					self.left = Node(data)
				else:
					self.left.insert(data)
			elif data > self.data:
				if self.right is None:
					self.right = Node(data)
				else:
					self.right.insert(data)
		else:
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
		if val < self.data:
			if self.left is None:
				return str(val) + ' Not Found'
			return self.left.findval(val)
		elif val > self.data:
			if self.right is None:
				return str(val) + ' Not Found'
			return self.right.findval(val)
		else:
			return str(self.data) + ' is Found'


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

print(root.findval(7))
print(root.findval(14))

root.PrintTree()
print()
'''
    12
  6   14
3
'''