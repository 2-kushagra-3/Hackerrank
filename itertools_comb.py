import itertools

ll, m = input().split()

k = int(m)


for n in range(k):
    for i in itertools.combinations(sorted(ll), n+1):
        print("".join(i))