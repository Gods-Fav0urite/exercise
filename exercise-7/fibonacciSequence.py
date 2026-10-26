N = int(input("Enter the number of elements:"))
a = 0
b = 1
even_sum = 0
even_str = ""
sequences_str = ""
reversed_str = ""
count = 0

while count < N:
    current_str = str(a)

    if count == 0:
        sequences_str = current_str
        reversed_str = current_str
    else:
        sequences_str = sequences_str + ", " + current_str
        reversed_str = current_str + ", " + reversed_str

    if a % 2 == 0:
        even_sum += a
        if even_str == "":
            even_str = str(a)
        else:
            even_str = even_str + " + " + str(a)

    next_num = a + b
    a = b
    b = next_num
    count += 1
print("Sequence:", sequences_str)
print(f"Even Sum: {even_sum} (which is {even_str})")
print("Reversed:", reversed_str)