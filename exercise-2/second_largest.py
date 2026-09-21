def find_second_largest(numbers):

    largest = None
    second_largest = None

    for number in numbers:
        if largest is None or number > largest:
            second_largest = largest
            largest = number
        elif number != largest and (second_largest is None or number > second_largest):
            second_largest = number
    return second_largest

print(find_second_largest([10, 5, 8,20, 15])) 
print(find_second_largest([4, 9, 2, 9, 7]))  