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


# 1 den verilen sayıya kadarolan tüm sayıların toplanını bulan rekürsif fonksiyon

def n_toplam(n):
   if n==1: 
     return 1
   else:
     return n + n_toplam(n-1) 

print(n_toplam(5))
