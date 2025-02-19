# argümansız fomksiyon tanımlama
# ekrana 1-20 arasındaki sayıları yazma
def sayiyaz():
    for i in range(1,21):
        print(i)
sayiyaz()

# argümansız fomksiyon tanımlama , dışarıdanalınan bilgiyi kullnama
y1=int(input("1. sınav notunu gir: "))
y2=int(input("2. sınav notunu gir: "))
s1=int(input("1. sözlü notunu gir: "))
s2=int(input("2. sözlü notunu gir: "))

def ortalama():
    global y1,y2,s1,s2
    ort=(y1+y2+s1+s2)/4
    print(f"ortalama = {ort}")

ortalama()


# argümanlı fonksiyon tanımlama , dışarıdanalınan bilgiyi kullanma
# çok argümanlı fonksiyon tanımlama , dört sayının ortalaması

yaz1=int(input("1. sınav notunu gir: "))
yaz2=int(input("2. sınav notunu gir: "))
soz1=int(input("1. sözlü notunu gir: "))
soz2=int(input("2. sözlü notunu gir: "))

def ortalama(y1,y2,s1,s2):
    ort=(y1+y2+s1+s2)/4
    print(f"ortalama = {ort}")

ortalama(yaz1,yaz2,soz1,soz2)


# çok argümanlı fonksiyon tanımlama , argüman sayısı belirsiz, tüm sayıların toplamını bulma
# tüm sayıların ortalamasını bulma
def ortalama(*notlar):
    toplam=0
    for n in notlar:
      toplam+=n
    ort=toplam/len(notlar)
    print(f"ortalama = {ort}")

ortalama(8,5,15,25,62,58,97)

# tüm sayıların ortalamasını bulma kolay yolu. sum ve len fonksiyonları
def ortalama(*sayilar):
  ort=sum(sayilar) / len(sayilar)
  print(ort)
ortalama(8,5,15,25,62,58,97)

# bir sayının verilen kuvvetini yani üssünü bulan fonksiyon
def usbul(sayi,us):
  sonuc=1
  for i in range(1,us+1):
     sonuc*=sayi
  print(sonuc)

usbul(5,3)


# bir sayının verilen kuvvetini yani üssünü bulan fonksiyon, us verilmezse 2 kabul et.
def usbul(sayi,us=2):
  print(sayi**us)

usbul(5,3)




# değer dönüren fonksiyon tanımlama
# aşağıdaki polinoma verilen değere göre sonucunu bulan fonksiyon
# p(x)=5X^3 + 6x^2 + 7x +19
# p(7)
def hesapla(x):
   return 5*x**3 + 6*x**2 + 7*x +19 
print(hesapla(7))

# verilen iki dik kenarın hipotenüsünü hesaplayan fonksiyon yaz. geriye değer döndürsün.
# pow(5,2) sayının üssünü bulur, sqrt(16) karekökünü bulur.


# verilen sayının tek yada çift olduğunu döndüren fonksiyon. tek ise False çift ise True dönsun



# Bir sayının asal olup olmadığını döndüren fonksiyon. asal değil ise False asal ise True dönsun
