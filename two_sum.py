# Problem Statement: Given array of numbers find two the position of two numbers whose sum equals to target sum
def two_sum(nums, target):
    result = {}
    for i, n in enumerate(nums):
        if n in result.keys():
            return i, result[n]
        else:
            result[target - n] = i
    return None


nums = [1, 2, 4, 5, 6]
target = 10
print(two_sum(nums, target))
target = 20
print(two_sum(nums, target))
target = 1
print(two_sum(nums, target))

# Note: Array Index starts from 0
