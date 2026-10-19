def find_duplicates(numbers):
    original_order = []
    for num in numbers:
        if num not in original_order:
            original_order.append(num)
            
    counts_dict = {}
    for num in numbers:
        if num in counts_dict:
            counts_dict[num] += 1
        else:
            counts_dict[num] = 1

    duplicates = []
    duplicate_counts = {} 

    for num in original_order:
        if counts_dict[num] > 1:
            duplicates.append(num)
            duplicate_counts[num] = counts_dict[num]

    return duplicates, duplicate_counts

test_1 = [int(x) for x in "1 2 3 2 4 5 1".split()]
test_2 = [int(x) for x in "4 4 4 4".split()]
test_3 = [int(x) for x in "1 2 3 4".split()]
test_4 = [int(x) for x in "10 20 10 30 20".split()]

test_cases = [test_1, test_2, test_3, test_4]

for test in test_cases:
    dup_list, dup_counts = find_duplicates(test)
    print(f"Input: {test} → {dup_list}")
    if dup_counts:
        print(f"  Stretch Dictionary: {dup_counts}")
