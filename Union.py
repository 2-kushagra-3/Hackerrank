n = int(input())
A = set(map(int, input().split()))
m = int(input())
B = set(map(int, input().split()))

ans = A.union(B)
print(len(ans))