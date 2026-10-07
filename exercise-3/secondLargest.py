def find_second_largest(numbers):
    largest = None
    second_largest = None
    
    for num in numbers:
        if num == largest or num == second_largest:
            continue
            
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
            
    return second_largest if second_largest != float('-inf') else None

print(find_second_largest([10, 5, 8, 20, 15]))  
print(find_second_largest([4, 9, 2, 9, 7]))     
print(find_second_largest([5, 5, 5]))           
