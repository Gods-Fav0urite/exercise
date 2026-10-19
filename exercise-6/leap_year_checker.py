user_input = input("Enter a year: ").strip()
year = int(user_input)

if year % 400 == 0:
    is_leap = True
elif year % 100 == 0:
    is_leap = False
elif year % 4 == 0:
    is_leap = True
else:
    is_leap = False

if is_leap:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

print("\nThe next 3 leap years after this are:")

count = 0
current_year = year + 1

while count < 3:
    if current_year % 400 == 0:
        print(current_year)
        count += 1
    elif current_year % 100 == 0:
        pass  
    elif current_year % 4 == 0:
        print(current_year)
        count += 1
        
    current_year += 1
