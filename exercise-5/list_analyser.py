numbers = [12, 5, 27, 8, 14]

Smallest = [numbers[0]]  
Largest = [numbers[0]]  
Total = 0

for result in numbers:
    if result < Smallest[0]:
        Smallest[0] = result
    if result > Largest[0]:
        Largest[0] = result
    Total += result

Average = Total / len(numbers)

print("Smallest:", Smallest[0])
print("Largest:", Largest[0])
print("Total:", Total)
print("Average:", Average)