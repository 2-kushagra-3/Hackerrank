from itertools import combinations_with_replacement
s,k = input().split()
print('\n'.join(map(''.join,combinations_with_replacement(sorted(s),int(k)))))
