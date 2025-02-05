# *
# **
# ***
# ****
# *****
# ******
# *******
# ********


# verilen sayı kadar yıldızı yanyana yazan rekürsif fonksiyon

def yildiz(n):
   if n==1: 
     print("*")
   else:
     y=""
     for i in range(0,n):
        y+="*"
     print(y)
     yildiz(n-1)

yildiz(15)
