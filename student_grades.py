students = [
    ["Samuel", 80, 75, 90],
    ["David", 55, 60, 50],
    ["Mary", 35, 40, 30],
    ["John", 65, 70, 68],
    ["Favour", 20, 40, 80]
]

for student in students:
    name = student[0]
    scores = student[1:]  
    total_score = 0
    score_count = 0
    for score in scores:
        total_score += score
        score_count += 1
        
    average = total_score / score_count
    
    if average >= 70:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 50:
        grade = "C"
    elif average >= 45:
        grade = "D"
    elif average >= 40:
        grade = "E"
    else:
        grade = "F"
        
    print(f"{name} - Average: {average:.2f} - Grade: {grade}")
