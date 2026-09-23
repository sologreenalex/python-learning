password=0
counter=1
while counter <=3:
    password=int(input("plasse enter password :"))
    if password == 123:
        print("your password is good ")
        break
    
    counter+=1
else:
    print("access denied")

    
    