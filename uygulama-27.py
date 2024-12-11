# aşağıdaki menüuü oluştur
# SAYI TAHMİN OYUNU
# -----------------
# 1 - Yeni Oyun
# 2 - Yardım
# 3 - Çıkış
#  Seçiminiz: 
secim="0"
sayi="0"
tahmin="0"
a=0
f=0
bildi=False

def sayi_tut():
    global sayi
    sayi="1234"

def tahmin_iste():
    global tahmin
    tahmin=input("tahmin gir")

def karsilastir():
    global a
    global f
    a=4
    f=0
    print("Alt Alta Tutan:",a)
    print("Farklı Yerlerde Tutan:",f)

def tebrik():
    print("Tebrikler! Bildiniz...")
def oyunu_baslat():
    print ("Oyun başladı")
# 1.adım: 4 basmaklı rakamları birbirinden farklı sayı oluştur.(sayi_tut fonksiyonu)
    # 2.adım: kullanıcıdan 4 basmaklı rakamları birbirinden farklı tahmin al. (tahmin_iste fonksiyonu)
    # 3.adım: alt alta gelen sayısını bul ekrana yaz. (karsilastir fonksiyonu)
    # 4.adım: alt alta olmayıp farklı yerlerde bulunan rakam sayısını bul ekrana yaz. (karsilastir fonksiyonu)
    # 5. sayıyı bilmişse tebrik et(tebrik fonksiyonu) ve menüye dön bilmemişse 2. adıma dön
    global bildi
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

