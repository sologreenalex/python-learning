# إنشاء قاموس
student = {
    "name": "أحمد",
    "age": 22,
    "grade": "ممتاز"
}

# الوصول لقيمة عبر المفتاح
print(student["name"])  # أحمد

# إضافة أو تعديل قيمة
student["age"] = 23
student["city"] = "القاهرة"

# المرور على المفاتيح والقيم
for key, value in student.items():
    print(f"{key}: {value}")