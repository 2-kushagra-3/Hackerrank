from itertools import product
args = list(map(int, input().split()))
print(max([sum([y**2 for y in x])%args[1] for x in product(*[map(int,input().split()[1:]) for _ in range(args[0])])]))