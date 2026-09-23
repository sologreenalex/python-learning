# ============================================
# مشروع سجل المنتجات والأسعار (البسيط)
# ============================================

# 1. قائمة تخزين البيانات (List of Dictionaries)
products = []

# 2. دالة إضافة منتج
def add_product(name, price):
    product = {"name": name, "price": price}
    products.append(product)
    print(f"✅ تم إضافة '{name}' بسعر {price} جنيه بنجاح!")

# 3. دالة عرض جميع المنتجات
def show_products():
    if not products:
        print("\n📭 لا توجد منتجات مسجلة حتى الآن!")
        return
        
    print("\n📦 --- قائمة المنتجات المسجلة ---")
    for index, item in enumerate(products, 1):
        print(f"{index}. المنتج: {item['name']} | السعر: {item['price']} جنيه")

# 4. حلقة التحكم الرئيسية بالبرنامج
def main():
    while True:
        print("\n===============================")
        print("🏪 --- نظام سجل المنتجات ---")
        print("1. إضافة منتج جديد")
        print("2. عرض جميع المنتجات")
        print("3. خروج")
        
        choice = input("اختر رقم الخيار (1-3): ")

        if choice == "1":
            name = input("أدخل اسم المنتج: ")
            price = float(input("أدخل سعر المنتج: "))
            add_product(name, price)

        elif choice == "2":
            show_products()

        elif choice == "3":
            print("شكراً لاستخدامك البرنامج. وداعاً!")
            break  # الخروج من حلقة while True

        else:
            print("❌ خيار غير صحيح، يرجى اختيار 1 أو 2 أو 3.")

# تشغيل البرنامج
if __name__ == "__main__":
    main()