nums = [2, 7, 11, 15]
target = 9

# Dictionary to store the number as the key and its index as the value
seen_numbers = {}
result = []

for current_index, current_num in enumerate(nums):
    # Calculate the required complement to reach the target
    complement = target - current_num
    
    # Check if the complement has already been seen
    if complement in seen_numbers:
        result = [seen_numbers[complement], current_index]
        break  # Found the first valid pair, exit the loop
        
    # Otherwise, record the current number and its index
    seen_numbers[current_num] = current_index

print(f"Output: {result}")
