def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Execution Pipeline
numbers_list = [2, 7, 11, 15]
target_value = 9
print(f"Output: {two_sum(numbers_list, target_value)}")
