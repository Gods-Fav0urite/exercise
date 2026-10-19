numbers = [12, 5, 27, 8, 14, 27, 3]
Smallest = numbers[0]
Smallest_index = 0
Largest = numbers[0]
Largest_index = 0
Total = 0

for result in range(len(numbers)):
    number = numbers[result]
    Total += number

    if number < Smallest:
        Smallest = number
        Smallest_index = result

    if number > Largest:
        Largest = number
        Largest_index = result
    # Total += number
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
Average = Total / len(numbers)

Above_average = 0
for number in numbers:
    if number > Average:
        Above_average += 1

print(f"Input List: {numbers}")
print(f"Smallest: {Smallest} (at indext {Smallest_index})")
print(f"Largest: {Largest} (at index {Largest_index})")
print(f"Total: {Total}")
print(f"Average: {Average:.2f}")
print(f"Numbers above average: {Above_average}")