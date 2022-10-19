# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

num_shoes = int(input())
sizes = [int(i) for i in input().split()] #2 3 4 5 6 8 7 6 5 18
num_cust = int(input())

d = Counter(sizes)

earn = 0
for i in range(num_cust):
#while(input() != null)    
    req_i = [int(j) for j in input().split()]
    req_i_size = req_i[0]
    if req_i_size in d.keys():
        if d[req_i_size] > 0:
            earn += req_i[1]
            d[req_i_size] -= 1
        
print(earn)        
