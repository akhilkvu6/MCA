import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])
print(arr)
print(arr.shape)

arr = arr.reshape(2, 3)
print(arr)
print(arr.shape)

arr2 = np.array([10, 20, 30, 40])
print(arr2)
print(arr2.shape)

arr2 = arr2.reshape(4, 1)
print(arr2)
print(arr2.shape)

arr = arr.reshape(1, -1)
print(arr)
print(arr.shape)

arr = arr.reshape(-1, 1)
print(arr)
print(arr.shape)

a2 = np.arange(10, 61, 10)
print(a2)
print(a2.shape)

a2 = a2.reshape(1, -1)
print(a2)
print(a2.shape)