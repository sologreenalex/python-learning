#سنأخذ قيمة المشتريات من المستخدم:
subtotal=float(input("Enter Subtotal :"))
if subtotal >=3000:
    discount_rate=0.20
elif subtotal >=2000:
    discount_rate=0.15   

  
elif subtotal >=1000:
    discount_rate=0.10


    
else:
    discount_rate=0    
discount=subtotal * discount_rate
total=subtotal -discount    
print(f"SubTotal: {subtotal:.2f}")
print(f"Discount:{discount}")
print(f"Total:{total}")
   
