# ============================================
# مشروع 3: لعبة تخمين الرقم الذكية (Number Guessing Game)
# ============================================

import random  # مكتبة لتوليد أرقام عشوائية

# 1. توليد رقم عشوائي بين 1 و 50
secret_number = random.randint(1, 50)
attempts = 0
max_attempts = 7

print("🎮 === مرحباً بك في لعبة تخمين الرقم! ===")
print(f"خمنت لك رقماً بين 1 و 50. لديك {max_attempts} محاولات لتخمينه!")

# 2. حلقة while للاستمرار حتى النجاح أو استهلاك المحاولات
while attempts < max_attempts:
    attempts += 1
    guess = int(input(f"\nالمحاولة ({attempts}/{max_attempts}) - أدخل رقمك: "))

    # فحص التخمين
    if guess == secret_number:
        print(f"🎉 رائع ومذهل! خمنت الرقم الصحيح ({secret_number}) بنجاح من المحاولة رقم {attempts}!")
        break  # الخروج من اللعبة بعد الفوز
    elif guess < secret_number:
        print("💡 الرقم المطلوب أكبر من ذلك! حاول مرة أخرى.")
    else:
        print("💡 الرقم المطلوب أصغر من ذلك! حاول مرة أخرى.")

# 3. إذا انتهت المحاولات ولم يفز
if guess != secret_number:
    print(f"\n❌ مع الأسف! انتهت جميع محاولاتك. الرقم الصحيح كان: {secret_number}")