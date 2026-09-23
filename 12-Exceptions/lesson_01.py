try:
    age = int(input("أدخل عمرك: "))
    print(f"عمرك هو: {age}")
except ValueError:
    print("❌ خطأ: يرجى إدخال رقم صحيح وليس حروفاً!")
    