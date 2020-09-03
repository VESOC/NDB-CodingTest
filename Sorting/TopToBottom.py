n = int(input())
array = [int(input()) for _ in range(n)]
print(sorted(array, reverse=True))

print(sorted([int(input()) for _ in range(int(input()))], reverse=True))