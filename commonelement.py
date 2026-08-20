# Find common elements between two arrays

def commonElements(arr1, arr2):
    return list(set(arr1) & set(arr2))

# Input
arr1 = list(map(int, input("Enter first array: ").split()))
arr2 = list(map(int, input("Enter second array: ").split()))

# Output
print(commonElements(arr1, arr2))