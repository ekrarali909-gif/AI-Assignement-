# Two Sum

def twoSum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        diff = target - num

        if diff in seen:
            return [seen[diff], i]

        seen[num] = i

    return []

# Input
nums = list(map(int, input().split()))
target = int(input())

# Output
print(twoSum(nums, target))