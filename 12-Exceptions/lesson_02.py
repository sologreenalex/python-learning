while True:
    try:
        age = int(input("أدخل عمرك: "))
        print(f"✅ تم القبول! عمرك هو: {age}")
        break  # الخروج من الحلقة فقط بعد إدخال رقم صحيح!
    except ValueError:
        print("❌ خطأ: يرجى كتابة أرقام فقط، حاول مرة أخرى.\n")