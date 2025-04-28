#Fuzzy Set Operations – De Morgan’s Law (Complement of Union)
def fuzzy_union(A, B):
    return {x: max(A.get(x, 0), B.get(x, 0)) for x in set(A) | set(B)}

def fuzzy_complement(A):
    return {x: 1 - A[x] for x in A}

# Example fuzzy sets
A = {'x': 0.3, 'y': 0.7}
B = {'x': 0.6, 'y': 0.5}

union_AB = fuzzy_union(A, B)
complement_union = fuzzy_complement(union_AB)

print("Complement of Union of A and B:", complement_union)
