# 06 April 2025

# A Pizza Delivery Program

customer_bill = 0

print("Welcome to Python Pizza Delivery Program!")
pizza_size = input("What Pizza size do you want (S)mall, (M)edium and (L)arge: ").lower()
include_pepperoni = input("Do you want pepperoni on your pizza (Y/N)? ").lower()
extra_cheese_include = input("Lastly do you want extra cheese (Y/N)? ").lower()
            
# Option 2:
if pizza_size == 's':
    customer_bill += 15
elif pizza_size == 'm':
    customer_bill += 20
else:
    customer_bill += 25
    
if include_pepperoni == 'y':
    if pizza_size == 's':
        customer_bill += 2
    else:
        customer_bill += 3
        
if extra_cheese_include == 'y':
    customer_bill += 1

print(f"The total bill is: ${customer_bill}")