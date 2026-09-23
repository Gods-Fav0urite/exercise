students = [
    ["Samuel", 80, 75, 90],
    ["David", 55, 60, 50],
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

def result():
    print(f"{name}, Average: {average:.2f}, Grade: {score}")

def remove_last():
    students.pop()

def append(insert):
    students.append(insert)

def reverse(insert):
    students.reverse(insert)

while True:
    print("1. Remove last name")
    print("2. Add a list")
    print("3. Reverse a name")

    question = input()

    if question == '1':
        insert = input("Insert a name: ")
        remove_last()
        result()
    elif question == '2':
        insert = input("Add a list: ")
        append(insert)
        result()
    elif question == '3':
        insert = input("Reverse a name: ")
        reverse(insert)
        result()