values = [14, 7, 22, 9, 7, 31, 7, 5]
Target = 18
Indices = []
Count = 0
first_index = None
last_index = None

for value in range(len(values)):
    if values[value] == Target:
        Indices.append(value)
        Count += 1

        if first_index is None:
            first_index = value
        last_index = value

if Count > 0:
    print(f"Target: {Target} → Found at index: {Indices} | Count: {Count} | First: {first_index} | Last: {last_index}")
else:
    print(f"Target: {Target} → Target not found")
