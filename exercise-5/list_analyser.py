numbers = [12, 5, 27, 8, 14]

Smallest = numbers[0]
Largest = numbers[0]
Total = 0

for result in numbers:
    if result < Smallest:
        Smallest = result
    if result > Largest:
        Largest = result
    Total += result

Average = Total / len(numbers)

print("Smallest:", Smallest)
print("Largest:", Largest)
print("Total:", Total)
print("Average:", Average)