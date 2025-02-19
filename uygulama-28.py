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

yildiz(5)


# 1 den verilen sayıya kadar olan tüm sayıların toplamını bulan rekürsif fonksiyon

def n_toplam(n):
   if n==1: 
     return 1
   else:
     return n + n_toplam(n-1) 

print(n_toplam(5))

# ödev: N sayısının faktöriyelini bulan rekürsif fonksiyon
# ÖR: N* ..3*2*1
def n_faktoriyel(n):
  if n==1:
    return 1
  else:
    return n * n_faktoriyel(n-1)

print (n_faktoriyel(6))

# ödev: 1 den N'e kadar sayıların faktöriyellerini toplayan rekürsif fonksiyon
# ÖR: 1! + 2! + 3! + 4! + 5! + 6! + 7! ....+ N! 
def n_faktoriyel(n):
  if n==1:
    return 1
  else:
    sonuc=1
    for i in range(1,n+1):
      sonuc *= i
    return sonuc + n_faktoriyel(n-1)

print (n_faktoriyel(6))

# ödev: 1 den N'e kadar sayıların asal olanlarını bulup diziye aktaran rekürsif fonksiyon
# ÖR: 1-100 arası asal sayılar 
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89 ve 97
