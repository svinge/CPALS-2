import numpy as np

# Taking two 2D array
# For 2-D arrays it is the matrix product
'''a = [[2, 1], [0, 3]]
b = [[1, 1], [3, 2]]'''

# Calculating dot product using dot()


a= [12, 10]
b = [20,10]
c = [15,11]

ab = [8,0]
ac = [3,1]

ba = [-8,0]
bc = [-5,1]


x = np.dot(ab, ac)
y = np.dot(ba, bc)

print(x, y)
