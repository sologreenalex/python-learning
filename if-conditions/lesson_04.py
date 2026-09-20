#العميل يحصل على خصم إذا كان VIP أو لديه Coupon.
#----------------or----------------
#False or True
#True  or True  = True
# True  or False = True
# False or True  = True
# False or False = False


is_vip=False
has_coupon=True
if is_vip or has_coupon:
    print("Discount available")