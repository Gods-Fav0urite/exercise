def insertion_sort(nums: list) -> tuple:
    comparisons, shifts = 0, 0
    for i in range(1, len(nums)):
        key, j = nums[i], i - 1
        while j >= 0:
            comparisons += 1
            if nums[j] > key:
                nums[j + 1] = nums[j]
                shifts += 1
                j -= 1
            else:
                break
        nums[j + 1] = key
    return comparisons, shifts

if __name__ == "__main__":
    print(f"[5, 2, 4, 1] -> {insertion_sort([5, 2, 4, 1])}") # (6, 5)
    print(f"[1, 2, 3, 4] -> {insertion_sort([1, 2, 3, 4])}") # (3, 0)
    print(f"[4, 3, 2, 1] -> {insertion_sort([4, 3, 2, 1])}") # (6, 6)
    print(f"[]           -> {insertion_sort([])}")           # (0, 0)

    print(f"\n10 Sorted:   {insertion_sort(list(range(1, 11)))}")
    print(f"10 Reversed: {insertion_sort(list(range(10, 0, -1)))}")
    print(f"20 Sorted:   {insertion_sort(list(range(1, 21)))}")
    print(f"20 Reversed: {insertion_sort(list(range(20, 0, -1)))}")

