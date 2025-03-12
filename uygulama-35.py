# string birleştirme
ad = "Hakan"
soyad = "KARATAŞ"

isim = ad + " (" + soyad + ")"
print(ad,soyad,isim)

# ismin 4. karakteri ile 8.karakterini yaz.

print(isim[3] + isim[7] )


# ismin uzunluuğunu bulma.
print(len(isim))

# bir sayının dört basmaklı olup olmadığını kontrol etme
sayi=1208

if len(str(sayi)) == 4:
    print ("dört basamklı")
else:
    print ("dört basamklı değil")

#stringi parçalara ayırma ve cümledeki kelime sayısını bulma

cumle = "Represents a duration the difference between two dates or times Timedelta is the pandas equivalent of pythons datetime timedelta and is interchangeable"
kelimeler = cumle.split(" ")
print(kelimeler)
print(len(kelimeler))


# bir tarih metninden yılı alma.
tarih ="15 mayıs 2024 saat 19:34"
print(tarih[9:13])

# sona yada başa kadar alma
print(tarih[:13])
print(tarih[9:])

# bir cümle içndeki türkçe kararkterleri ingilizceye çevirme fonksiyonu
def cevir(cumle):   
    cumle = cumle.replace("ç","c")
    cumle = cumle.replace("ğ","g")
    cumle = cumle.replace("ı","i")
    cumle = cumle.replace("ö","o")
    cumle = cumle.replace("ş","s")
    cumle = cumle.replace("ü","u")
    cumle = cumle.replace("Ç","C")
    cumle = cumle.replace("Ğ","G")
    cumle = cumle.replace("İ","I")
    cumle = cumle.replace("Ö","O")
    cumle = cumle.replace("Ş","S")
    cumle = cumle.replace("Ü","U")
    return cumle

metin = "Bankamız ile çalışıyorsanız, hesaplarınızın olduğu şubeye giderek bu talebinizi iletmeniz ve POS başvuru formunu doldurmanız yeterli olacaktır."
print(cevir(metin))


# bir cümle başıbdaki boşlukları çıkartma.
metin = " Bankamız ile çalışıyorsanız, hesaplarınızın olduğu şubeye giderek bu talebinizi iletmeniz ve POS başvuru formunu doldurmanız yeterli olacaktır. "
print(metin)
print(metin.strip())

# bir cümle başındaki Ban metnini çıkarma çıkartma.
metin = " Bankamız ile çalışıyorsanız, hesaplarınızın olduğu şubeye giderek bu talebinizi iletmeniz ve POS başvuru formunu doldurmanız yeterli olacaktır. "
print(metin)
print(metin.strip("Ban")) # başında boşluk var. çıkarmaz
print(metin.strip(" Ban"))

# karakter ekleme
kelime ="İstanbul"
harf="-"
print(harf.join(kelime))

#bir metin içnde bir kelime arayıp bulduğu yere başka bir kelime ekleme
metin = "Bankamız ile çalışıyorsanız, hesaplarınızın olduğu şubeye giderek bu talebinizi iletmeniz ve POS başvuru formunu doldurmanız yeterli olacaktır."
kelime="talebinizi"
yenisi ="isteğinizi"

yer = metin.find(kelime)
print(yer)
print(metin[:yer] + yenisi+ metin[yer+len(kelime):])

# bir metin içinde bir karakter  varmı yokmu?
user = "adminMehmet.34"
if "Admin" in user:
    print("geçersiz kullanıcı")
else:
    print("geçerli kullanıcı")

# büyük küçük harf fonksiyonları
metin = "mUSTAFA kARATAŞ"
print(metin)
print(metin.upper())
print(metin.lower())
print(metin.capitalize())
print(metin.title())
print(metin.swapcase())

