num = -987

sign = -1 if num < 0 else 1
remaining_digits = abs(num)

reversed_num = 0

while remaining_digits > 0:
    last_digit = remaining_digits % 10
    reversed_num = (reversed_num * 10) + last_digit
    remaining_digits = remaining_digits // 10


final_result = sign * reversed_num

print(f"Output: {final_result}")
