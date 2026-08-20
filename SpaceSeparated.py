# Convert a space-separated string to CamelCase

s = input().strip()

words = s.split()
camel_case = ''.join(word.capitalize() for word in words)

print(camel_case)
