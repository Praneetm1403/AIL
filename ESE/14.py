#Fuzzy Set Operations – De Morgan’s Law (Complement of Intersection)
def fuzzy_intersection(A, B):
    return {x: min(A.get(x, 0), B.get(x, 0)) for x in set(A) & set(B)}

def fuzzy_complement(A):
    return {x: 1 - A[x] for x in A}

# Example fuzzy sets
A = {'x': 0.4, 'y': 0.9}
B = {'x': 0.7, 'y': 0.5}

intersection_AB = fuzzy_intersection(A, B)
complement_intersection = fuzzy_complement(intersection_AB)

print("Complement of Intersection of A and B:", complement_intersection)
