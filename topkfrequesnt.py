from collections import Counter


def topKFrequent(nums, k):
    if k <= 0:
        return []

    return [num for num, _ in Counter(nums).most_common(k)]


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    k = int(input())

    print(topKFrequent(nums, k))
