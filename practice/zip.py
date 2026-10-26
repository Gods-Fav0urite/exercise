developers = ["Naomi", "Dario", "Jessica", "Tom"]
ids = [1,2,3,4]

for name, dev_id in zip(developers, ids):
    print(f"Name: {name}")
    print(f"ID: {dev_id}")

even_numbers = []
for num in range(21):
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)

celsius = [0, 10, 20, 30, 40]

def to_fahrenheit(temp):
    return (temp * 9/5) + 32

fahrenheit = list(map(to_fahrenheit, celsius))
print(fahrenheit) 

def calculate_expression(x):
    if x > 0:
        return x**2 + 2*x -1
    else:
        return x**3 - x + 4
print(calculate_expression(3))