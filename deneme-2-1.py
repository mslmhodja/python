from datetime import datetime

# 1. kullanıcıdan gg/aa/yyyy (12/04/2025) formatında doğum tarihi isteyen (10p))
tarih = input("Lütfen doğum tarihinizi gg/aa/yyyy formatında girin: ")

# 2. giriş parametresi olarak string tipinde tarih bilgisini alan(50p)
#    geriye tarih tipinde değer döndüren
#    verilen string tipindeki bilginin ilk iki karakterini alıp gun bilgisi yapan
#    verilen string tipindeki bilginin 4-5 karakterleri alıp ay bilgisi yapan
#    verilen string tipindeki bilginin 7-10 karakterleri alıp yıl bilgisi yapan
#    bulduğu gün ay yıl bilgilerini kullanarak tarih formatına dönüştürerek geriye döndüren.
#   fonksiyon tanımla
def tarihe_donustur(tarih_str):
    # Tarihi parçalama
    gun = int(tarih_str[:2])  # İlk 2 karakter gün
    ay = int(tarih_str[3:5])  # 4. ve 5. karakterler ay
    yil = int(tarih_str[6:])   # 7. - 10. karakterler yıl
    return datetime(day=gun,month=ay,year=yil)

# 3. bu fonksiyonu kullanarak oluşturulan tarih bilgisini ekrana yaz.(10p)
dtarih = tarihe_donustur(tarih)
print(f"Tarih: {dtarih}")


# 4. giriş parametresi olarak string tipinde tarih bilgisini alan(30p)
#     geriye doğduğu aya göre  burcunu Döndüren fonksiyon tanımlayarak kullanıcının burcunu ekrana yaz.
# Koç	MART, Boğa	NİSAN, İkizler	MAYIS, Yengeç	HAZİRAN, Aslan	TEMMUZ, Başak	AĞUSTOS, 
# Terazi	EYLÜL, Akrep	EKİM, Yay	KASIM, Oğlak	ARALIK,Kova	OCAK, Balık	ŞUBAT 

def burc_hesapla(tarih_str):
    ay = int(tarih_str[3:5])  # 4. ve 5. karakterler ay
    burclar = {
        1: "Oğlak",    # Ocak
        2: "Kova",     # Şubat
        3: "Balık",    # Mart
        4: "Koç",      # Nisan
        5: "Boğa",     # Mayıs
        6: "İkizler",  # Haziran
        7: "Yengeç",   # Temmuz
        8: "Aslan",    # Ağustos
        9: "Başak",    # Eylül
        10: "Terazi",  # Ekim
        11: "Akrep",   # Kasım
        12: "Yay"      # Aralık
    }
    if ay==1:
        return "oğlak"
    if ay==2:
        return "kova"
    if ay==3:
        return "balık"
    if ay==4:
        return "koç"
    if ay==5:
        return "boğa"
    if ay==6:
        return "ikizler"
    if ay==7:
        return "yengeç"
    if ay==8:
        return "aslan"
    if ay==9:
        return "başak"
    if ay==10:
        return "terazi"
    if ay==11:
        return "akrep"
    if ay==12:
        return "yay"

burc = burc_hesapla(tarih)
print(f"Burcunuz: {burc}")

