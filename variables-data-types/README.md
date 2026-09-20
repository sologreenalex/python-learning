# 📝 تمارين على المتغيرات ودمج النصوص (Variables & String Formatting in Python)

مشروع تطبيقي بسيط بلغة Python يهدف إلى التدرب على إنشاء المتغيرات من أنواع بيانات مختلفة واستخدام نصوص formatted string (`f-strings`) لتنسيق ودمج النصوص والمخرجات بطريقة منظمة.

---

## 🎯 المفاهيم المطبقة في المشروع

- **المتغيرات (Variables):** تخزين البيانات واستدعاؤها بسهولة.
- **أنواع البيانات (Data Types):**
  - النصوص (`str`): مثل `name` و `city`.
  - الأرقام الصحيحة (`int`): مثل `age` و `weight` و `future_age`.
  - القيم المنطقية (`bool`): مثل `is_job`.
- **دمج النصوص (f-strings):** دمج المتغيرات والعمليات الحسابية المباشرة داخل النصوص بطريقة احترافية وعصرية.
- **العمليات الحسابية البسيطة:** حساب العمر المستقبلي مباشرة داخل عبارة الطباعة `(age + future_age)`.

---

## 💻 كود المشروع (main.py)

```python
name = "aymen"
age = 49
city = "Alexandria"
weight = 110
is_job = True
future_age = 5

print(f"My Name is : {name} , I am {age} years old , I live in {city} , my weight is {weight}, Yes I have Job {is_job}, After 5 years my age is {age+future_age}")
```

---

## 📤 المخرجات المتوقعة (Output)

```text
My Name is : aymen , I am 49 years old , I live in Alexandria , my weight is 110, Yes I have Job True, After 5 years my age is 54
```

---

## 🚀 كيفية التشغيل

1. تأكد من تثبيت بيئة **Python 3**.
2. قم بتشغيل الملف عبر سطر الأوامر (Terminal):
   ```bash
   python main.py
   ```
