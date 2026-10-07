guests = [
    "Favy",
    "Mary",
    "Okeke"
]

def result():
    remaining = len(guests)-1
    for guest in guests:
        print(f"Welcome {guest}, Number of people left: {remaining}")
        remaining -= 1


def late_comer(name):
    guests.append(name)

def merge(arr2):
    guests.extend(arr2)

def cancellation(name):
    guests.remove(name)

# guests.append("Dera")
# guests.extend(["Oluchi", "Godswill", "Marve"])
# guests.remove("Mary")

while True:
    print("1. Add a late comer")
    print("2. Add a new list")
    print("3. Remove a guest")

    action = input()

    if action == '1':
        name = input("Enter a name: ")
        late_comer(name)
        result()
    elif action == '2':
        print("Feature not available")
        result()
    elif action == '3':
        name = input("Enter a name: ")
        cancellation(name)
        result()