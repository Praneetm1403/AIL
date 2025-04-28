# Fuzzy Set Operations in Python
def fuzzy_union(A, B):
    return {key: max(A.get(key, 0), B.get(key, 0)) for key in set(A) | set(B)}

def fuzzy_intersection(A, B):
    return {key: min(A.get(key, 0), B.get(key, 0)) for key in set(A) & set(B)}

def fuzzy_complement(A):
    return {key: round(1 - value, 2) for key, value in A.items()}

def is_subset(A, B):
    return all(A.get(key, 0) <= B.get(key, 0) for key in A)

def de_morgan_check(A, B):
    left = fuzzy_complement(fuzzy_union(A, B))
    right = fuzzy_intersection(fuzzy_complement(A), fuzzy_complement(B))
    return left, right, left == right  # Checking (A ∪ B)' == A' ∩ B'

# Read Fuzzy Sets from UserA
def read_fuzzy_set(name):
    n = int(input(f"Enter number of elements in {name}: "))
    fuzzy_set = {}
    for _ in range(n):
        key = input("Enter element name: ")
        value = float(input(f"Enter membership value for {key} (0-1): "))
        fuzzy_set[key] = round(value, 2)
    return fuzzy_set

# Main Execution
print("\nEnter Fuzzy Set A:")
A = read_fuzzy_set("A")
print("\nEnter Fuzzy Set B:")
B = read_fuzzy_set("B")

# Perform Operations
union_result = fuzzy_union(A, B)
intersection_result = fuzzy_intersection(A, B)
complement_A = fuzzy_complement(A)
complement_B = fuzzy_complement(B)

print("\nFuzzy Set A:", A)
print("Fuzzy Set B:", B)
print("\nUnion (A ∪ B):", union_result)
print("Intersection (A ∩ B):", intersection_result)
print("Complement of A (A'):", complement_A)
print("Complement of B (B'):", complement_B)

# Subset Check
if is_subset(A, B):
    print("\nA is a subset of B")
else:
    print("\nA is NOT a subset of B")

# De Morgan's Law Demonstration
left, right, is_valid = de_morgan_check(A, B)
print("\nDe Morgan’s Law Verification:")
print("(A ∪ B)' :", left)
print("A' ∩ B':", right)
print("De Morgan’s Law holds:", is_valid)
