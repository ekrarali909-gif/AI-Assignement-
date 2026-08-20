# Group Anagrams

from collections import defaultdict

def groupAnagrams(strs):
    groups = defaultdict(list)

    for word in strs:
        key = ''.join(sorted(word))
        groups[key].append(word)

    return list(groups.values())

# Input
n = int(input())  # Number of strings
strs = [input().strip() for _ in range(n)]

# Output
result = groupAnagrams(strs)
print(result)