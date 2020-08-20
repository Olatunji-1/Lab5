import numpy as np

# Use Broadcasting to create a 4 x 4 ndarray that has its first
# column full of 1s, its second column full of 2s, its third
# column full of 3s, etc.. 

x = np.arange(4).reshape(4,1)
y = np.ones(5)

broadcast = x + y
print(broadcast)

