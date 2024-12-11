# aşağıdaki menüuü oluştur
# SAYI TAHMİN OYUNU
# -----------------
# 1 - Yeni Oyun
# 2 - Yardım
# 3 - Çıkış
#  Seçiminiz: 
import random
secim="0"
sayi="0"
tahmin="0"
a=0
f=0
bildi=False

def sayi_tut():
    global sayi
    sayi = str(random.randrange(1000,10000))
    # rastgele 4 basamaklı rakamları birbirinden farklı sayı üretme
    while sayi[0]==sayi[1] or sayi[0]==sayi[2] or sayi[0]==sayi[3] or sayi[1]==sayi[2] or sayi[1]==sayi[3] or sayi[2]==sayi[3] :
        sayi = str(random.randrange(1000,10000))
    print(sayi)    

def tahmin_iste():
    global tahmin
    while 1:
        tahmin= input("tahmininiz(4 basamaklı rakamları farklı): ")
        if int(tahmin) <1000 or int(tahmin) >9999:
            continue 
        if tahmin[0]==tahmin[1] or tahmin[0]==tahmin[2] or tahmin[0]==tahmin[3] or tahmin[1]==tahmin[2] or tahmin[1]==tahmin[3] or tahmin[2]==tahmin[3]:
            continue
        break
    print("tamam")

def karsilastir():
    global a
    global f

    a =0
    if sayi[0]==tahmin[0]:
        a+=1
    if sayi[1]==tahmin[1]:
        a+=1
    if sayi[2]==tahmin[2]:
        a+=1
    if sayi[3]==tahmin[3]:
        a+=1
    print(f"aynı= {a}")
    f=0
    if sayi[0]==tahmin[1] or sayi[0]==tahmin[2] or sayi[0]==tahmin[3]:
        f+=1
    if sayi[1]==tahmin[0] or sayi[1]==tahmin[2] or sayi[1]==tahmin[3]:
        f+=1
    if sayi[2]==tahmin[0] or sayi[2]==tahmin[1] or sayi[2]==tahmin[3]:
        f+=1
    if sayi[3]==tahmin[0] or sayi[3]==tahmin[1] or sayi[3]==tahmin[2]:
        f+=1
    print(f"farklı= {f}")


def tebrik():
    print("Tebrikler! Bildiniz...")
def oyunu_baslat():
    print ("Oyun başladı")
    global bildi
    bildi=False
    global a
    sayi_tut()
    while bildi==False:
        tahmin_iste()
        karsilastir()
        if a==4:
            bildi=True
    tebrik()   
while secim!="3":
    print ("SAYI TAHMİN OYUNU")
    print ( "-----------------")
    print ( "1 - Yeni Oyun")
    print ( "2 - Yardım")
    print ( "3 - Çıkış"  )
    secim = input ( " Seçiminiz:") 
    if secim=="3":
        continue
    elif secim=="2":
        print ("Bu oyun sayı 4 basamaklıtahmin oyunudur....")
        input("devam etmek için entera bas")
    elif secim=="1":       
        # oyun oynama komutları buraya yazılacak.
        oyunu_baslat()
        input("devam etmek için entera bas")
    else:  
        print("yanlış seçim yaptınız.")
        input("deva etmekı için entera bas")
print("Güle Güle")

