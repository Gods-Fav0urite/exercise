def find_two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                # return [numbers[i], numbers[j]]
                return i, j

print(find_two_sum([2, 7, 11, 15], 9))   
print(find_two_sum([3, 8, 4, 6], 10)) 