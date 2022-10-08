import itertools
A = list(map(int,input().split()))
B = list(map(int,input().split()))

p = list(itertools.product(A,B))
print(" ".join(map(str,p)))