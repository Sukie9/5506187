from itertools import product

# Read the input lists
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Compute the Cartesian product of A and B
cartesian_product = list(product(A, B))

# Output the space-separated tuples of the Cartesian product
for item in cartesian_product:
    print(item, end=" ")