from itertools import combinations
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
lst = [i for i in input().split()]
k = int(input())
a_indxs = {i for i in range(1, n + 1) if lst[i - 1] == 'a'}
a_num = 0
comb_len = 0
for comb in combinations(range(1, n + 1), k):
    comb_len += 1
    if set(comb) & a_indxs:
        a_num += 1
print(a_num / comb_len)