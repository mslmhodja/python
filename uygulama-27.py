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
