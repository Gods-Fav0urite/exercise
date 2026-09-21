students = [
    ["Samuel", 80, 75, 90],
    ["David", 55,60,50],
    ["Mary", 35, 40, 30],
    ["John", 65,70, 68]
]

for student in students:
    name = student[0]

    score1 = student[1]
    score2 = student[2]
    score3 = student[3]

    total = score1 + score2 + score3
    average = total / 3

    if average >= 70:
        score = "A"
    elif average >= 60:
        score = "B"
    elif average >= 50:
        score = "C"
    elif average >= 45:
        score = "D"
    elif average >=40:
        score = "E"
    else:
        score = "F"

    print(f"{name}, Average: {average:.2f}, Grade: {score}")