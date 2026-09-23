# 1. المخطط (Class)
class BankAccount:
    # دالة التأسيس: تأخذ اسم صاحب الحساب والرصيد المبدئي
    def __init__(self, owner, balance):
        self.owner = owner      # اسم صاحب الحساب
        self.balance = balance  # الرصيد الحقيقي

    # دالة لإيداع مبلغ
    def deposit(self, amount):
        self.balance += amount
        print(f"💵 تم إيداع {amount} جنيه. الرصيد الحالي لـ {self.owner}: {self.balance} جنيه")

    # دالة لعرض تفاصيل الحساب
    def show_balance(self):
        print(f"👤 الحساب: {self.owner} | 💰 الرصيد: {self.balance} جنيه")


# 2. إنشاء كائنين (حسابين مختلفين من نفس المخطط)
account1 = BankAccount("أحمد", 1000)
account2 = BankAccount("سارة", 5000)

# 3. تجربة العمليات
account1.show_balance()  # عرض حساب أحمد
account1.deposit(500)    # إيداع 500 في حساب أحمد

print("---")

account2.show_balance()  # عرض حساب سارة (لن يتأثر برصيد أحمد!)