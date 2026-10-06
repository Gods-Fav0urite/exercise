def step(largest: float, second_largest: float, x: int) -> tuple[float, float]:
    """Pure state machine step updating the top two largest unique numbers."""
    if x > largest:
        return (x, largest)
    elif x < largest and x > second_largest:
        return (largest, x)
    return (largest, second_largest)


def second_largest(nums: list[int]) -> float | None:
    """Finds the second-largest unique element using a single loop and step()."""
    large = float('-inf')
    second = float('-inf')
    
    for x in nums:
        large, second = step(large, second, x)
        
    return second if second != float('-inf') else None

numbers = [4, 9, 2, 9, 7]
result = second_largest(numbers)
print(f"Output: {result}")
