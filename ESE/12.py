#Fuzzy Set Operations – Union, Intersection, Complement (3 fuzzy sets)
def fuzzy_union(A, B):
    return {x: max(A.get(x, 0), B.get(x, 0)) for x in set(A) | set(B)}

def fuzzy_intersection(A, B):
    return {x: min(A.get(x, 0), B.get(x, 0)) for x in set(A) & set(B)}

def fuzzy_complement(A):
    return {x: 1 - A[x] for x in A}

# Example fuzzy sets
A = {'a': 0.2, 'b': 0.5, 'c': 0.7}
B = {'a': 0.6, 'b': 0.4, 'd': 0.8}
C = {'b': 0.9, 'c': 0.3, 'e': 0.5}

print("Union of A and B:", fuzzy_union(A, B))
print("Intersection of A and B:", fuzzy_intersection(A, B))
print("Complement of A:", fuzzy_complement(A))
