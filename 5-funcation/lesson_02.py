def calculate_tax(price):
    tax = price * 0.15
    return price + tax  # ترجع السعر الإجمالي بعد الضريبة

# استخدام النتيجة المرجعة
final_price = calculate_tax(100)
print(f"السعر النهائي: {final_price}") # سيطبع 115.0