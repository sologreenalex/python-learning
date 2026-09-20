#store code 

product_name="Keyboard"
price=float(input("Enter Product Price :"))
quantity=float(input("Enter Product Quantity : "))
tax_rate=0.14
subtotal=price * quantity
tax=subtotal * tax_rate
total=subtotal + tax

print(f"Product Name : {product_name} ")
print(f"Price : {price:.2f}")
print(f"Quantity: {quantity}")
print(f"tax rate : {tax_rate * 100:.0f}")
print(f"subtotal: {subtotal:.2f}")
print(f"Tax {tax:.2f}")
print(f"Total {total}")

