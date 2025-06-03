# 📌 Fonksiyon: İki sınav notunun ortalamasını hesaplar
def ortalama_hesapla(n1, n2):
    return (n1 + n2) / 2  # İki notun toplamı 2'ye bölünerek ortalama alınır

# 📌 Fonksiyon: Ortalama 50 ve üzeriyse "Geçti", değilse "Kaldı" döner
def gecti_mi(ortalama):
    if ortalama >= 50:
        return "Geçti"
    else:
        return "Kaldı"

# 📌 Fonksiyon: Öğrenci ekleme işlemi yapar
def ogrenci_ekle(ogrenciler):
    ad = input("Öğrenci adı: ")  # Kullanıcıdan öğrenci adı alınır
    try:
        not1 = float(input("1. sınav notu: "))  # 1. sınav notu alınır (ondalıklı olabilir)
        not2 = float(input("2. sınav notu: "))  # 2. sınav notu alınır

        # Notların geçerli aralıkta olup olmadığı kontrol edilir
        if not (0 <= not1 <= 100 and 0 <= not2 <= 100):
            print("⚠️ Notlar 0-100 arasında olmalı!")
            return  # Fonksiyon durdurulur

        ort = ortalama_hesapla(not1, not2)  # Ortalama hesaplanır
        durum = gecti_mi(ort)  # Geçti mi kaldı mı bilgisi alınır

        # Bilgiler listeye tuple olarak eklenir
        ogrenciler.append((ad, not1, not2, ort, durum))

        # Kullanıcıya bilgi verilir
        print(f"{ad} eklendi. Ortalama: {ort:.2f} → {durum}")
    except:
        # Hatalı sayı girilirse burası çalışır
        print("⚠️ Geçersiz not girdiniz! Lütfen sayı girin.")

# 📌 Fonksiyon: Öğrenci listesini ekrana yazdırır
def ogrencileri_goster(ogrenciler):
    if not ogrenciler:
        print("Henüz öğrenci eklenmedi.")  # Liste boşsa bilgi ver
    else:
        print("\n📋 Öğrenci Listesi:")
        for ogr in ogrenciler:
            # Her öğrencinin bilgileri ekrana yazdırılır
            print(f"→ {ogr[0]} - Not1: {ogr[1]}, Not2: {ogr[2]}, Ort: {ogr[3]:.2f}, Durum: {ogr[4]}")

# 📌 Fonksiyon: Öğrenci listesini bir dosyaya kaydeder
def dosyaya_kaydet(ogrenciler):
    try:
        # Dosya yazma modunda açılır (eski içerik silinir)
        dosya = open("notlar.txt", "w", encoding="utf-8")

        # Her öğrencinin bilgileri dosyaya yazılır
        for ogr in ogrenciler:
            satir = f"{ogr[0]} - Not1: {ogr[1]}, Not2: {ogr[2]}, Ort: {ogr[3]:.2f}, Durum: {ogr[4]}\n"
            dosya.write(satir)

        dosya.close()  # Dosya manuel olarak kapatılır
        print("✅ Bilgiler 'notlar.txt' dosyasına kaydedildi.")
    except:
        # Herhangi bir dosya hatasında burası çalışır
        print("⚠️ Dosya yazma hatası")

# 📌 Fonksiyon: Kayıtlı öğrencileri dosyadan okuyup listeye aktarır
def dosyadan_oku(ogrenciler):
    try:
        # Dosya okuma modunda açılır
        dosya = open("notlar.txt", "r", encoding="utf-8")
        satirlar = dosya.readlines()  # Tüm satırlar okunur
        dosya.close()  # Dosya kapatılır

        if not satirlar:
            print("❗ Dosya boş. Henüz öğrenci kaydedilmemiş.")
            return

        ogrenciler.clear()  # Önce mevcut liste temizlenir

        print("\n📄 Dosyadaki Öğrenciler:")
        for satir in satirlar:
            print(f"→ {satir.strip()}")  # Satır yazdırılır (\n olmadan)

            try:
                # Satırdan veriler ayrıştırılır

                parcalar = satir.strip().split(" - ")  # Satırın başındaki/sonundaki boşluklar ve \n silinir, sonra " - " işaretine göre ikiye bölünür
                ad = parcalar[0]  # İlk parça öğrencinin adıdır (örnek: "Ali")

                diger = parcalar[1].split(", ")  # İkinci parça (örnek: "Not1: 80, Not2: 90, Ort: 85.0, Durum: Geçti") virgüllerle bölünür

                not1 = float(diger[0].split(": ")[1])  # "Not1: 80" ifadesinden ":" sonrası alınır → "80", sonra float'a çevrilir
                not2 = float(diger[1].split(": ")[1])  # "Not2: 90" → "90" → 90.0
                ort = float(diger[2].split(": ")[1])   # "Ort: 85.0" → "85.0" → 85.0
                durum = diger[3].split(": ")[1]        # "Durum: Geçti" → "Geçti" (metin olduğu için float'a çevrilmez)

                # Öğrenci listesine eklenir
                ogrenciler.append((ad, not1, not2, ort, durum))
            except:
                print("⚠️ Satırdan veri ayrıştırılamadı!")
    except:
        print("❗ Dosya bulunamadı. Önce kaydetmelisiniz.")

# 📌 Ana Menü: Kullanıcının işlem seçmesini sağlar
def menu():
    ogrenciler = []  # Başlangıçta boş bir liste tanımlanır

    while True:  # Kullanıcı çıkana kadar menü gösterilir
        print("\n📌 MENÜ")
        print("1 - Öğrenci Ekle")
        print("2 - Öğrencileri Göster")
        print("3 - Dosyaya Kaydet")
        print("4 - Dosyadan Oku ve Listeye Aktar")
        print("0 - Çıkış")

        secim = input("Bir seçenek girin (0-4): ")

        # Seçime göre uygun işlem yapılır
        if secim == '1':
            ogrenci_ekle(ogrenciler)
        elif secim == '2':
            ogrencileri_goster(ogrenciler)
        elif secim == '3':
            dosyaya_kaydet(ogrenciler)
        elif secim == '4':
            dosyadan_oku(ogrenciler)
        elif secim == '0':
            print("👋 Programdan çıkılıyor...")
            break  # Döngü sonlandırılır
        else:
            print("⚠️ Geçersiz seçim! Lütfen 0-4 arasında bir sayı girin.")

# 📌 Programın başlangıç noktası
menu()
