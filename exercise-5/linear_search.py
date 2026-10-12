values = [14, 7, 22, 9, 7, 31]

Target = 18
Found = False

for result in range(len(values)):
    if values[result] == Target:
        Found = True
        break

if Found:
    print("Found at index:", result)
else:
    print("Target not found")