import numpy as np

A = np.ones((5, 6))
print("Ones matrix: \n", A, "\n")
B = np.zeros((5, 6))
print("Zeroes matrix: \n", B, "\n")
res = np.concatenate((A, B))
print("concatenate: \n", res, "\n")

# shaping
shaped = np.array([1, 2, 3, 4, 5, 6, 7, 8])
shaped = shaped.reshape(4, 2)
shaped = shaped.reshape(2, -1)
shaped = shaped.ravel()
print("shaped Array: \n", shaped)

arr = np.arange(1, 200)
print("range array: ", arr)
sqrts = np.sqrt(arr)
print("sqrts of arr: ", sqrts)
