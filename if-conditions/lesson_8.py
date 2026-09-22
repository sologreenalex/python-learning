temperature=int(input("Enter your Temperature :"))
if temperature <=0:
    print("ثلج شديد البرودة - تجنب الخروج")
elif temperature >0 and temperature <=15:
    print("الطقس بارد - ارتدِ ملابس ثقيلة")     
elif temperature >=16 and temperature <=30:
    print("الطقس معتدل وجميل") 
elif temperature >30:
    print("الطقس حار - اشرب الكثير من الماء")    
