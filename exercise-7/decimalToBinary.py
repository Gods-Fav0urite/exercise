num = int(input("Enter a positive integer: "))

if num == 0:
    binary_str = "0"
else:
    binary_str = ""
    while num > 0:
        remainder = num % 2
        binary_str = str(remainder) + binary_str
        
        num = num // 2
print("Binary output:", binary_str)
