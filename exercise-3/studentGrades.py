students = [
    {"name": "Sam", "scores": [80, 90]}, 
    {"name": "David", "scores": [55, 60]}
]

highest_student = None
highest_avg = -1  

lowest_student = None
lowest_avg = 101  

for student in students:
    total_score = 0
    count = 0
    for score in student["scores"]:
        total_score += score
        count += 1
    
    average = total_score / count if count > 0 else 0

    if 70 <= average <= 100:
        grade = "A"
    elif 60 <= average <= 69:
        grade = "B"
    elif 50 <= average <= 59:
        grade = "C"
    elif 45 <= average <= 49:
        grade = "D"
    elif 40 <= average <= 44:
        grade = "E"
    else:
        grade = "F"
        
    print(f"{student['name']} → Average: {average:.2f} → Grade: {grade}")
    
    if average > highest_avg:
        highest_avg = average
        highest_student = student["name"]
        
    if average < lowest_avg:
        lowest_avg = average
        lowest_student = student["name"]

print(f"Highest Performing Student: {highest_student} ({highest_avg:.2f})")
print(f"Lowest Performing Student: {lowest_student} ({lowest_avg:.2f})")
