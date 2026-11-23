def fibonacci_even_sum_and_reverse(n: int):
    if n <= 0:
        print("Sequence: ")
        print("Even Sum: 0")
        print("Reversed: ")
        return

    a, b = 0, 1
    
    even_sum = 0
    sequence_str = ""
    reversed_str = ""
    even_breakdown_str = ""

    for i in range(n):
        num_str = str(a)
        if a % 2 == 0:
            even_sum += a
            if even_breakdown_str == "":
                even_breakdown_str += num_str
            else:
                even_breakdown_str += " + " + num_str
        if i == 0:
            sequence_str += num_str
            reversed_str = num_str
        else:
            sequence_str += ", " + num_str
            reversed_str = num_str + ", " + reversed_str
            
        a, b = b, a + b

    print(f"Sequence: {sequence_str}")
    print(f"Even Sum: {even_sum} (which is {even_breakdown_str})")
    print(f"Reversed: {reversed_str}")

if __name__ == "__main__":
    print("--- Test Case: N = 8 ---")
    fibonacci_even_sum_and_reverse(8)
