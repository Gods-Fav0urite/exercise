def stats(nums):
    if not nums:
        return None

    smallest = largest = nums[0]
    total = 0

    for x in nums:
        if x < smallest:
            smallest = x
        if x > largest:
            largest = x
        total += x

    return (smallest, largest, round(total / len(nums), 2))

print(stats([4, 9, 2, 7]))