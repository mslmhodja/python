# modul yükleme
from datetime import datetime

# şu anki zaman bilgisi
print(datetime.now())
print(datetime.today())

# şu anki Yıl bilgisi
print(datetime.now().year)
# şu anki Ay bilgisi
print(datetime.now().month)
# şu anki Gün bilgisi
print(datetime.now().day)
# şu anki Saat bilgisi
print(datetime.now().hour)
# şu anki Dakika bilgisi
print(datetime.now().minute)
# şu anki saniye bilgisi
print(datetime.now().second)
# şuan haftanın kaçıncı günüdeyiz bilgisi
print(datetime.weekday(datetime.now())+1)

# doğduğum günden beri geçen süre
bugun=datetime.now()
dogumtarihi = datetime(1976,11,28)
print(dogumtarihi)
print(bugun-dogumtarihi)

# Uygulama
# kullanıcıdan doğduğu yılı ayı ve günü alıp
# 1a. şu ana kadar geçen süreyi ekrana yaz
# 1b. kaç yaşında olduğunu ekrana yaz.
bugun=datetime.now()
y=int(input("yıl: "))
a=int(input("ay: "))
g=int(input("gün: "))
dogum=datetime(y,a,g)
geçensüre= bugun-dogum

print(dogum)
print(bugun)
print(geçensüre)
bugünyıl=datetime.now().year
yaş=bugünyıl-y

print(yaş)
# 2. doğum tarihi bilgisini parametre olarak alıp şuan kaç yaşında olduğunu döndüren fonksiyon
def yas(yil,ay,gun):
    dogum=datetime(yil,ay,gun)
    buyil=datetime.now().year
    yas=buyil-yil
    return yas
print(yas(2010,8,31))
# 3. tarih bilgisini parametre olarak alıp bu tarihin hangi gün olduğunu döndüren fonksiyon
def gunbul(tarih):
    gunkac=datetime.weekday(tarih)+1
    if gunkac == 1:
        print("pazartesi")
    if gunkac == 2:
        print("salı")
    if gunkac == 3:
        print("çarşamba")
    if gunkac == 4:
        print("perşembe")
    if gunkac == 5:
        print("cuma")
    if gunkac == 6:
        print("cumartesin")
    if gunkac == 7:
        print("pazar")
gunbul(datetime(1976,11,28))

# 4. tarih bilgisini parametre olarak alıp bu tarihin hangi ay olduğunu döndüren fonksiyon
# 5. iki parametre alacak
# ilki tarih bilgisi
# ikincisi gün sayısı
# verilen tarihten gün sayısı kadar sonraki tarihi bulup geriye döndürsün.
