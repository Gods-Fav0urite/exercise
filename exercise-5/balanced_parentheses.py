text = "(a + b) * (c - d)"

balanced_num = 0
is_balanced = True

for char in text:
    if char == '(':
        balanced_num += 1
    elif char == ')':
       balanced_num -= 1

    if balanced_num < 0:
        is_balanced = False
        break
if is_balanced and balanced_num == 0:
    print("Balanced")
else:
    print("Not Balanced")