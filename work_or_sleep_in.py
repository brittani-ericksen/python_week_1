day = int(input('Day (0-6)? '))

if day ==0 or day ==6:
    print("Go to work")
elif day >= 7:
    print("Invalid input")
else:
    print("Sleep in")