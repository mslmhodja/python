# klasör komutları kütüphanesini yükler
import os

#aktif diziin yolunu verir
dizin = os.getcwd()
print(dizin)

#verilen dizinin son klasörüne göre ikiye ayırır.
liste = os.path.split(dizin)
print(liste)

#verilen yola hakan isimli klasörü ekler
sonuc = os.path.join(dizin,"hakan")
print(sonuc)

#bir klasörün olup olmadığını kontrole der.
if os.path.exists(sonuc):
  # aktif klasörü değiştirir.
  os.chdir(sonuc)

# verilen yolun klasör olup olmadığını kontrol eder.
if os.path.isdir(sonuc):
  os.chdir(sonuc)


