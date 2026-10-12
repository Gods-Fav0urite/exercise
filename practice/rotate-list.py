def remove_duplicates(nums):
    seen = {}
    for item in nums:
        seen[item] = True
    return list(seen.keys())

def rotate_list(nums, k):
    if not nums:
        return []
    k = k % len(nums)
    return nums[-k:] + nums[:-k]

if __name__ == "__main__":
    print("--- Testing remove_duplicates ---")
    print(remove_duplicates([1, 2, 2, 3, 4, 4]))  
    print(remove_duplicates([3, 1, 3, 2, 1]))    
    print(remove_duplicates([]))                  
    
    print("\n--- Testing rotate_list ---")
    sample_list = [1, 2, 3, 4, 5]
    print(f"Rotate {sample_list} by 2 steps: {rotate_list(sample_list, 2)}")
  

'''
Rotate List
Problem
Given a list and a number k, rotate the list to the right by k positions.

Function Signature
rotate_list(nums, k) -> list

Examples
input	output	why
[1, 2, 3, 4, 5], k=2	[4, 5, 1, 2, 3]	the last 2 items move to the front
[1, 2, 3, 4, 5], k=5	[1, 2, 3, 4, 5]	rotating by the full length returns the same list
[1, 2, 3, 4, 5], k=7	[4, 5, 1, 2, 3]	7 is the same as 2 after one full rotation
[], k=3	[]	nothing to rotate
Assumptions
rotation is to the right
k is a non-negative integer, and may be larger than the list length
return a new list
Hint
what happens to k when it's bigger than the list? which operator wraps a number back into a range? you used it in caesar cipher.'''