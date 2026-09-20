# exmple invoice resturant 
# how to using variables 

restaurant_name="Pizza House"
burger_price=120
fries_price=50
drink_price=30
Tax_rate=0.14
subtotal=burger_price + fries_price +drink_price 
tax=subtotal * Tax_rate
total = subtotal + tax
print(restaurant_name)
print("---------------------")
print(f"Burger Price: {burger_price} EGP")
print(f"Fries Price:{fries_price} EGP")
print(f"Drink Price: {drink_price} EGP")
print("---------------------")
print(f"Subtotal : {subtotal} EGP")
print(f"Tax: {tax} EGP")
print(f"Total : {total} EGP")

