import numpy as np

#dot method

# Example 1
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
result1 = np.dot(A, B)
print("Result 1:\n", result1)

# Example 2
C = np.array([[1, 0, 2], [0, 1, 2]])
D = np.array([[1, 2], [3, 4], [5, 6]])
result2 = np.dot(C, D)
print("Result 2:\n", result2)

# Example 3
E = np.array([[1, 2], [3, 4], [5, 6]])
F = np.array([[1, 2, 3], [4, 5, 6]])
result3 = np.dot(E, F)
print("Result 3:\n", result3)

#transpose method

# Example 1
G = np.array([[1, 2], [3, 4]])
result1 = G.transpose()
print("Transpose 1:\n", result1)

# Example 2
H = np.array([[1, 0, 2], [0, 1, 2]])
result2 = H.transpose()
print("Transpose 2:\n", result2)

# Example 3
I = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result3 = I.transpose()
print("Transpose 3:\n", result3)

#linalg.inv method

# Example 1
J = np.array([[1, 2], [3, 4]])
result1 = np.linalg.inv(J)
print("Inverse 1:\n", result1)

# Example 2
K = np.array([[4, 7], [2, 6]])
result2 = np.linalg.inv(K)
print("Inverse 2:\n", result2)

# Example 3
L = np.array([[1, 1, 1], [0, 2, 5], [2, 5, -1]])
result3 = np.linalg.inv(L)
print("Inverse 3:\n", result3)

#linalg.det method

# Example 1
M = np.array([[1, 2], [3, 4]])
result1 = np.linalg.det(M)
print("Determinant 1:", result1)

# Example 2
N = np.array([[4, 7], [2, 6]])
result2 = np.linalg.det(N)
print("Determinant 2:", result2)

# Example 3
O = np.array([[1, 1, 1], [0, 2, 5], [2, 5, -1]])
result3 = np.linalg.det(O)
print("Determinant 3:", result3)

#flatten method

# Example 1
P = np.array([[1, 2], [3, 4]])
result1 = P.flatten()
print("Flatten 1:", result1)

# Example 2
Q = np.array([[1, 0, 2], [0, 1, 2]])
result2 = Q.flatten()
print("Flatten 2:", result2)

# Example 3
R = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result3 = R.flatten()
print("Flatten 3:", result3)

