# verilen 4 basamaklı sayının her basamağını tamsayı tipinde bir dizi elemanı olarak ekleyen program.

sayi1 = "5678"  
sayi_dizi = []
sayi_dizi.append(int(sayi1[0]))
sayi_dizi.append(int(sayi1[1]))
sayi_dizi.append(int(sayi1[2]))
sayi_dizi.append(int(sayi1[3]))

# print(f"{sayi_dizi[0]}{sayi_dizi[1]}{sayi_dizi[2]}{sayi_dizi[3]}")

# 4 basamaklı sayının rakamlarının birbirinden farklı olup olmadığını bulan kod

if sayi1[0]==sayi1[1] or sayi1[0]==sayi1[2] or sayi1[0]==sayi1[3] or sayi1[1]==sayi1[2] or sayi1[1]==sayi1[3] or sayi1[2]==sayi1[3] :
  print("rakamları birbirinden farklı değil")
else:
  print("rakamları birbirinden farklıdır")

# iki tane 4 basamaklı sayıyı karşılaştır.
#   1- alt alta gelen basamakları aynı olan kaç tane var
#   5678
#   1798
#  1 tane var
#   2- alt alta olmayıp diğer basamaklarla aynı olan kaç tane var
#   5678
#   6798
#   2 tane var
sayi2="1678"
print(sayi1)
print(sayi2)
ayni =0
if sayi1[0]==sayi2[0]:
  ayni+=1
if sayi1[1]==sayi2[1]:
  ayni+=1
if sayi1[2]==sayi2[2]:
  ayni+=1
if sayi1[3]==sayi2[3]:
  ayni+=1
print(f"AYNI= {ayni}")
farkli=0
if sayi1[0]==sayi2[1] or sayi1[0]==sayi2[2] or sayi1[0]==sayi2[3]:
  farkli+=1
if sayi1[1]==sayi2[0] or sayi1[1]==sayi2[2] or sayi1[1]==sayi2[3]:
  farkli+=1
if sayi1[2]==sayi2[0] or sayi1[2]==sayi2[1] or sayi1[2]==sayi2[3]:
  farkli+=1
if sayi1[3]==sayi2[0] or sayi1[3]==sayi2[1] or sayi1[3]==sayi2[2]:
  farkli+=1
print(f"FARKLI= {farkli}")

# rastgele 4 basamaklı sayı üretme
import random
sayi = str(random.randrange(1000,10000))
# rastgele 4 basamaklı rakamları birbirinden farklı sayı üretme
i=1
while sayi[0]==sayi[1] or sayi[0]==sayi[2] or sayi[0]==sayi[3] or sayi[1]==sayi[2] or sayi[1]==sayi[3] or sayi[2]==sayi[3] :
  sayi = str(random.randrange(1000,10000))
print(sayi)

# 4 basamaklı rakamları farklı tahmin isteme
while 1:
  sayi= input("tahmininiz(4 basamaklı rakamları farklı): ")
  if int(sayi) <1000 or int(sayi) >9999:
    continue 
  if sayi[0]==sayi[1] or sayi[0]==sayi[2] or sayi[0]==sayi[3] or sayi[1]==sayi[2] or sayi[1]==sayi[3] or sayi[2]==sayi[3]:
    continue
  break
print("tamam")
