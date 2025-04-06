visitor_height = int(input("Enter your height in cm: "))

bill = 0
minimum_height = 120
if visitor_height >= minimum_height:
    print("You're allowed to ride the roller coaster.")
    
    # Check for user age
    visitor_age = int(input("Enter your age: "))
    if visitor_age <= 12:
        bill += 5
        print("The ticket cost $5")
    elif visitor_age <= 18:
        bill += 7
        print("The ticket cost $7")
    elif visitor_age >= 45 or visitor_age <= 55:
        bill += 0
        print("Have a free ride on us!")
    else:
        bill += 12
        print("The ticket cost $12")
    
    # Check if they want an extra photo or not
    extra_photo = input("Do you want a photo for $3 (y/n): ")
    if extra_photo == 'y':
        bill += 3
        print(f"$3 added to the bill, the total is: ${bill}")
    else:
        print(f"The total bill is: ${bill}")
else:
    print("You aren't allowed to ride the roller coaster.")