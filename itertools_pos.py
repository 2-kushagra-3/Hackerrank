# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

ll, n = input().split()

for i in itertools.permutations(sorted(ll),int(n)):
    print("".join(i))