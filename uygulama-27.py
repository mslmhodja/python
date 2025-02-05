# argümansız fomksiyon tanımlama
def Selamla():
  print("Selamün aleyküm gardaş")

Selamla()

# argümansız fomksiyon tanımlama , dışarıdanalınan bilgiyi kullnama
def kareBul():
  global sayi
  print(sayi*sayi)

sayi = 5
Karebul()

# argümanlı fomksiyon tanımlama , dışarıdanalınan bilgiyi kullnama
def kareBul(sayi):
  print(sayi*sayi)

kareBul(5)

# çok argümanlı fonksiyon tanımlama , iki sayının ortalaması
def OrtalamaBul(sayi1,sayi2):
  ortalama = (sayi1+sayi2)/2
  print(ortalama)

OrtalamaBul(90,70)

# çok argümanlı fonksiyon tanımlama , argüman sayısı belirsiz, tüm sayıların toplamını bulma
def toplama(*sayilar):
  toplam = 0
  for sayi in sayilar:
    toplam+=sayi
  print(toplam)
toplama(8,5,15,25,62,58,97)


# tüm sayıların ortalamasını bulma
def ortalama(*sayilar):
  toplam = 0
  for sayi in sayilar:
    toplam+=sayi
  ort=toplam / len(sayilar)
  print(ort)
ortalama(8,5,15,25,62,58,97)

# tüm sayıların ortalamasını bulma kolay yolu.
def ortalama(*sayilar):
  ort=sum(sayilar) / len(sayilar)
  print(ort)
ortalama(8,5,15,25,62,58,97)


# bir sayının ver,len kuvvetini yani üssünü bulan fonksiyon
def usbul(sayi,us)
  sonuc=1
  for i in range(1,us+1)
     sonuc*=sayi
  print(sonuc)

usbul(5,3)

# bir sayının verilen kuvvetini yani üssünü bulan fonksiyon, us verilmezse 2 kabul et.
def usbul(sayi,us=2):
  sonuc=1
  for i in range(1,us+1):
     sonuc*=sayi
  print(sonuc)

usbul(5)
usbul(5,4)

# değer dönüren fonksiyon tanımlama
# bir sayının verilen kuvvetini yani üssünü bulan fonksiyon
# p(x)=5X^3 + 6x^2 + 7x +19
# p(7)

def usbul(sayi,us=2):
  sonuc=1
  for i in range(1,us+1):
     sonuc*=sayi
  return sonuc
  
s = usbul(5,4)

print(s)

print(5*usbul(7,3) + 6*usbul(7,2) + 6*usbul(7,1) + 19)



# kendi kendini çağıraan yada tekrarlı fonksiyonlar.


