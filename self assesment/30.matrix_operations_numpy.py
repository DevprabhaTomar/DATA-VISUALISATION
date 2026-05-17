import numpy as np

# Create two matrices
A = np.array([[2, 4],
              [6, 8]])

B = np.array([[1, 3],
              [5, 7]])

print("Matrix A:\n", A)
print("\nMatrix B:\n", B)

# Addition
add = A + B
print("\nAddition:\n", add)

# Subtraction
sub = A - B
print("\nSubtraction:\n", sub)

# Multiplication (Matrix multiplication)
mul = np.dot(A, B)
print("\nMatrix Multiplication:\n", mul)

# Inverse (only for square matrix with non-zero determinant)
try:
    inv_A = np.linalg.inv(A)
    print("\nInverse of A:\n", inv_A)
except np.linalg.LinAlgError:
    print("\nInverse of A not possible")

try:
    inv_B = np.linalg.inv(B)
    print("\nInverse of B:\n", inv_B)
except np.linalg.LinAlgError:
    print("\nInverse of B not possible")