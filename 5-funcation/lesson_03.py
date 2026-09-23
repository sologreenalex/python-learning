def usd_to_egp(dollars):
    rate=52
    resuelt=dollars * rate
    return resuelt
total_egp=usd_to_egp(10)
print(total_egp)



def gold_price(weight_gold):
    price_today=7135
    charge=100
    resuelt=price_today + charge * weight_gold
    return resuelt
total_gold=gold_price(5)
print(total_gold)


def sar_to_egp(ser):
    reate=13
    total=ser * reate
    return total

# 1. الدالة التي كتبتها أنت (ممتازة!)
def sar_to_egp(sar):
    rate = 13
    total = sar * rate
    return total

# 2. حلقة while True لاستمرار البرنامج
while True:
    user_input = input("أدخل المبلغ بالريال السعودي (أو اكتب exit للخروج): ")
    
    # شرط الخروج من الحلقة
    if user_input == "exit":
        print("شكراً لاستخدامك البرنامج. وداعاً!")
        break
    
    # تحويل النص المدخل إلى رقم
    sar_amount = float(user_input)
    
    # استدعاء دالتك وحساب النتيجة
    result = sar_to_egp(sar_amount)
    print(f"💵 {sar_amount} ريال = {result} جنيه مصري\n")
    
