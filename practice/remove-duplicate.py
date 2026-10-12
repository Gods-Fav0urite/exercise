def remove_duplicates(nums):
    unique_items = []
    for item in nums:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items 
if __name__ == "__main__":
    print(remove_duplicates([1, 2, 2, 3, 4, 4]))  
    print(remove_duplicates([3, 1, 3, 2, 1]))     
    print(remove_duplicates([]))                  

'''
Remove Duplicates
Problem
Given a list, return a new list with duplicates removed. keep the first occurrence of each item and preserve the original order.

constraint: do not use set().

Function Signature
remove_duplicates(nums) -> list

Examples
input	output	why
[1, 2, 2, 3, 4, 4]	[1, 2, 3, 4]	2 and 4 appear twice, only the first of each is kept
[3, 1, 3, 2, 1]	[3, 1, 2]	order follows first appearance, the result is not sorted
[]	[]	nothing to remove
Assumptions
return a new list, don't modify the input
items can be numbers or strings
Hint
build a new list. before adding an item, how can you check whether it's already there?'''