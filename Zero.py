import numpy as np
dims = input().split()
dims = [int(i) for i in dims]
print(np.zeros(tuple(dims),dtype=np.int))
print(np.ones(tuple(dims),dtype=np.int))