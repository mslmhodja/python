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
